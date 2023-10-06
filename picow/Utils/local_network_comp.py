import time, os
import math

import ssl
import ipaddress
import wifi

import supervisor
import ssl
import adafruit_requests
import socketpool
import binascii

from .comp import Comp
from .color import *
from .font_5x7 import font_3x5

from .neo_canvas import Canvas


class GitStars(Comp):
    def __init__(self, name, canvas:Canvas, requests, interval=600, star_receiver_comp=None):
        super(GitStars, self).__init__(name)
        self.canvas = canvas
        self.requests = requests
        self.interval = interval
        self.star_count = -1
        self.b_always_update = True # can run in backgound
        self.star_receiver_comp = star_receiver_comp
        self.last_fetch_time = -1
        
        self.fetch_and_send()

    def enter(self, time):
        super().enter(time)
        self.canvas.clear() # todo, clear only the area that this comp will draw
        self.draw()
    
    def exit(self, time):
        super().exit(time)
        self.canvas.clear(bFlush=False)

    def draw(self):
        self.canvas.show_text("STAR:{}{}".format(chr(31), self.star_count)
                    , font=font_3x5, x_offset=0, y_offset=1, color=yellow, override_colors=None)
    
    def fetch_star_count(self):
        # get data from local server
        quotes_url = "http://192.168.1.31:8080/tapython"
        try:
            response = self.requests.get(quotes_url)
            json_data = response.json()
            if "stars" in json_data:
                self.star_count = json_data["stars"]

        except Exception as e:
            print("Error: fetch_star_count\n", str(e))
            return
    
    def fetch_and_send(self):
        self.fetch_star_count()
        if self.star_receiver_comp:
            self.star_receiver_comp.set_extra_text(str(self.star_count))

    def on_update_do(self):
        if self.time - self.last_fetch_time > self.interval:
            self.fetch_and_send()

            if self.b_active:
                self.draw()
            self.last_fetch_time = self.time

        

class Settings(Comp):
    def __init__(self, name, canvas:Canvas, brightness):
        super(Settings, self).__init__(name)
        self.canvas = canvas
        self.brightness = brightness

    def draw(self):
        self.canvas.show_text("BRI:{}{:.2f}".format(chr(31), self.brightness)
                            , font=font_3x5, x_offset=0, y_offset=1, color=white, override_colors=None)
        
    def enter(self, time):
        super().enter(time)
        self.canvas.clear()
        self.draw()

    def exit(self, time):
        super().exit(time)
        self.canvas.clear(bFlush=False)

    def on_rot_change(self, delta) -> bool:
        self.brightness += delta * 0.02
        self.brightness = min(1, max(0, self.brightness))

        self.canvas.neo_pixels.brightness = self.brightness

        self.draw()        
        


class NetFetcher(Comp):
    def __init__(self, canvas, requests, interval=2, on_get_func=None):
        name = "NetFetcher"
        super(NetFetcher, self).__init__(name)
        
        self.requests = requests
        self.canvas = canvas
        self.interval = interval
        self.on_get_callback = on_get_func

        self.b_enabled = True
        self.task = "1"

        self.last_fetch_time = -1


    def enter(self, time):
        super().enter(time)

    def fetch_from_local_network(self):
        start_msecs = supervisor.ticks_ms()
        print("fetch_from_local_network")
        if not self.requests:
            return
        quotes_url = "http://192.168.1.31:8080/pico_test"
        try:
            response = self.requests.get(quotes_url)
            json_data = response.json()
            if "image_content" in json_data:
                image_content_64 = json_data["image_content"]
                image_content = binascii.a2b_base64(image_content_64)

                print("image_content: {}".format(len(image_content)))
                self.canvas.set_pixels_from_bytes(image_content)
            stop_msecs = supervisor.ticks_ms()
            print("elapsed time = ", (stop_msecs - start_msecs)/1000)
        except Exception as e:
            print("Error: fetch_from_local_network\n", str(e))
            return
        

    def on_update_do(self):
        
        if not self.b_enabled:
            return
        
        
        if self.time - self.last_fetch_time > self.interval:
            
            self.fetch_from_local_network()
            self.last_fetch_time = self.time

            
