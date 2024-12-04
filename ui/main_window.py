import re

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer
from ui.ui_form import Ui_ADBenQ
from connection import Connection

class MainWindow(QWidget):
    def log(self, text, type):
            self.ui.log_text.setText(f'<span style="color: {"#00b300" if type == 1 else "#ff2600"}">{text}</span>')
            QTimer.singleShot(2000, lambda: self.ui.log_text.clear())

    def refresh(self):
        self.update_battery()
        self.update_volume()
        self.update_brightness()
        self.update_informations()
        self.update_screen_resolution()
        self.update_display_state()

    def reset_ui(self):
        self.ui.battery_input.clear()
        self.ui.link_input.clear()
        self.ui.width_input.clear()
        self.ui.height_input.clear()

        self.ui.device_name_text.setText("Name:")
        self.ui.device_model_text.setText("Model:")
        self.ui.device_version_text.setText("Android version:")
        self.ui.device_screen_resolution_text.setText("Screen resolution:")

    def update_connection_state(self):
        is_connected = self.connection.connected

        state_color = "#00b300" if is_connected else "#ff2600"
        state_text = "connected" if is_connected else "disconnected"
        self.ui.state_text.setText(f'State: <span style="color: {state_color};">{state_text}</span>')
        self.ui.connect_button.setText("Disconnect" if is_connected else "Connect")

        widgets = [
            self.ui.refresh_button,
            self.ui.screenshot_button,
            self.ui.settings_button,
            self.ui.scrcpy_button,
            self.ui.informations_group,
            self.ui.screen_group,
            self.ui.brightness_slider,
            self.ui.volume_slider,
            self.ui.battery_input,
            self.ui.set_battery_button,
            self.ui.reset_battery_button,
            self.ui.link_button,
            self.ui.link_input
        ]

        for widget in widgets:
            widget.setEnabled(is_connected)

        for i in range(1, self.ui.tabs.count()):
            self.ui.tabs.setTabEnabled(i, is_connected)

        if is_connected:
            self.ui.ip_input.setText(self.connection.device_ip)
            self.refresh()

    def update_display_state(self):
        if self.connection.connected_device.screen.is_display_on(self.connection.device):
            if self.ui.display_checkbox.checkState().Unchecked:
                self.ui.display_checkbox.setChecked(True)
        else:
            if self.ui.display_checkbox.checkState().Checked:
                self.ui.display_checkbox.setChecked(False)

    def update_screen_resolution(self):
        sizes = self.connection.connected_device.screen.get_resolution(self.connection.device)

        self.ui.width_input.setText(sizes.split("x")[0])
        self.ui.height_input.setText(sizes.split("x")[1])

    def update_informations(self):
        informations = self.connection.connected_device.get_informations(self.connection.device)

        self.ui.device_name_text.setText(f"Name: {informations[0]}")
        self.ui.device_model_text.setText(f"Model: {informations[1]}")
        self.ui.device_version_text.setText(f"Android version: {informations[2]}")
        self.ui.device_screen_resolution_text.setText(f"Screen resolution: {informations[3]}")

    def update_battery(self):
        self.ui.battery_input.setText(str(self.connection.connected_device.battery.get_level(self.connection.device)))

    def update_volume(self):
        volume = self.connection.connected_device.media.get_volume_level(self.connection.device)
        self.ui.volume_value_text.setText(f"{str(volume)} %")
        self.ui.volume_slider.setValue(volume)

    def update_brightness(self):
        brightness = self.connection.connected_device.brightness.get_level(self.connection.device)

        self.ui.brightness_value_text.setText(f"{str(brightness)} %")
        self.ui.brightness_slider.setValue(brightness)

    def toggle_display(self):
        self.connection.connected_device.screen.toggle_display(self.connection.device, self.ui.display_checkbox.isChecked())
        self.log(f'Turned screen {"ON" if self.ui.display_checkbox.isChecked() else "OFF"}', 1)

    def set_screen_resolution(self):
        width = self.ui.width_input.text()
        height = self.ui.height_input.text()

        if not width or not height:
            self.log("Please provide valid sizes", 0)
            return

        self.connection.connected_device.screen.set_resolution(self.connection.device, width, height)

    def reset_screen_resolution(self):
        self.connection.connected_device.screen.reset_resolution(self.connection.device)
        self.update_screen_resolution()

    def set_brightness(self):
        brightness = self.ui.brightness_slider.value()

        self.connection.connected_device.brightness.set_level(self.connection.device, brightness)
        self.ui.brightness_value_text.setText(f"{brightness} %")

    def set_volume(self):
        volume = self.ui.volume_slider.value()
        self.connection.connected_device.media.set_volume_level(self.connection.device, volume)
        self.ui.volume_value_text.setText(f"{volume} %")

    def set_battery(self):
        battery = self.ui.battery_input.text()

        if not battery or not battery.isdigit():
            self.log("Please provide a battery value", 0)
            self.ui.battery_input.clear()
            return

        battery = int(battery)

        if battery < 0 or battery > 2147483646:
            self.log("Please provide a valid battery value", 0)
            self.ui.battery_input.clear()
            return

        self.connection.connected_device.battery.set_level(self.connection.device, battery)
        self.log(f"Battery value set to {battery} %", 1)

    def take_screenshot(self):
        self.connection.connected_device.screen.take_screenshot(self.connection.device)
        self.log("Taking screenshot...", 1)

    def reset_battery(self):
        self.connection.connected_device.battery.reset_level(self.connection.device)
        self.update_battery()
        self.log("Battery value reset", 1)

    def open_scrcpy(self):
        self.connection.connected_device.device.open_scrcpy(self.connection.device)
        self.log("Starting SCRCPY...", 1)

    def open_settings(self):
        self.connection.connected_device.open_settings(self.connection.device)
        self.log("Opening settings...", 1)

    def open_link(self):
        link = self.ui.link_input.text()

        link_pattern = re.compile(r'https?://\S+')

        if not link_pattern.match(link):
            self.log("Please provide a valid link", 0)
            return

        self.connection.connected_device.open_link(self.connection.device.link)
        self.log("Opening link...", 1)

    def connect_to_device(self):
        ip_address = self.ui.ip_input.text()

        ip_pattern = re.compile(
            r'^(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$'
        )

        if not ip_address or not ip_pattern.match(ip_address):
            self.log("Invalid IP address entered. Please provide a valid IP.", 0)
            return

        if self.connection.connected:
            self.connection.disconnect_device()
            self.reset_ui()
            self.log("Disconnected from the device.", 1)

        else:
            self.connection.device_ip = ip_address

            if self.connection.connect_device():
                self.refresh()
                self.log(f'Connected to device at IP: {ip_address}', 1)
            else:
                self.log(f'Failed to connect to {ip_address}', 0)

        self.update_connection_state()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ADBenQ()
        self.ui.setupUi(self)

        self.connection = Connection(self.ui)
        self.update_connection_state()

        self.ui.set_battery_button.clicked.connect(self.set_battery)
        self.ui.volume_slider.valueChanged.connect(self.set_volume)
        self.ui.brightness_slider.valueChanged.connect(self.set_brightness)
        self.ui.reset_battery_button.clicked.connect(self.reset_battery)
        self.ui.connect_button.clicked.connect(self.connect_to_device)
        self.ui.set_screen_button.clicked.connect(self.set_screen_resolution)
        self.ui.reset_screen_button.clicked.connect(self.reset_screen_resolution)
        self.ui.display_checkbox.toggled.connect(self.toggle_display)
        self.ui.screenshot_button.clicked.connect(self.take_screenshot)
        self.ui.scrcpy_button.clicked.connect(self.open_scrcpy)
        self.ui.refresh_button.clicked.connect(self.refresh)
        self.ui.settings_button.clicked.connect(self.open_settings)
