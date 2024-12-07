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

    def set_volume_level(self, device, level: int) -> None:
        """
        Set the volume level of the device.

        Args:
            device: The device on which to set the volume level.
            level: The volume level to set as an integer.
        """
        device.shell(f"cmd media_session volume --stream 3 --set {int(level)}")

    def __init__(self, ui) -> None:
        """
        Initialize the Media class.

        Args:
            ui: The user interface associated with the media component.
        """
        self.ui = ui
