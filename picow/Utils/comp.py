import time
import math
from .neo_canvas import Canvas
from .color import Scale as ScaleColor
from .color import get_color_from_hsv

class Comp(object):
    def __init__(self, name):
        self._enter_time = -1
        self._exit_time = -1
        
        self.time = -1
        self._last_update_time = -1

        self.delta_time = -1
        self._last_dalta_time = -1

        self.name = name
        self.b_always_update = False    # if true, update will be called even if it's not the current app
        self.b_active = False 

    def enter(self, time):
        self._enter_time = time
        self.b_active = True

    def exit(self, time):
        self._exit_time = time
        self.b_active = False

    def pre_update(self, time, delta_time):
        self.time = time
        self.delta_time = delta_time

    def on_update_do(self):
        pass

    def update(self, time, delta_time):
        self.pre_update(time, delta_time)
        self.on_update_do()
        self.post_update()

    def post_update(self):
        self._last_update_time = self.time
        self._last_dalta = self.delta_time

    def on_rot_change(self, delta):
        pass

    def on_button_down(self):
        pass




class LedBlinker(Comp):
    def __init__(self, name, led, on_interval=0.3, off_interval=0.2, on_led_turn_on_func=None, on_led_turn_off_func=None):
        super(LedBlinker, self).__init__(name)
        self.led = led
        self.bOn = False
        self.on_callback = on_led_turn_on_func
        self.off_callback = on_led_turn_off_func
        self.on_interval = on_interval
        self.off_interval = off_interval

        self.last_led_on_time = -1
        self.last_led_off_time = -1


    def enter(self, time):
        super().enter(time)
        self.turn_led_on(True)

    def on_update_do(self):
        if self.bOn:
            if self.time - self.last_led_on_time > self.on_interval:
                self.turn_led_on(False)
        else:
            if self.time - self.last_led_off_time > self.off_interval:
                self.turn_led_on(True)

    def turn_led_on(self, bOn):
        self.led.value = bOn
        self.bOn = bOn
        if bOn:
            self.last_led_on_time = self.time
            if self.on_callback:
                self.on_callback()
        else:
            self.last_led_off_time = self.time
            if self.off_callback:
                self.off_callback()


class DigitalClock(Comp):
    def __init__(self, canvas:Canvas, font, color, b24Hour=True, show_second=True):
        name = "DigitalClock"
        super(DigitalClock, self).__init__(name)
        self.canvas = canvas
        self.font = font
        self.color = color 
        
        

        self.font_height = 5
        self.b24Hour = b24Hour
        self.show_second = show_second
        
        self.local_time = time.localtime()

        self.on_interval = 0.5
        self.off_interval = 0.5
        self.last_blink_time = -1
        self.last_local_time = None

        self.tm_wday = 0  #days since Sunday
        
        self.phi = 0

        self.auto_color = self.color is None
        self.hue_offset = 0
        if self.auto_color:
            self.color = self.get_color_from_time()
        
        self.extra_text = "---"
        
        
    def get_color_from_time(self, offset=0):
        h = self.local_time.tm_hour
        m = self.local_time.tm_min
        s = self.local_time.tm_sec
        # hue 0-360
        hue = ((m * 60 + s) / 3600 * 360 + self.hue_offset + offset) % 360
        return get_color_from_hsv(hue, 1, 255)

    def time_to_str(self):
        odd_second = self.local_time.tm_sec % 2
        if self.b24Hour:
            sep = ':' if odd_second else chr(31) # us ascii 31 is unit separator
            if self.show_second:
                return '{:02d}{}{:02d}{}{:02d}'.format(self.local_time.tm_hour, sep, self.local_time.tm_min, sep, self.local_time.tm_sec)
            else:
                return '{:02d}{}{:02d}'.format(self.local_time.tm_hour, sep, self.local_time.tm_min)
        else:
            if self.show_second:
                return '{:02d}:{:02d}:{:02d}'.format(self.local_time.tm_hour % 12, self.local_time.tm_min, self.local_time.tm_sec)
            else:
                return '{:02d}:{:02d}'.format(self.local_time.tm_hour % 12, self.local_time.tm_min)
    
    def set_time(self, seconds):
        self.local_time = time.localtime(seconds)

    def on_update_do(self):
        local_time = time.localtime()
        if local_time != self.local_time:
            self.tm_wday = local_time.tm_wday
            if self.auto_color and self.last_local_time:
                self.color = self.get_color_from_time()

            self.local_time = local_time
            self.last_time = self.time
            self.phi = 0
            self.draw()
            self.last_local_time = local_time

        self.phi += self.delta_time

        v = min(abs(0.5-max(0, self.phi - 0.2)) * 2, 1)

        if self.show_second:
            coords = [(8, 1), (8, 3), (18, 1), (18, 3)]
        else:
            coords = [(8, 1), (8, 3)]
        x = self.get_time_num_start_x()
        for coord in coords:
            self.canvas.set_pixel(coord[0] + x, coord[1] + 1, ScaleColor(self.color, v))
        self.canvas.flush()

    def on_button_down(self):
        self.change_mode()
        
    def set_extra_text(self, text):
        print("set_extra_text called: {}".format(text))
        self.extra_text = str(text) if not isinstance(text, str) else text
    
    def get_time_num_start_x(self):
        return 3 if self.show_second else 15

    def draw(self):
        if self.canvas:
            text = self.time_to_str()

            self.canvas.show_text(text, x_offset=self.get_time_num_start_x(), y_offset=1, color=self.color)
            # show extra text
            if self.extra_text and not self.show_second:
                self.canvas.show_text(self.extra_text, x_offset=2, y_offset=1
                                , color=self.get_color_from_time(offset=100))
            for i in range(7):
                x = i * 4 + 3
                y = 7
                for j in range(3):
                    self.canvas.set_pixel(x + j, y, [255, 255, 255] if i == self.tm_wday  else [64, 64, 64])
                self.canvas.set_pixel(x + 3, y, [0, 0, 0])
                    
                    

    def enter(self, time):
        super().enter(time)

    def exit(self, time):
        super().exit(time)
        self.canvas.clear(bFlush=False)

    @property
    def width(self):
        if self.show_second:
            return 4+4 + 1 + 4+4 + 1 + 4+4
        else:
            return 4+4 + 1 + 4+4 + len(self.extra_text) * 4 
        
    @property
    def height(self):
        return self.font_height

        
    def clear(self, bFlush):
        if self.canvas:
            for x in range(2, 32):
                for y in range(1, 1 + self.font_height):
                    self.canvas.set_pixel(x, y, [0, 0, 0])
            for x in range(2, 28):
                self.canvas.set_pixel(x, 7, [0, 0, 0])
            if bFlush:
                self.canvas.flush()
            

    def change_mode(self):
        self.clear(bFlush=False)

        self.show_second = not self.show_second

        self.draw()

    def change_hue(self, hue_delta):
        self.hue_offset += hue_delta
        self.color = self.get_color_from_time()
        self.draw()
        
    def on_rot_change(self, delta):
        self.change_hue(delta * 10)



