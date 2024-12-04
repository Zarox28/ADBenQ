# ----- IMPORTS -----

import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow

# ----- MAIN -----
if __name__ == "__main__":
    """
    Entry point of the application.
    Initializes the QApplication, creates the main window widget,
    shows it, and starts the event loop.
    """
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
