import subprocess

from ppadb.client import Client as adb
from device import Device

class Connection:
    server = adb(host="127.0.0.1", port=5037)

    device_ip = "127.0.0.1"
    device_port = 5555

    device = None

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
            self.device = self.server.device(f"{self.device_ip}:{self.device_port}")

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

    def __init__(self, ui):
        self.ui = ui

        self.start_server()
        self.connect_device()

        self.connected_device = Device(self.ui)
