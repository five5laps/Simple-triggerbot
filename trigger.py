import time

import keyboard
import pyautogui
from PIL import ImageGrab

key_pressed = False
prev_pixel_color = None


def get_pixel(x, y):
    return ImageGrab.grab().getpixel((x, y))


def on_key_event(e):
    global key_pressed

    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'alt':
            key_pressed = True
        else:
            pass
    elif e.event_type == keyboard.KEY_UP:
        if e.name == 'alt':
            key_pressed = False
        else:
            pass


keyboard.hook(on_key_event)

try:
    while True:
        if key_pressed:
            pixel_color = get_pixel(577, 433)
            if prev_pixel_color is None:
                prev_pixel_color = pixel_color
            elif prev_pixel_color is not None and pixel_color != prev_pixel_color:
                pyautogui.mouseDown()
                time.sleep(0.1)
                pyautogui.mouseUp()
                prev_pixel_color = None
            time.sleep(0.1)
        else:
            prev_pixel_color = None
            time.sleep(0.5)
except KeyboardInterrupt:
    print("Closed.")
