# ----- IMPORTS -----

import subprocess
from ppadb.client import Client as adb
from device import Device


# ----- CONNECTION -----
class Connection:
    server = adb(host="127.0.0.1", port=5037)

    device_ip: str = "127.0.0.1"
    device_port: int = 5555

    device = None
    connected: bool = False

    def start_server(self) -> None:
        """
        Starts the ADB server.
        """
        subprocess.run(["adb", "start-server"])

    def get_connected_device(self) -> str:
        """
        Retrieves the serial number of the first connected device.

        Returns:
            str: The serial number of the connected device, or None if no devices are connected.
        """
        devices = self.server.devices()

        if devices:
            return devices[0].serial
        else:
            return None

    def connect_device(self) -> bool:
        """
        Connects to the device using the IP and port.

        Returns:
            bool: True if the device is successfully connected, False otherwise.
        """
        device = self.get_connected_device()

        if device:
            self.device_ip = device.split(":")[0]
            self.device_port = int(device.split(":")[1])
            self.device = self.server.device(f"{self.device_ip}:{self.device_port}")

        self.server.remote_connect(self.device_ip, self.device_port)

        if self.server.device(f"{self.device_ip}:{self.device_port}") is not None:
            self.connected = True
        else:
            self.connected = False
            return False

        return True

    def disconnect_device(self) -> None:
        """
        Disconnects the device.
        """
        self.server.remote_disconnect(self.device_ip, self.device_port)
        self.connected = False

    def __init__(self, ui):
        """
        Initializes the Connection class, starts the ADB server, and connects to the device.

        Args:
            ui: The user interface instance.
        """
        self.ui = ui

        self.start_server()
        self.connect_device()

        self.connected_device = Device(self.ui)
