import subprocess, os

from ppadb.client import Client as adb
from datetime import datetime
from math import floor

class Connection:
    server = adb(host="127.0.0.1", port=5037)

    device_ip = "127.0.0.1"
    device_port = 5555

    connected = False

    def start_server(self):
        subprocess.run(["adb", "start-server"])

    def get_connected_device(self):
        devices = self.server.devices()

        if devices:
            return devices[0].serial
        else:
            return None

    def connect_device(self):
        device = self.get_connected_device()

        if device:
            self.device_ip = device.split(":")[0]
            self.device_port = device.split(":")[1]

        self.server.remote_connect(self.device_ip, int(self.device_port))
        if self.server.device(f"{self.device_ip}:{self.device_port}") is not None:
            self.connected = True
        else:
            self.connected = False
            return False

        return True

    def disconnect_device(self):
        self.server.remote_disconnect(self.device_ip, int(self.device_port))
        self.connected = False

    def open_scrcpy(self):
        subprocess.run([
            "scrcpy",
            "-s",
            self.server.device(f"{self.device_ip}:{self.device_port}").get_serial_no()
        ])

    def open_settings(self):
        self.server.device(f"{self.device_ip}:{self.device_port}").shell("am start-activity -S com.android.settings/.Settings")

    def take_screenshot(self):
        device = self.server.device(f"{self.device_ip}:{self.device_port}")
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

    def open_link(self, link):
        self.server.device(f"{self.device_ip}:{self.device_port}").shell(f"am start {link}")

    def is_display_on(self):
        device = self.server.device(f"{self.device_ip}:{self.device_port}")
        screen_state = device.shell('dumpsys window | grep "mCurrentFocus"').split("=")[1].strip()

        if screen_state != "null": return True
        else: return False

    def switch_display(self, checked):
        device = self.server.device(f"{self.device_ip}:{self.device_port}")

        if checked:
            device.shell("input keyevent 224")
        else:
            device.shell("input keyevent 223")


    def get_informations(self):
        informations = []

        device = self.server.device(f"{self.device_ip}:{self.device_port}")

        informations.append(device.shell("settings get global device_name").strip())
        informations.append(device.get_properties().get("ro.product.model"))
        informations.append(device.get_properties().get("ro.product.build.version.release"))
        informations.append(device.shell("wm size").strip().split(":")[1])

        return informations

    def get_screen_sizes(self):
        device = self.server.device(f"{self.device_ip}:{self.device_port}")

        return device.shell("wm size").strip().split(":")[1]

    def set_screen_resolution(self, width, height):
        device = self.server.device(f"{self.device_ip}:{self.device_port}")

        device.shell(f"wm size {width}x{height}")

    def reset_screen_resolution(self):
        device = self.server.device(f"{self.device_ip}:{self.device_port}")

        device.shell("wm size reset")

    def get_battery_level(self):
        device = self.server.device(f"{self.device_ip}:{self.device_port}")

        return device.get_battery_level()

    def set_battery_level(self, level):
        device = self.server.device(f"{self.device_ip}:{self.device_port}")
        device.shell(f"dumpsys battery set level {level}")

    def reset_battery_level(self):
        device = self.server.device(f"{self.device_ip}:{self.device_port}")
        device.shell("cmd battery reset -f")

    def get_brightness_level(self):
        device = self.server.device(f"{self.device_ip}:{self.device_port}")

        brightness_value = int(device.shell("settings get system screen_brightness").strip()) / 255

        return floor(1*(1-brightness_value) + 100 * brightness_value)

    def set_brightness_level(self, level):
        self.server.device(f"{self.device_ip}:{self.device_port}").shell(f"settings put system screen_brightness {int(level)}")

    def get_volume_level(self):
        device = self.server.device(f"{self.device_ip}:{self.device_port}")

        return int(device.shell("settings get system volume_music_speaker"))

    def set_volume_level(self, level):
        self.server.device(f"{self.device_ip}:{self.device_port}").shell(f"cmd media_session volume --stream 3 --set {int(level)}")

    def __init__(self, ui):
        self.ui = ui

        self.start_server()

        connected_device = self.get_connected_device()

        if connected_device: self.connect_device()
