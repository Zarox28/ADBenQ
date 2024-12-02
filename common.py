from PySide6.QtCore import QTimer

class Common:
    def __init__(self, ui):
        self.ui = ui

    def display_info(self, text, type):
        self.ui.info_text.setText(f'<span style="color: {"#00b300" if type == 1 else "#ff2600"}">{text}</span>')
        QTimer.singleShot(2000, lambda: self.ui.info_text.clear())
