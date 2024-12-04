class Media:
    def get_volume_level(self, device):
        return int(device.shell("settings get system volume_music_speaker"))

    def set_volume_level(self, device, level):
        device.shell(f"cmd media_session volume --stream 3 --set {int(level)}")

    def __init__(self, ui):
        self.ui = ui
