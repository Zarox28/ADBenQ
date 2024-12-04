class Battery:
    def get_level(self, device):
        return device.get_battery_level()

    def set_level(self, device, level):
        device.shell(f"dumpsys battery set level {level}")

    def reset_level(self, device):
        device.shell("cmd battery reset -f")

    def __init__(self, ui):
        self.ui = ui
