from components.battery import Battery
from components.brightness import Brightness
from components.media import Media
from components.screen import Screen

class Device:
    def get_informations(self, device):
        informations = []

        informations.append(device.shell("settings get global device_name").strip())
        informations.append(device.get_properties().get("ro.product.model"))
        informations.append(device.get_properties().get("ro.product.build.version.release"))
        informations.append(device.shell("wm size").strip().split(":")[1])

        return informations

    def open_scrcpy(self, device):
        subprocess.run([
            "scrcpy",
            "-s",
            device.get_serial_no()
        ])

    def open_settings(self, device):
        device.shell("am start-activity -S com.android.settings/.Settings")

    def open_link(self, device, link):
        device.shell(f"am start {link}")

    def __init__(self, ui):
        self.ui = ui

        self.battery = Battery(self.ui)
        self.brightness = Brightness(self.ui)
        self.media = Media(self.ui)
        self.screen = Screen(self.ui)
