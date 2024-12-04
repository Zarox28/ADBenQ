import os, subprocess
from datetime import datetime

class Screen:
    def is_display_on(self, device):
        screen_state = device.shell('dumpsys window | grep "mCurrentFocus"').split("=")[1].strip()

        if screen_state != "null": return True
        else: return False

    def toggle_display(self, device, checked):
        if checked:
            device.shell("input keyevent 224")
        else:
            device.shell("input keyevent 223")

    def get_resolution(self, device):
        return device.shell("wm size").strip().split(":")[1]

    def set_resolution(self, device, width, height):
        device.shell(f"wm size {width}x{height}")

    def reset_resolution(self, device):
        device.shell("wm size reset")

    def take_screenshot(self, device):
        screenshot = device.screencap()

        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        current_date_time = datetime.now().strftime("%Y:%m:%d_%H-%M-%S")
        screenshot_path = os.path.join(downloads_path, f"screen_{current_date_time}.png")

        with open(screenshot_path, "wb") as f:
            f.write(screenshot)

        try:
            if os.name == 'posix':
                subprocess.run(['open', screenshot_path], check=True)
            elif os.name == 'nt':
                os.startfile(screenshot_path)
            else:
                subprocess.run(['xdg-open', screenshot_path], check=True)

        except Exception as e:
            print(f"Could not open the screenshot: {e}")

    def __init__(self, ui):
        self.ui = ui
