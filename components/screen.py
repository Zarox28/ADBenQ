# ---- IMPORTS ----
import os
import subprocess
from datetime import datetime


# ---- SCREEN COMPONENT ----
class Screen:
    def is_display_on(self, device) -> bool:
        """
        Check if the display is currently on.

        Args:
            device: The device to check the display state on.

        Returns:
            bool: True if the display is on, False otherwise.
        """
        screen_state = device.shell('dumpsys window | grep "mCurrentFocus"').split("=")[1].strip()
        return screen_state != "null"

    def toggle_display(self, device, checked: bool) -> None:
        """
        Toggle the display on or off.

        Args:
            device: The device to toggle the display on.
            checked (bool): If True, turn the display on. If False, turn it off.
        """
        if checked:
            device.shell("input keyevent 224")
        else:
            device.shell("input keyevent 223")

    def get_resolution(self, device) -> str:
        """
        Get the current screen resolution.

        Args:
            device: The device to get the resolution from.

        Returns:
            str: The current screen resolution.
        """

        size = device.shell("wm size")
        if (size.splitlines().__len__() > 1):
            return size.splitlines()[1].split(":")[1].strip()
        else:
            return size.split(":")[1].strip()

    def set_resolution(self, device, width: int, height: int) -> None:
        """
        Set the screen resolution.

        Args:
            device: The device to set the resolution on.
            width (int): The width of the resolution.
            height (int): The height of the resolution.
        """
        device.shell(f"wm size {width}x{height}")

    def reset_resolution(self, device) -> None:
        """
        Reset the screen resolution to its default value.

        Args:
            device: The device to reset the resolution on.
        """
        device.shell("wm size reset")

    def take_screenshot(self, device) -> None:
        """
        Take a screenshot of the current screen and save it to the Downloads folder.

        Args:
            device: The device to take the screenshot from.
        """
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

    def __init__(self, ui) -> None:
        """
        Initialize the Screen class.

        Args:
            ui: The user interface associated with the screen.
        """
        self.ui = ui
