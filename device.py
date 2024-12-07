# ----- IMPORTS -----

from components.battery import Battery
from components.brightness import Brightness
from components.media import Media
from components.screen import Screen
import subprocess


# ----- DEVICE -----
class Device:
    def get_informations(self, device) -> list:
        """
        Retrieve various information about the device.

        Args:
            device: The device object to retrieve information from.

        Returns:
            A list of device information including device name, model,
            build version, and screen size.
        """
        informations = []

        informations.append(device.shell("settings get global device_name").strip())
        informations.append(device.get_properties().get("ro.product.model"))
        informations.append(device.get_properties().get("ro.product.build.version.release"))
        informations.append(self.screen.get_resolution(device))

        return informations

    def open_scrcpy(self, device) -> None:
        """
        Open scrcpy for the given device.

        Args:
            device: The device object to open scrcpy for.
        """
        subprocess.run([
            "scrcpy",
            "-s",
            device.get_serial_no()
        ])

    def open_settings(self, device) -> None:
        """
        Open the settings application on the device.

        Args:
            device: The device object to open settings on.
        """
        device.shell("am start-activity -S com.android.settings/.Settings")

    def open_link(self, device, link: str) -> None:
        """
        Open a link on the device.

        Args:
            device: The device object to open the link on.
            link: The URL link to open.
        """
        device.shell(f"am start {link}")

    def __init__(self, ui):
        """
        Initialize the Device with UI components.

        Args:
            ui: The UI object to interact with.
        """
        self.ui = ui

        self.battery = Battery(self.ui)
        self.brightness = Brightness(self.ui)
        self.media = Media(self.ui)
        self.screen = Screen(self.ui)
