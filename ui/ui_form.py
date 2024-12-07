# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Ui_ADBenQ(object):
    def setupUi(self, ADBenQ):
        if not ADBenQ.objectName():
            ADBenQ.setObjectName("ADBenQ")
        ADBenQ.setEnabled(True)
        ADBenQ.resize(682, 484)
        ADBenQ.setMinimumSize(QSize(540, 0))
        icon = QIcon()
        icon.addFile("src/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ADBenQ.setWindowIcon(icon)
        self.gridLayout = QGridLayout(ADBenQ)
        self.gridLayout.setObjectName("gridLayout")
        self.state_container = QHBoxLayout()
        self.state_container.setObjectName("state_container")
        self.state_text = QLabel(ADBenQ)
        self.state_text.setObjectName("state_text")

        self.state_container.addWidget(self.state_text)

        self.horizontal_spacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.state_container.addItem(self.horizontal_spacer)

        self.log_text = QLabel(ADBenQ)
        self.log_text.setObjectName("log_text")

        self.state_container.addWidget(self.log_text)

        self.gridLayout.addLayout(self.state_container, 1, 0, 1, 1)

        self.tabs = QTabWidget(ADBenQ)
        self.tabs.setObjectName("tabs")
        self.tabs.setEnabled(True)
        self.general_tab = QWidget()
        self.general_tab.setObjectName("general_tab")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_tab.sizePolicy().hasHeightForWidth())
        self.general_tab.setSizePolicy(sizePolicy)
        self.general_tab.setMinimumSize(QSize(0, 0))
        self.gridLayout_3 = QGridLayout(self.general_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, -1, 10, 10)
        self.general_container = QVBoxLayout()
        self.general_container.setObjectName("general_container")
        self.header_container = QHBoxLayout()
        self.header_container.setObjectName("header_container")
        self.scrcpy_button = QPushButton(self.general_tab)
        self.scrcpy_button.setObjectName("scrcpy_button")

        self.header_container.addWidget(self.scrcpy_button)

        self.settings_button = QPushButton(self.general_tab)
        self.settings_button.setObjectName("settings_button")
        self.settings_button.setEnabled(True)

        self.header_container.addWidget(self.settings_button)

        self.screenshot_button = QPushButton(self.general_tab)
        self.screenshot_button.setObjectName("screenshot_button")
        self.screenshot_button.setMinimumSize(QSize(0, 0))

        self.header_container.addWidget(self.screenshot_button)

        self.refresh_button = QPushButton(self.general_tab)
        self.refresh_button.setObjectName("refresh_button")

        self.header_container.addWidget(self.refresh_button)

        self.ip_input = QLineEdit(self.general_tab)
        self.ip_input.setObjectName("ip_input")
        self.ip_input.setMinimumSize(QSize(0, 0))
        self.ip_input.setMaximumSize(QSize(110, 16777215))
        self.ip_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.ip_input.setMaxLength(15)
        self.ip_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.header_container.addWidget(self.ip_input)

        self.connect_button = QPushButton(self.general_tab)
        self.connect_button.setObjectName("connect_button")
        self.connect_button.setMinimumSize(QSize(78, 0))

        self.header_container.addWidget(self.connect_button)

        self.general_container.addLayout(self.header_container)

        self.vertical_spacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.general_container.addItem(self.vertical_spacer)

        self.main_container = QHBoxLayout()
        self.main_container.setObjectName("main_container")
        self.informations_group = QGroupBox(self.general_tab)
        self.informations_group.setObjectName("informations_group")
        self.informations_group.setEnabled(True)
        self.informations_group.setMinimumSize(QSize(250, 0))
        self.verticalLayout_3 = QVBoxLayout(self.informations_group)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.device_name_text = QLabel(self.informations_group)
        self.device_name_text.setObjectName("device_name_text")

        self.verticalLayout_3.addWidget(self.device_name_text)

        self.device_model_text = QLabel(self.informations_group)
        self.device_model_text.setObjectName("device_model_text")

        self.verticalLayout_3.addWidget(self.device_model_text)

        self.device_version_text = QLabel(self.informations_group)
        self.device_version_text.setObjectName("device_version_text")

        self.verticalLayout_3.addWidget(self.device_version_text)

        self.device_screen_resolution_text = QLabel(self.informations_group)
        self.device_screen_resolution_text.setObjectName(
            "device_screen_resolution_text"
        )

        self.verticalLayout_3.addWidget(self.device_screen_resolution_text)

        self.main_container.addWidget(self.informations_group)

        self.horizontal_spacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.main_container.addItem(self.horizontal_spacer_4)

        self.screen_group = QGroupBox(self.general_tab)
        self.screen_group.setObjectName("screen_group")
        self.screen_group.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.screen_group.setFlat(False)
        self.screen_layout = QVBoxLayout(self.screen_group)
        self.screen_layout.setSpacing(0)
        self.screen_layout.setObjectName("screen_layout")
        self.display_checkbox = QCheckBox(self.screen_group)
        self.display_checkbox.setObjectName("display_checkbox")
        self.display_checkbox.setChecked(False)

        self.screen_layout.addWidget(self.display_checkbox)

        self.vertical_spacer_5 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.screen_layout.addItem(self.vertical_spacer_5)

        self.screen_inputs_container = QHBoxLayout()
        self.screen_inputs_container.setSpacing(10)
        self.screen_inputs_container.setObjectName("screen_inputs_container")
        self.screen_inputs_container.setSizeConstraint(
            QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.screen_inputs_container.setContentsMargins(-1, 0, -1, -1)
        self.width_input = QLineEdit(self.screen_group)
        self.width_input.setObjectName("width_input")
        self.width_input.setMaximumSize(QSize(100, 16777215))
        self.width_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.width_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.screen_inputs_container.addWidget(self.width_input)

        self.height_input = QLineEdit(self.screen_group)
        self.height_input.setObjectName("height_input")
        self.height_input.setMaximumSize(QSize(100, 16777215))
        self.height_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.height_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.screen_inputs_container.addWidget(self.height_input)

        self.screen_layout.addLayout(self.screen_inputs_container)

        self.screen_button_container = QHBoxLayout()
        self.screen_button_container.setSpacing(10)
        self.screen_button_container.setObjectName("screen_button_container")
        self.screen_button_container.setContentsMargins(-1, 10, -1, 0)
        self.horizontal_spacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.screen_button_container.addItem(self.horizontal_spacer_5)

        self.set_screen_button = QPushButton(self.screen_group)
        self.set_screen_button.setObjectName("set_screen_button")

        self.screen_button_container.addWidget(self.set_screen_button)

        self.reset_screen_button = QPushButton(self.screen_group)
        self.reset_screen_button.setObjectName("reset_screen_button")

        self.screen_button_container.addWidget(self.reset_screen_button)

        self.screen_layout.addLayout(self.screen_button_container)

        self.main_container.addWidget(self.screen_group)

        self.general_container.addLayout(self.main_container)

        self.vertical_spacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.general_container.addItem(self.vertical_spacer_2)

        self.footer_container = QHBoxLayout()
        self.footer_container.setObjectName("footer_container")
        self.footer_left_container = QVBoxLayout()
        self.footer_left_container.setObjectName("footer_left_container")
        self.battery_container = QHBoxLayout()
        self.battery_container.setObjectName("battery_container")
        self.battery_container.setContentsMargins(-1, 0, -1, -1)
        self.battery_input = QLineEdit(self.general_tab)
        self.battery_input.setObjectName("battery_input")
        self.battery_input.setMinimumSize(QSize(100, 0))
        self.battery_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.battery_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.battery_container.addWidget(self.battery_input)

        self.set_battery_button = QPushButton(self.general_tab)
        self.set_battery_button.setObjectName("set_battery_button")

        self.battery_container.addWidget(self.set_battery_button)

        self.reset_battery_button = QPushButton(self.general_tab)
        self.reset_battery_button.setObjectName("reset_battery_button")

        self.battery_container.addWidget(self.reset_battery_button)

        self.footer_left_container.addLayout(self.battery_container)

        self.link_container = QHBoxLayout()
        self.link_container.setObjectName("link_container")
        self.link_input = QLineEdit(self.general_tab)
        self.link_input.setObjectName("link_input")
        self.link_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.link_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.link_container.addWidget(self.link_input)

        self.link_button = QPushButton(self.general_tab)
        self.link_button.setObjectName("link_button")
        self.link_button.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.link_container.addWidget(self.link_button)

        self.footer_left_container.addLayout(self.link_container)

        self.footer_container.addLayout(self.footer_left_container)

        self.horizontal_spacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.footer_container.addItem(self.horizontal_spacer_6)

        self.sliders_container = QVBoxLayout()
        self.sliders_container.setObjectName("sliders_container")
        self.brightness_container = QVBoxLayout()
        self.brightness_container.setObjectName("brightness_container")
        self.brightness_label = QLabel(self.general_tab)
        self.brightness_label.setObjectName("brightness_label")

        self.brightness_container.addWidget(self.brightness_label)

        self.brightness_slider_container = QHBoxLayout()
        self.brightness_slider_container.setObjectName("brightness_slider_container")
        self.brightness_slider = QSlider(self.general_tab)
        self.brightness_slider.setObjectName("brightness_slider")
        self.brightness_slider.setMinimumSize(QSize(150, 0))
        self.brightness_slider.setMinimum(1)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setOrientation(Qt.Orientation.Horizontal)

        self.brightness_slider_container.addWidget(self.brightness_slider)

        self.brightness_value_text = QLabel(self.general_tab)
        self.brightness_value_text.setObjectName("brightness_value_text")
        self.brightness_value_text.setMinimumSize(QSize(38, 0))

        self.brightness_slider_container.addWidget(self.brightness_value_text)

        self.brightness_container.addLayout(self.brightness_slider_container)

        self.sliders_container.addLayout(self.brightness_container)

        self.volume_container = QVBoxLayout()
        self.volume_container.setObjectName("volume_container")
        self.volume_label = QLabel(self.general_tab)
        self.volume_label.setObjectName("volume_label")

        self.volume_container.addWidget(self.volume_label)

        self.volume_slider_container = QHBoxLayout()
        self.volume_slider_container.setObjectName("volume_slider_container")
        self.volume_slider = QSlider(self.general_tab)
        self.volume_slider.setObjectName("volume_slider")
        self.volume_slider.setMinimumSize(QSize(150, 0))
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.volume_slider_container.addWidget(self.volume_slider)

        self.volume_value_text = QLabel(self.general_tab)
        self.volume_value_text.setObjectName("volume_value_text")
        self.volume_value_text.setMinimumSize(QSize(38, 0))

        self.volume_slider_container.addWidget(self.volume_value_text)

        self.volume_container.addLayout(self.volume_slider_container)

        self.sliders_container.addLayout(self.volume_container)

        self.footer_container.addLayout(self.sliders_container)

        self.general_container.addLayout(self.footer_container)

        self.gridLayout_3.addLayout(self.general_container, 0, 0, 1, 1)

        self.tabs.addTab(self.general_tab, "")
        self.media_tab = QWidget()
        self.media_tab.setObjectName("media_tab")
        self.media_tab.setEnabled(False)
        self.gridLayout_2 = QGridLayout(self.media_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttons_container = QGridLayout()
        self.buttons_container.setObjectName("buttons_container")
        self.left_button = QPushButton(self.media_tab)
        self.left_button.setObjectName("left_button")
        self.left_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.left_button.setAutoFillBackground(False)
        self.left_button.setIconSize(QSize(32, 32))
        self.left_button.setFlat(True)

        self.buttons_container.addWidget(self.left_button, 1, 0, 1, 1)

        self.right_button = QPushButton(self.media_tab)
        self.right_button.setObjectName("right_button")
        self.right_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.right_button.setAutoFillBackground(False)
        self.right_button.setIconSize(QSize(32, 32))
        self.right_button.setFlat(True)

        self.buttons_container.addWidget(self.right_button, 1, 2, 1, 1)

        self.enter_button = QPushButton(self.media_tab)
        self.enter_button.setObjectName("enter_button")
        self.enter_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.enter_button.setAutoFillBackground(False)
        self.enter_button.setIconSize(QSize(32, 32))
        self.enter_button.setFlat(True)

        self.buttons_container.addWidget(self.enter_button, 1, 1, 1, 1)

        self.up_button = QPushButton(self.media_tab)
        self.up_button.setObjectName("up_button")
        self.up_button.setEnabled(False)
        palette = QPalette()
        brush = QBrush(QColor(255, 147, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.up_button.setPalette(palette)
        self.up_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.up_button.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(
            "../src/ui/media/up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.up_button.setIcon(icon1)
        self.up_button.setIconSize(QSize(32, 32))
        self.up_button.setFlat(True)

        self.buttons_container.addWidget(self.up_button, 0, 1, 1, 1)

        self.back_button = QPushButton(self.media_tab)
        self.back_button.setObjectName("back_button")
        self.back_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.back_button.setAutoFillBackground(False)
        self.back_button.setIconSize(QSize(32, 32))
        self.back_button.setFlat(True)

        self.buttons_container.addWidget(self.back_button, 2, 0, 1, 1)

        self.down_button = QPushButton(self.media_tab)
        self.down_button.setObjectName("down_button")
        self.down_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.down_button.setAutoFillBackground(False)
        self.down_button.setIconSize(QSize(32, 32))
        self.down_button.setFlat(True)

        self.buttons_container.addWidget(self.down_button, 2, 1, 1, 1)

        self.pause_button = QPushButton(self.media_tab)
        self.pause_button.setObjectName("pause_button")
        self.pause_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pause_button.setAutoFillBackground(False)
        self.pause_button.setIconSize(QSize(32, 32))
        self.pause_button.setFlat(True)

        self.buttons_container.addWidget(self.pause_button, 2, 2, 1, 1)

        self.gridLayout_2.addLayout(self.buttons_container, 1, 1, 1, 1)

        self.horizontal_spacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontal_spacer_2, 1, 0, 1, 1)

        self.vertical_spacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_2.addItem(self.vertical_spacer_3, 0, 1, 1, 1)

        self.horizontal_spacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_2.addItem(self.horizontal_spacer_3, 1, 2, 1, 1)

        self.vertical_spacer_4 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_2.addItem(self.vertical_spacer_4, 2, 1, 1, 1)

        self.tabs.addTab(self.media_tab, "")
        self.apps_tab = QWidget()
        self.apps_tab.setObjectName("apps_tab")
        self.apps_tab.setEnabled(False)
        self.tabs.addTab(self.apps_tab, "")
        self.activities_tab = QWidget()
        self.activities_tab.setObjectName("activities_tab")
        self.activities_tab.setEnabled(False)
        self.tabs.addTab(self.activities_tab, "")
        self.processes_tab = QWidget()
        self.processes_tab.setObjectName("processes_tab")
        self.processes_tab.setEnabled(False)
        self.tabs.addTab(self.processes_tab, "")

        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)

        self.retranslateUi(ADBenQ)

        self.tabs.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(ADBenQ)

    # setupUi

    def retranslateUi(self, ADBenQ):
        ADBenQ.setWindowTitle(QCoreApplication.translate("ADBenQ", "ADBenQ", None))
        self.state_text.setText(
            QCoreApplication.translate(
                "ADBenQ",
                '<html><head/><body><p><span style=" color:#ffffff;">State:</span><span style=" color:#ff2600;"> disconnected</span></p></body></html>',
                None,
            )
        )
        self.log_text.setText("")
        self.scrcpy_button.setText(QCoreApplication.translate("ADBenQ", "Scrcpy", None))
        self.settings_button.setText(
            QCoreApplication.translate("ADBenQ", "Settings", None)
        )
        self.screenshot_button.setText(
            QCoreApplication.translate("ADBenQ", "Screenshot", None)
        )
        self.refresh_button.setText(
            QCoreApplication.translate("ADBenQ", "Refresh", None)
        )
        self.ip_input.setPlaceholderText(
            QCoreApplication.translate("ADBenQ", "IP", None)
        )
        self.connect_button.setText(
            QCoreApplication.translate("ADBenQ", "Connect", None)
        )
        self.informations_group.setTitle(
            QCoreApplication.translate("ADBenQ", "Informations", None)
        )
        self.device_name_text.setText(
            QCoreApplication.translate("ADBenQ", "Name:", None)
        )
        self.device_model_text.setText(
            QCoreApplication.translate("ADBenQ", "Model:", None)
        )
        self.device_version_text.setText(
            QCoreApplication.translate("ADBenQ", "Android version:", None)
        )
        self.device_screen_resolution_text.setText(
            QCoreApplication.translate("ADBenQ", "Screen resolution:", None)
        )
        self.screen_group.setTitle(QCoreApplication.translate("ADBenQ", "Screen", None))
        self.display_checkbox.setText(
            QCoreApplication.translate("ADBenQ", "Display", None)
        )
        self.width_input.setPlaceholderText(
            QCoreApplication.translate("ADBenQ", "Width", None)
        )
        self.height_input.setPlaceholderText(
            QCoreApplication.translate("ADBenQ", "Height", None)
        )
        self.set_screen_button.setText(
            QCoreApplication.translate("ADBenQ", "Set", None)
        )
        self.reset_screen_button.setText(
            QCoreApplication.translate("ADBenQ", "Reset", None)
        )
        self.battery_input.setPlaceholderText(
            QCoreApplication.translate("ADBenQ", "Battery level", None)
        )
        self.set_battery_button.setText(
            QCoreApplication.translate("ADBenQ", "Set", None)
        )
        self.reset_battery_button.setText(
            QCoreApplication.translate("ADBenQ", "Reset", None)
        )
        self.link_input.setText("")
        self.link_input.setPlaceholderText(
            QCoreApplication.translate("ADBenQ", "URL", None)
        )
        self.link_button.setText(QCoreApplication.translate("ADBenQ", "Open", None))
        self.brightness_label.setText(
            QCoreApplication.translate("ADBenQ", "Brightness", None)
        )
        self.brightness_value_text.setText(
            QCoreApplication.translate("ADBenQ", "-- %", None)
        )
        self.volume_label.setText(QCoreApplication.translate("ADBenQ", "Volume", None))
        self.volume_value_text.setText(
            QCoreApplication.translate("ADBenQ", "-- %", None)
        )
        self.tabs.setTabText(
            self.tabs.indexOf(self.general_tab),
            QCoreApplication.translate("ADBenQ", "General", None),
        )
        self.left_button.setText("")
        self.right_button.setText("")
        self.enter_button.setText("")
        self.up_button.setText("")
        self.back_button.setText("")
        self.down_button.setText("")
        self.pause_button.setText("")
        self.tabs.setTabText(
            self.tabs.indexOf(self.media_tab),
            QCoreApplication.translate("ADBenQ", "Media", None),
        )
        self.tabs.setTabText(
            self.tabs.indexOf(self.apps_tab),
            QCoreApplication.translate("ADBenQ", "Apps", None),
        )
        self.tabs.setTabText(
            self.tabs.indexOf(self.activities_tab),
            QCoreApplication.translate("ADBenQ", "Activities", None),
        )
        self.tabs.setTabText(
            self.tabs.indexOf(self.processes_tab),
            QCoreApplication.translate("ADBenQ", "Processes", None),
        )

    # retranslateUi
