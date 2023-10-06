from .color import *
from .layer import Layer
from .font_5x7 import font_3x5

UPPER_LEFT = 0
UPPER_RIGHT = 1
LOWER_LEFT = 2
LOWER_RIGHT = 3

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3


class Canvas(object):
    '''
    封装显示版顺序及朝向带来的变化
    '''
    def __init__(self, width, height, orders, neo_pixels=None):
        self.width = width
        self.height = height

        self.orders = orders

        self.layers = []
        self.layer_opacity = []
        self.raw_pixels = [(0, 0, 0) for i in range(width*height)]    # raw pixel orders, neo pixel's order , id 0 may not the upper left

        self.neo_pixels = neo_pixels
        self.b_dirty = False

    def get_index(self, x, y):
        return self.orders[x * self.height + y]

    def set_pixel(self, x, y, color):
        index = x * self.height + y
        if 0 <= index < len(self.raw_pixels):
            self.raw_pixels[self.orders[index]] = color
            self.b_dirty = True
        return False

    def set_pixels_from_bytes(self, content_bytes, bFlush=True):
        print("set_pixels_from_bytes call: {} bytes".format(len(content_bytes)))
        
        index = 0
        for i in range(0, len(content_bytes), 3):
            color = (int(content_bytes[i])/255.0, int(content_bytes[i+1])/255.0, int(content_bytes[i+2])/255.0)
            color = (int(color[0]*color[0]*255) , int(color[1]*color[1]*255), int(color[2]*color[2]*255))
            self.raw_pixels[self.orders[index]] = color
            if index == 0:
                print("color: {}".format(color))
            index += 1
        if bFlush:
            self.flush()

    def set_pixels(self, pixels):
        for i, pixel in enumerate(pixels):
            self.raw_pixels[self.orders[i]] = pixel
            self.b_dirty = True

    def get_pixel(self, x, y):
        return self.raw_pixels[self.orders[x * self.height + y]]

    def get_pixels(self):
        # get the pixels in logic order, y first,
        for x in range(self.width):
            for y in range(self.height):
                yield self.raw_pixels[self.orders[x * self.height + y]]
        

    def __len__(self):
        return len(self.raw_pixels) if self.raw_pixels else 0

    def print(self):
        for y in range(self.height):
            s = ""
            for x in range(self.width):
                s += "{} ".format(self.orders[y][x])
                if self.orders[y][x] < 10:
                    s += " "
            print(s)


    def add_layer(self, layer):
        if layer:
            self.layers.append(layer)
        else:
            print("Layer == null")

    def flush(self):
        if not self.b_dirty:
            return
        
        if self.neo_pixels:
            for i, pixel in enumerate(self.raw_pixels):
                self.neo_pixels[i] = pixel
            self.neo_pixels.write()
        else:
            print("Warning: self.neo_pixel == none")
        self.b_dirty = False

    def show_debug_order(self, colors=[red, green, blue]):
        self.neo_pixels.fill(black)
        self.neo_pixels.write()
        for color in colors:
            for i, x in enumerate(self.orders):
                self.neo_pixels[x] = color
                self.neo_pixels.write()

    def set_rect(self, x, y, width, height, color):
        b = False
        for i in range(width):
            for j in range(height):
                b |= self.set_pixel(x + i, y + j, color)
        self.b_dirty |= b
            
    def clear(self, bFlush=True):
        self.raw_pixels = [(0, 0, 0) for i in range(self.width*self.height)]
        if bFlush:
            self.flush()
           
    def show_text(self, text: str, font=font_3x5, x_offset=0, y_offset = 0, color=white, override_colors=None):
        
        font_width = 3 if font == font_3x5 else 5
        font_height = 5 if font == font_3x5 else 7
        for i, c in enumerate(text):
            if c not in font:
                self.set_rect(x_offset, y_offset, font_width+1, font_height, color)
                x_offset += font_width + 1
                continue
            column_bytes = font[c]
            
            bTransparent = c == chr(31)
                        
            for j, column_byte in enumerate(column_bytes):
                column_value = bin(column_byte)[2:]
                while len(column_value) < font_height:
                    column_value = "0" + column_value
                for k, s in enumerate(column_value):
                    if k >= font_height:
                        break
                    if s == '1':
                        if not bTransparent:
                            self.set_pixel(x_offset + j, k+y_offset, color)
                    else:
                        if not bTransparent:
                            self.set_pixel(x_offset + j, k+y_offset, black)

            x_offset += len(column_bytes) + 1
        return True 