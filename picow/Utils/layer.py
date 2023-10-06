from .color import *


class Layer(object):
    def __init__(self, width, height, pixels=[]):
        self.width = width
        self.height = height
        if pixels:
            if len(pixels) == self.width * self.height:
                self._pixels = pixels
            else:
                print("Pixel count not match: {} vs {}".format(self.width * self.height, len(pixels)))
        else:
            self._pixels = []

        self.blend_mode = None
        self.enabled = True
        self.mask = None
        self.opacity = 1
        self.out_colors = self.pixels[:]
        self.modify()


    def __len__(self):
        return len(self.pixels)

    @property
    def pixels(self):
        return self._pixels

    @pixels.setter
    def pixels(self, pixels):
        if pixels and len(pixels) == self.width * self.height:
            self._pixels = pixels
            self.modify()

    def tint(self, color):
        new_pixels = list([Multiply(pixel, color) for pixel in self.pixels])
        self.pixels = new_pixels
        self.modify()


    def modify(self):
        self.calculate()

    def calculate(self):
        if len(self.out_colors) != len(self.pixels):
            self.out_colors = [] * len(self.pixels)
        for i, p in enumerate(self.pixels):
            out_c = p if len(p) == 4 else [p[0], p[1], p[2], 255]
            if self.opacity != 1:
                out_c[3] *= self.opacity
            if self.mask:
                if self.mask[i] != 255:
                    out_c[3] *= self.mask[i] / 255.0
                    # print("out_c[3] * self.mask[i] / 255.0 : {}, mask: {}".format(out_c[3], self.mask[i]))
            self.out_colors[i] = out_c

    def apply_mask(self, mask):
        self.mask = mask
        self.modify()


    # @staticmethod
    # def Blend(upper_layer, lower_layer):
    #     return [Blend(a[i], b[i]) for i in range(len(a))]

    @staticmethod
    def BlendWithBuffer(upper_layer, buffer):
        result = []
        for i, c in enumerate(upper_layer.out_colors):
            # print("c: {}  buffer: {}".format(c, buffer[i]))
            # if i == 0:
            #     print("buffer[0].a: {} upper.a: {}".format(buffer[i][3], c[3]))
            result.append(AlphaBlend(c[:3], buffer[i][:3], c[3], buffer[i][3]))
        return result

    @staticmethod
    def from_layer(layer):
        result = Layer(width=layer.width, height=layer.height, pixels=layer.pixels[:] )
        result.mask = layer.mask
        result.enabled = True
        result.blend_mode = layer.blend_mode
        return result


