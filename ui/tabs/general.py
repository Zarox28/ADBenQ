# ----- IMPORTS -----
import socket


# ----- GENERAL TAB -----
class GeneralTab:
    def update_connection_state(self) -> None:
        """
        Updates the connection state UI elements based on the current connection status.
        """
        is_connected = self.connection.connected

        state_color = "#00b300" if is_connected else "#ff2600"
        state_text = "connected" if is_connected else "disconnected"
        self.ui.state_text.setText(
            f'State: <span style="color: {state_color};">{state_text}</span>'
        )
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
            self.ui.volume_slider_show_checkbox,
            self.ui.battery_input,
            self.ui.set_battery_button,
            self.ui.reset_battery_button,
            self.ui.turn_off_button,
            self.ui.reboot_button,
        ]

        for widget in widgets:
            widget.setEnabled(is_connected)

        for i in range(1, self.ui.tabs.count()):
            self.ui.tabs.setTabEnabled(i, is_connected)

        if is_connected:
            self.ui.ip_input.setText(self.connection.device_ip)
            self.parent.refresh()

    def update_display_state(self) -> None:
        """
        Updates the display state checkbox based on the current display state of the connected device.
        """
        if self.connection.connected_device.screen.is_display_on(
            self.connection.device
        ):
            if self.ui.display_checkbox.checkState().Unchecked:
                self.ui.display_checkbox.setChecked(True)
        else:
            if self.ui.display_checkbox.checkState().Checked:
                self.ui.display_checkbox.setChecked(False)

    def update_screen_resolution(self) -> None:
        """
        Updates the screen resolution inputs based on the current resolution of the connected device.
        """
        sizes = self.connection.connected_device.screen.get_resolution(
            self.connection.device
        )

        self.ui.width_input.setText(sizes.split("x")[0])
        self.ui.height_input.setText(sizes.split("x")[1])

    def update_informations(self) -> None:
        """
        Updates the device information text fields based on the current information of the connected device.
        """
        informations = self.connection.connected_device.get_informations(
            self.connection.device
        )

        self.ui.device_name_text.setText(f"Name: {informations[0]}")
        self.ui.device_model_text.setText(f"Model: {informations[1]}")
        self.ui.device_version_text.setText(f"Android version: {informations[2]}")
        self.ui.device_screen_resolution_text.setText(
            f"Screen resolution: {informations[3]}"
        )

    def update_battery(self) -> None:
        """
        Updates the battery input field based on the current battery level of the connected device.
        """
        self.ui.battery_input.setText(
            str(
                self.connection.connected_device.battery.get_level(
                    self.connection.device
                )
            )
        )

    def update_volume(self) -> None:
        """
        Updates the volume slider and text based on the current volume level of the connected device.
        """
        volume = self.connection.connected_device.media.get_volume_level(
            self.connection.device
        )
        self.ui.volume_value_text.setText(f"{str(volume)} %")
        self.ui.volume_slider.setValue(volume)

    def update_brightness(self) -> None:
        """
        Updates the brightness slider and text based on the current brightness level of the connected device.
        """
        brightness = self.connection.connected_device.brightness.get_level(
            self.connection.device
        )

        self.ui.brightness_value_text.setText(f"{str(brightness)} %")
        self.ui.brightness_slider.setValue(brightness)

    def toggle_display(self) -> None:
        """
        Toggles the display state of the connected device based on the checkbox state.
        """
        self.connection.connected_device.screen.toggle_display(
            self.connection.device, self.ui.display_checkbox.isChecked()
        )
        self.parent.log(
            f'Turned screen {"ON" if self.ui.display_checkbox.isChecked() else "OFF"}',
            1,
        )

    def set_screen_resolution(self) -> None:
        """
        Sets the screen resolution of the connected device based on the input fields.
        """
        width = int(self.ui.width_input.text())
        height = int(self.ui.height_input.text())

        if not width or not height:
            self.parent.log("Please provide valid sizes", 0)
            return

        self.connection.connected_device.screen.set_resolution(
            self.connection.device, width, height
        )
        self.parent.log(f"Screen resolution set to {width}x{height}", 1)
        self.update_informations()

    def reset_screen_resolution(self) -> None:
        """
        Resets the screen resolution of the connected device to its default value.
        """
        self.connection.connected_device.screen.reset_resolution(self.connection.device)
        self.parent.log("Screen resolution reset", 1)
        self.update_screen_resolution()
        self.update_informations()

    def set_brightness(self) -> None:
        """
        Sets the brightness level of the connected device based on the slider value.
        """
        brightness = self.ui.brightness_slider.value()

        self.connection.connected_device.brightness.set_level(
            self.connection.device, brightness
        )
        self.ui.brightness_value_text.setText(f"{brightness} %")

    def set_volume(self) -> None:
        """
        Sets the volume level of the connected device based on the slider value.
        """
        volume = self.ui.volume_slider.value()
        show = self.ui.volume_slider_show_checkbox.isChecked()

        self.connection.connected_device.media.set_volume_level(
            self.connection.device, volume, show
        )
        self.ui.volume_value_text.setText(f"{volume} %")

    def set_battery(self) -> None:
        """
        Sets the battery level of the connected device based on the input field value.
        """
        battery = self.ui.battery_input.text()

        if not battery or not battery.isdigit():
            self.parent.log("Please provide a battery value", 0)
            self.ui.battery_input.clear()
            return

        battery = int(battery)

        if battery < 0 or battery > 2147483646:
            self.parent.log("Please provide a valid battery value", 0)
            self.ui.battery_input.clear()
            return

        self.connection.connected_device.battery.set_level(
            self.connection.device, battery
        )
        self.parent.log(f"Battery value set to {battery} %", 1)

    def take_screenshot(self) -> None:
        """
        Takes a screenshot of the connected device.
        """
        self.connection.connected_device.screen.take_screenshot(self.connection.device)
        self.parent.log("Taking screenshot...", 1)

    def reset_battery(self) -> None:
        """
        Resets the battery level of the connected device to its default value.
        """
        self.connection.connected_device.battery.reset_level(self.connection.device)
        self.update_battery()
        self.parent.log("Battery value reset", 1)

    def open_scrcpy(self) -> None:
        """
        Opens the SCRCPY application for the connected device.
        """
        if self.connection.connected_device.open_scrcpy(self.connection.device):
            self.parent.log("Starting SCRCPY...", 1)
        else:
            self.parent.log("SCRCPY is already running", 0)

    def open_settings(self) -> None:
        """
        Opens the settings application on the connected device.
        """
        self.connection.connected_device.open_settings(self.connection.device)
        self.parent.log("Opening settings...", 1)

    def turn_off(self) -> None:
        """
        Turns off the connected device.
        """
        self.connection.connected_device.turn_off(self.connection.device)

        self.connection.disconnect_device()
        self.parent.reset_ui()

        self.parent.log("Turning off device...", 1)

    def reboot(self) -> None:
        """
        Reboots the connected device.
        """
        self.connection.connected_device.reboot(self.connection.device)

        self.connection.disconnect_device()
        self.parent.reset_ui()

        self.parent.log("Rebooting device...", 1)

    def connect_to_device(self) -> None:
        """
        Connects to a device using the IP address provided in the input field.
        """
        ip_address = self.ui.ip_input.text()

        if not ip_address:
            self.parent.log(
                "Invalid address entered. Please provide a valid address.", 0
            )
            return

        if self.connection.connected:
            self.connection.disconnect_device()
            self.parent.reset_ui()
            self.parent.log("Disconnected from the device.", 1)

        else:
            if self.connection.connect_device(
                socket.gethostbyname(ip_address) if ip_address else ""
            ):
                self.parent.refresh()
                self.parent.log(f"Connected to device at IP: {ip_address}", 1)
            else:
                self.parent.log(f"Failed to connect to {ip_address}", 0)

        self.update_connection_state()

    def __init__(self, parent, ui, connection) -> None:
        """
        Initializes the GeneralTab class.

        Args:
            parent: The parent widget of the tab.
            ui: The user interface associated with the tab.
        """
        self.parent = parent
        self.ui = ui
        self.connection = connection

        # Button connections
        self.ui.set_battery_button.clicked.connect(self.set_battery)
        self.ui.reset_battery_button.clicked.connect(self.reset_battery)
        self.ui.connect_button.clicked.connect(self.connect_to_device)
        self.ui.set_screen_button.clicked.connect(self.set_screen_resolution)
        self.ui.reset_screen_button.clicked.connect(self.reset_screen_resolution)
        self.ui.screenshot_button.clicked.connect(self.take_screenshot)
        self.ui.scrcpy_button.clicked.connect(self.open_scrcpy)
        self.ui.settings_button.clicked.connect(self.open_settings)
        self.ui.turn_off_button.clicked.connect(self.turn_off)
        self.ui.reboot_button.clicked.connect(self.reboot)

        # Slider connections
        self.ui.volume_slider.valueChanged.connect(self.set_volume)
        self.ui.brightness_slider.valueChanged.connect(self.set_brightness)

        # Checkbox connections
        self.ui.display_checkbox.toggled.connect(self.toggle_display)
