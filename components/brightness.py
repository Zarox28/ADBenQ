# ----- IMPORTS -----
from math import floor


# ----- BRIGHTNESS COMPONENT -----
class Brightness:
    def get_level(self, device) -> int:
        """
        Get the current brightness level of the device.

        Args:
            device: The device from which to get the brightness level.

        Returns:
            The brightness level as an integer.
        """
        brightness_value = (
            int(device.shell("settings get system screen_brightness").strip()) / 255
        )
        return floor(1 * (1 - brightness_value) + 100 * brightness_value)

    def set_level(self, device, level: int) -> None:
        """
        Set the brightness level of the device.

        Args:
            device: The device on which to set the brightness level.
            level: The brightness level to set as an integer.
        """
        device.shell(f"settings put system screen_brightness {int(level)}")

    def __init__(self, ui) -> None:
        """
        Initialize the Brightness component.

        Args:
            ui: The user interface associated with the brightness component.
        """
        self.ui = ui
