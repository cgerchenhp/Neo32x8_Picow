import io, os
import time
import rtc # real time clock
import adafruit_ntp 
import random
import json

import digitalio
import rotaryio
import board

import neopixel
import adafruit_matrixkeypad

import ssl
import ipaddress
import wifi
import socketpool
import adafruit_requests


from Utils.comp import LedBlinker

from Utils.color import *
from Utils.neo_canvas import Canvas
from Utils.neo_utils import order_32x8_rev, show_debug_order
from Utils.comp import Comp
from Utils.comp import DigitalClock
from Utils.local_network_comp import NetFetcher, GitStars, Settings

from Utils.font_5x7 import font_3x5

try:
    settings = json.loads(open("my_settings.json", "r").read())
    print("Setting loaded. {}".format(settings.keys()))
except Exception as e:
    print("Error: load settings.json\n", str(e))
    settings = {
        "Brightness": 0.2
    }


print("hello world.    " * 4)
print(os.getenv("CIRCUITPY_WIFI_SSID"))
# https://learn.adafruit.com/pico-w-wifi-with-circuitpython/pico-w-json-feed-openweathermap


# NeoPixel 
neo_width = 32; neo_height = 8
led_count = neo_width * neo_height
settings["Brightness"]

neo = neopixel.NeoPixel(board.GP28, led_count, brightness=settings["Brightness"], auto_write=False)
neo.fill([255, 64, 0])
neo.write()

neo_canvas = Canvas(neo_width, neo_height, order_32x8_rev, neo_pixels=neo)

# Time rtc
def get_rtc_from_internet():
    wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))
    pool = socketpool.SocketPool(wifi.radio)
    ntp = adafruit_ntp.NTP(pool, tz_offset=8)
    return ntp.datetime

try:
    rtc.RTC().datetime = get_rtc_from_internet()
    print("RTC time: {}".format(rtc.RTC().datetime))
except Exception as e:
    print("Error: get_rtc_from_internet\n", str(e))




# LEDs Start
board_led = digitalio.DigitalInOut(board.LED)
board_led.direction = digitalio.Direction.OUTPUT
board_led.value = True

board_led_blinker = LedBlinker("led_blinker", board_led, on_interval=0.1, off_interval=0.3)

status_led = digitalio.DigitalInOut(board.GP22)
status_led.direction = digitalio.Direction.OUTPUT
status_led_blinker = LedBlinker("status_led_blinker", status_led, on_interval=0.3, off_interval=0.7)
# LEDs End

def init_keypad_4x4():
    # keypad
    cols = [digitalio.DigitalInOut(x) for x in (board.GP9, board.GP8, board.GP7, board.GP6)]
    rows = [digitalio.DigitalInOut(x) for x in (board.GP13, board.GP12, board.GP11, board.GP10)]
    keys = (('1', '2', '3', 'A')
          , ('4', '5', '6', 'B')
          , ('7', '8', '9', 'C')
          , ('*', '0', '#', 'D'))
    return adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)
    

def connect_wifi():
    wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))
    print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])
    print("My IP address is", wifi.radio.ipv4_address)
    pool = socketpool.SocketPool(wifi.radio)
    requests = adafruit_requests.Session(pool, ssl.create_default_context())
    #ipv4 = ipaddress.ip_address("8.8.4.4")
    return pool, requests


# functions
def get_time():
    return time.monotonic_ns() / 1000_000_100

last_time = get_time()

rotator_a = rotaryio.IncrementalEncoder(board.GP16, board.GP17)
rotator_btn = digitalio.DigitalInOut(board.GP18)
rotator_btn.direction = digitalio.Direction.INPUT
rotator_btn.pull = digitalio.Pull.UP
rot_a_last_position = 0

BUTTON_FREE_VALUE = True if rotator_btn.pull == digitalio.Pull.UP else False
rotator_btn_status = BUTTON_FREE_VALUE

#buttons
buttons = [digitalio.DigitalInOut(gp_x) for gp_x in [board.GP19, board.GP20, board.GP21]]
for btn in buttons:
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
buttons_status = [BUTTON_FREE_VALUE for _ in buttons]

#keypad = init_keypad_4x4()

try:
    pool, requests = connect_wifi()
    print("req: {}".format(requests))
    
    quotes_url = "http://192.168.1.31:8080/"
    response = requests.get(quotes_url)
    print("response: {}".format(response.text))
except Exception as e:
    print("Error: connect_wifi\n", str(e))
    

# net_fetcher = NetFetcher(neo_canvas, requests, interval=2, on_get_func=None)
# Clock

clock_comp = DigitalClock(neo_canvas, font_3x5, color=None, b24Hour=True, show_second=False)
settings_comp = Settings("settings", neo_canvas, settings["Brightness"])
github_comp = GitStars("github", neo_canvas, requests, interval=600, star_receiver_comp=clock_comp)

# Apps

apps = [clock_comp, settings_comp, github_comp]
app_index = -1

def next_app():
    global app_index
    app_index = (app_index + 1) % len(apps)
    return apps[app_index]

current_app = next_app()
current_app.enter(get_time())

CLEAR_BUTTON_ID = 0
MODE_BUTTON_ID = 1
APP_BUTTON_ID = 2

while True:
    
    time.sleep(0.02)

    current_time = get_time()
    delta_time = current_time - last_time

    board_led_blinker.update(current_time, delta_time)
    status_led_blinker.update(current_time, delta_time)
    
     
    position_a = rotator_a.position
    if rot_a_last_position is None or position_a != rot_a_last_position:
        print(position_a)
        is_rot_a_action = True
        delta = position_a - rot_a_last_position

        current_app.on_rot_change(delta)

        rot_a_last_position = position_a
        
    if rotator_btn.value != rotator_btn_status:
        bDown = rotator_btn.value != BUTTON_FREE_VALUE
        rotator_btn_status = rotator_btn.value
        
        print("rotator_btn {}".format("down" if bDown else "up"))
    
    for i, btn in enumerate(buttons):
        if btn.value != buttons_status[i]:
            bDown = btn.value != BUTTON_FREE_VALUE
            buttons_status[i] = btn.value
            print("button {} {}".format(i, "down" if bDown else "up"))
            if i == APP_BUTTON_ID:
                if bDown:
                    current_app.exit(current_time)
                    current_app = next_app()
                    current_app.enter(current_time)
            elif i == MODE_BUTTON_ID:
                if bDown:
                    current_app.on_button_down()
            elif i == CLEAR_BUTTON_ID:
                if bDown:
                    neo.fill([255, 64, 0])
                    neo.write()

    
    current_app.update(current_time, delta_time)
    for app in apps:
        if app != current_app and app.b_always_update:
            app.update(current_time, delta_time)

    
    neo_canvas.flush()

    last_time = current_time
# while end
