# ----- IMPORTS -----
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget

from connection import Connection
from ui.tabs.general import GeneralTab
from ui.tabs.media import MediaTab
from ui.ui_form import Ui_ADBenQ


# ----- MAIN WINDOW -----
class MainWindow(QWidget):
    def log(self, text: str, type: int) -> None:
        """
        Logs a message to the UI log text area with a specific color based on the type.

        Args:
            text: The text to log.
            type: The type of log message. 0 for error, 1 for success.
        """
        if self.log_timer is not None:
            self.log_timer.stop()

        self.ui.log_text.setText(
            f'<span style="color: {"#00b300" if type == 1 else "#ff2600"}">{text}</span>'
        )

        self.log_timer = QTimer()
        self.log_timer.timeout.connect(lambda: self.ui.log_text.clear())
        self.log_timer.setSingleShot(True)
        self.log_timer.start(2000)

    def reset_ui(self) -> None:
        """
        Resets the UI elements to their default state.
        """
        self.ui.battery_input.clear()
        self.ui.link_input.clear()
        self.ui.width_input.clear()
        self.ui.height_input.clear()

        self.ui.device_name_text.setText("Name:")
        self.ui.device_model_text.setText("Model:")
        self.ui.device_version_text.setText("Android version:")
        self.ui.device_screen_resolution_text.setText("Screen resolution:")

        self.ui.brightness_value_text.setText("-- %")
        self.ui.volume_value_text.setText("-- %")

        self.ui.volume_slider_show_checkbox.setChecked(False)

    def refresh(self) -> None:
        """
        Refreshes various UI elements by updating battery, volume, brightness, information,
        screen resolution, and display state.
        """
        self.log("Refreshing...", 1)

        tab = self.ui.tabs.currentWidget().objectName().split("_")[0].lower()

        if tab == "general":
            self.general_tab.update_battery()
            self.general_tab.update_volume()
            self.general_tab.update_brightness()
            self.general_tab.update_informations()
            self.general_tab.update_screen_resolution()
            self.general_tab.update_display_state()

    def __init__(self, parent=None) -> None:
        """
        Initializes the main window and sets up the UI and connections.
        """
        super().__init__(parent)
        self.ui = Ui_ADBenQ()
        self.ui.setupUi(self)

        # Set up log timer
        self.log_timer = None

        # Set up connection
        self.connection = Connection(self.ui)

        # Set up tabs
        self.general_tab = GeneralTab(self, self.ui, self.connection)
        self.general_tab.update_connection_state()

        self.media_tab = MediaTab(self, self.ui, self.connection)

        # Connect the refresh button to the refresh method
        self.ui.refresh_button.clicked.connect(self.refresh)
