# ----- BATTERY COMPONENT -----
class Battery:
    """
    A class to manage battery operations on a device.
    """

    def __init__(self, ui):
        """
        Initializes the Battery class with a UI component.

        Args:
            ui: The UI object to interact with.
        """
        self.ui = ui

    def get_level(self, device) -> int:
        """
        Retrieves the current battery level of the device.

        Args:
            device: The device to get the battery level from.

        Returns:
            int: The battery level as an integer.
        """
        return device.get_battery_level()

    def set_level(self, device, level: int) -> None:
        """
        Sets the battery level of the device to a specified value.

        Args:
            device: The device to set the battery level on.
            level: The battery level to set as an integer.
        """
        device.shell(f"dumpsys battery set level {level}")

    def reset_level(self, device) -> None:
        """
        Resets the battery level of the device to its default state.

        Args:
            device: The device to reset the battery level on.
        """
        device.shell("cmd battery reset -f")
