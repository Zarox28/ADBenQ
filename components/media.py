# ---- MEDIA COMPONENT ----
class Media:
    def get_volume_level(self, device) -> int:
        """
        Get the current volume level of the device.

        Args:
            device: The device from which to get the volume level.

        Returns:
            The current volume level as an integer.
        """
        return int(device.shell("settings get system volume_music_speaker"))

    def set_volume_level(self, device, level: int, show_slider: bool) -> None:
        """
        Set the volume level of the device.

        Args:
            device: The device on which to set the volume level.
            level: The volume level to set as an integer.
            show_slider: Whether to show the volume slider on the screen.
        """
        device.shell(
            f"cmd media_session volume --stream 3 --set {int(level)} {'--show' if show_slider else ''}"
        )

    def press_up(self, device) -> None:
        """
        Press the up button.

        Args:
            device: The device on which to press the up button.
        """
        device.shell("input keyevent 19")

    def press_down(self, device) -> None:
        """
        Press the down button.

        Args:
            device: The device on which to press the down button.
        """
        device.shell("input keyevent 20")

    def press_left(self, device) -> None:
        """
        Press the left button.

        Args:
            device: The device on which to press the left button.
        """
        device.shell("input keyevent 21")

    def press_right(self, device) -> None:
        """
        Press the right button.

        Args:
            device: The device on which to press the right button.
        """
        device.shell("input keyevent 22")

    def press_enter(self, device) -> None:
        """
        Press the enter button.

        Args:
            device: The device on which to press the enter button
        """
        device.shell("input keyevent 66")

    def press_back(self, device) -> None:
        """
        Press the back button.

        Args:
            device: The device on which to press the back button.
        """
        device.shell("input keyevent 4")

    def press_pause(self, device) -> None:
        """
        Press the pause button.

        Args:
            device: The device on which to press the pause button.
        """
        device.shell("input keyevent 85")

    def __init__(self, ui) -> None:
        """
        Initialize the Media class.

        Args:
            ui: The user interface associated with the media component.
        """
        self.ui = ui
