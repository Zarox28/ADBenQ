# ----- IMPORTS -----
import re


# ----- MEDIA TAB -----
class MediaTab:
    def press_up(self) -> None:
        """
        Press the up button.
        """
        self.connection.connected_device.media.press_up(self.connection.device)

    def press_down(self) -> None:
        """
        Press the down button.
        """
        self.connection.connected_device.media.press_down(self.connection.device)

    def press_left(self) -> None:
        """
        Press the left button.
        """
        self.connection.connected_device.media.press_left(self.connection.device)

    def press_right(self) -> None:
        """
        Press the right button.
        """
        self.connection.connected_device.media.press_right(self.connection.device)

    def press_enter(self) -> None:
        """
        Press the enter button.
        """
        self.connection.connected_device.media.press_enter(self.connection.device)

    def press_back(self) -> None:
        """
        Press the back button.
        """
        self.connection.connected_device.media.press_back(self.connection.device)

    def press_pause(self) -> None:
        """
        Press the pause button.
        """
        self.connection.connected_device.media.press_pause(self.connection.device)

    def open_link(self) -> None:
        """
        Opens a link on the connected device based on the input field value.
        """
        link = self.ui.link_input.text()

        link_pattern = re.compile(r"https?://\S+")

        if not link_pattern.match(link):
            self.parent.log("Please provide a valid link", 0)
            return

        self.connection.connected_device.open_link(self.connection.device, link)
        self.parent.log("Opening link...", 1)

    def __init__(self, parent, ui, connection) -> None:
        """
        Initializes the media tab and sets up the UI and connections.

        Args:
            parent: The parent widget of the media tab.
            ui: The user interface associated with the media tab.
            connection: The connection object.
        """
        self.parent = parent
        self.ui = ui
        self.connection = connection

        # Button connections
        self.ui.up_button.clicked.connect(self.press_up)
        self.ui.down_button.clicked.connect(self.press_down)
        self.ui.left_button.clicked.connect(self.press_left)
        self.ui.right_button.clicked.connect(self.press_right)
        self.ui.enter_button.clicked.connect(self.press_enter)
        self.ui.back_button.clicked.connect(self.press_back)
        self.ui.pause_button.clicked.connect(self.press_pause)
        self.ui.link_button.clicked.connect(self.open_link)
