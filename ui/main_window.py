import sys, re

from PySide6.QtWidgets import QApplication, QWidget, QStyleFactory

from ui.ui_form import Ui_ADBenQ

from common import Common
from connection import Connection

class MainWindow(QWidget):
    def update_connection_state(self):
        if self.connection.connected:
            self.ui.state_text.setText('State: <span style="color: #00b300;">connected</span>')
            self.ui.connect_button.setText("Disconnect");
        else:
            self.ui.state_text.setText('State: <span style="color: #ff2600;">disconnected</span>')
            self.ui.connect_button.setText("Connect");

        for i in range(1, 5) :
            self.ui.tabs.setTabEnabled(i, self.connection.connected)

        self.ui.refresh_button.setEnabled(self.connection.connected)
        self.ui.screenshot_button.setEnabled(self.connection.connected)
        self.ui.settings_button.setEnabled(self.connection.connected)
        self.ui.scrcpy_button.setEnabled(self.connection.connected)
        self.ui.informations_group.setEnabled(self.connection.connected)
        self.ui.screen_group.setEnabled(self.connection.connected)
        self.ui.brightness_slider.setEnabled(self.connection.connected)
        self.ui.volume_slider.setEnabled(self.connection.connected)
        self.ui.battery_input.setEnabled(self.connection.connected)
        self.ui.battery_button.setEnabled(self.connection.connected)
        self.ui.reset_battery_button.setEnabled(self.connection.connected)
        self.ui.link_button.setEnabled(self.connection.connected)
        self.ui.link_input.setEnabled(self.connection.connected)

    def update_informations(self):
        self.ui.device_name_text.setText(f"Name: {self.connection.get_informations()[0]}")
        self.ui.device_model_text.setText(f"Model: {self.connection.get_informations()[1]}")
        self.ui.device_version_text.setText(f"Android version: {self.connection.get_informations()[2]}")
        self.ui.device_screen_text.setText(f"Screen resolution: {self.connection.get_informations()[3]}")

    def update_display_state(self):
        if self.connection.is_display_on():
            if self.ui.display_checkbox.checkState().Unchecked:
                self.ui.display_checkbox.setChecked(True)
        else:
            if self.ui.display_checkbox.checkState().Checked:
                self.ui.display_checkbox.setChecked(False)

    def update_battery(self):
        self.ui.battery_input.setText(str(self.connection.get_battery_level()))

    def set_battery_button(self):
        battery = self.ui.battery_input.text()

        if not battery or not battery.isdigit():
            self.common.display_info("Please provide a battery value", 0)
            self.ui.battery_input.clear()
            return

        battery = int(battery)

        if battery < 0 or battery > 2147483646:
            self.common.display_info("Please provide a valid battery value", 0)
            self.ui.battery_input.clear()
            return

        self.connection.set_battery_level(battery)
        self.common.display_info(f"Battery value set to {battery} %", 1)

    def reset_battery_button(self):
        self.connection.reset_battery_level()
        self.update_battery()
        self.common.display_info("Battery value reset", 1)

    def update_brightness(self):
        brightness = self.connection.get_brightness_level()
        self.ui.brightness_value.setText(f"{str(brightness)} %")
        self.ui.brightness_slider.setValue(brightness)

    def set_brightness_slider(self):
        brightness = self.ui.brightness_slider.value()
        self.connection.set_brightness_level(brightness)
        self.ui.brightness_value.setText(f"{brightness} %")

    def update_volume(self):
        volume = self.connection.get_volume_level()
        self.ui.volume_value.setText(f"{str(volume)} %")
        self.ui.volume_slider.setValue(volume)

    def set_volume_slider(self):
        volume = self.ui.volume_slider.value()
        self.connection.set_volume_level(volume)
        self.ui.volume_value.setText(f"{volume} %")

    def reset_ui(self):
        self.ui.battery_input.clear()
        self.ui.link_input.clear()
        self.ui.width_input.clear()
        self.ui.height_input.clear()

        self.ui.device_name_text.setText("Name:")
        self.ui.device_model_text.setText("Model:")
        self.ui.device_version_text.setText("Android version:")
        self.ui.device_screen_text.setText("Screen resolution:")

    def connect_to_device_button(self):
        ip_address = self.ui.ip_input.text()

        ip_pattern = re.compile(
            r'^(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$'
        )

        if not ip_address or not ip_pattern.match(ip_address):
            self.common.display_info("Invalid IP address entered. Please provide a valid IP.", 0)
            return

        if self.connection.connected:
            self.connection.disconnect_device()
            self.reset_ui()
            self.common.display_info("Disconnected from the device.", 1)
        else:
            self.connection.device_ip = ip_address

            if self.connection.connect_device():
                self.update_informations()
                self.update_battery()
                self.update_display_state()
                self.update_screen_resolution()
                self.common.display_info(f'Connected to device at IP: {ip_address}', 1)
            else:
                self.common.display_info(f'Failed to connect to {ip_address}', 0)

        self.update_connection_state()

    def open_scrcpy_button(self):
        self.connection.open_scrcpy()
        self.common.display_info("Starting SCRCPY...", 1)

    def open_settings_button(self):
        self.connection.open_settings()
        self.common.display_info("Opening settings...", 1)

    def screenshot_button(self):
        self.connection.take_screenshot()
        self.common.display_info("Taking screenshot...", 1)

    def open_link_button(self):
        link =  self.ui.link_input.text()

        link_pattern = re.compile(r'https?://\S+')

        if not link_pattern.match(link):
            self.common.display_info("Please provide a valid link", 0)
            return

        self.connection.open_link(link)
        self.common.display_info("Opening link...", 1)

    def refresh(self):
        self.update_informations()
        self.update_battery()
        self.update_display_state()
        self.update_brightness()
        self.update_volume()
        self.update_screen_resolution()
        self.common.display_info("Refreshing...", 1)

    def switch_display_button(self):
        self.connection.switch_display(self.ui.display_checkbox.isChecked())
        self.common.display_info(f'Turned screen {"ON" if self.ui.display_checkbox.isChecked() else "OFF"}', 1)

    def update_screen_resolution(self):
        sizes = self.connection.get_screen_sizes()

        self.ui.width_input.setText(sizes.split("x")[0])
        self.ui.height_input.setText(sizes.split("x")[1])

    def set_screen_resolution_button(self):
        width = self.ui.width_input.text()
        height = self.ui.height_input.text()

        if not width or not height:
            self.common.display_info("Please provide valid sizes", 0)
            return

        self.connection.set_screen_resolution(width, height)

    def reset_screen_resolution_button(self):
        self.connection.reset_screen_resolution()
        self.update_screen_resolution()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ADBenQ()
        self.ui.setupUi(self)

        self.common = Common(self.ui)

        self.connection = Connection(self.ui)
        self.update_connection_state()

        if self.connection.connected:
            self.ui.ip_input.setText(self.connection.device_ip)
            self.update_informations()
            self.update_battery()
            self.update_display_state()
            self.update_brightness()
            self.update_volume()
            self.update_screen_resolution()

        self.ui.display_checkbox.toggled.connect(self.switch_display_button)

        self.ui.brightness_slider.valueChanged.connect(self.set_brightness_slider)
        self.ui.volume_slider.valueChanged.connect(self.set_volume_slider)

        self.ui.connect_button.clicked.connect(self.connect_to_device_button)
        self.ui.scrcpy_button.clicked.connect(self.open_scrcpy_button)
        self.ui.refresh_button.clicked.connect(self.refresh)
        self.ui.settings_button.clicked.connect(self.open_settings_button)
        self.ui.screenshot_button.clicked.connect(self.screenshot_button)
        self.ui.screen_button.clicked.connect(self.set_screen_resolution_button)
        self.ui.battery_button.clicked.connect(self.set_battery_button)
        self.ui.reset_battery_button.clicked.connect(self.reset_battery_button)
        self.ui.link_button.clicked.connect(self.open_link_button)
        self.ui.screen_button.clicked.connect(self.set_screen_resolution_button)
        self.ui.reset_screen_button.clicked.connect(self.reset_screen_resolution_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyle(QStyleFactory.create("Fusion"))
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
