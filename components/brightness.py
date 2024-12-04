from math import floor

class Brightness:
    def get_level(self, device):
       brightness_value = int(device.shell("settings get system screen_brightness").strip()) / 255

       return floor(1*(1-brightness_value) + 100 * brightness_value)

    def set_level(self, device, level):
        device.shell(f"settings put system screen_brightness {int(level)}")

    def __init__(self, ui):
        self.ui = ui
