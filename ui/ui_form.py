# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
import rc_ui

class Ui_ADBenQ(object):
    def setupUi(self, ADBenQ):
        if not ADBenQ.objectName():
            ADBenQ.setObjectName(u"ADBenQ")
        ADBenQ.setEnabled(True)
        ADBenQ.resize(682, 484)
        ADBenQ.setMinimumSize(QSize(540, 0))
        icon = QIcon()
        icon.addFile(u"src/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ADBenQ.setWindowIcon(icon)
        self.gridLayout = QGridLayout(ADBenQ)
        self.gridLayout.setObjectName(u"gridLayout")
        self.state_container = QHBoxLayout()
        self.state_container.setObjectName(u"state_container")
        self.state_text = QLabel(ADBenQ)
        self.state_text.setObjectName(u"state_text")

        self.state_container.addWidget(self.state_text)

        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.state_container.addItem(self.horizontal_spacer)

        self.log_text = QLabel(ADBenQ)
        self.log_text.setObjectName(u"log_text")

        self.state_container.addWidget(self.log_text)


        self.gridLayout.addLayout(self.state_container, 1, 0, 1, 1)

        self.tabs = QTabWidget(ADBenQ)
        self.tabs.setObjectName(u"tabs")
        self.tabs.setEnabled(True)
        self.general_tab = QWidget()
        self.general_tab.setObjectName(u"general_tab")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.general_tab.sizePolicy().hasHeightForWidth())
        self.general_tab.setSizePolicy(sizePolicy)
        self.general_tab.setMinimumSize(QSize(0, 0))
        self.gridLayout_3 = QGridLayout(self.general_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, -1, 10, 10)
        self.general_container = QVBoxLayout()
        self.general_container.setObjectName(u"general_container")
        self.header_container = QHBoxLayout()
        self.header_container.setObjectName(u"header_container")
        self.scrcpy_button = QPushButton(self.general_tab)
        self.scrcpy_button.setObjectName(u"scrcpy_button")

        self.header_container.addWidget(self.scrcpy_button)

        self.settings_button = QPushButton(self.general_tab)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setEnabled(True)

        self.header_container.addWidget(self.settings_button)

        self.screenshot_button = QPushButton(self.general_tab)
        self.screenshot_button.setObjectName(u"screenshot_button")
        self.screenshot_button.setMinimumSize(QSize(0, 0))

        self.header_container.addWidget(self.screenshot_button)

        self.refresh_button = QPushButton(self.general_tab)
        self.refresh_button.setObjectName(u"refresh_button")

        self.header_container.addWidget(self.refresh_button)

        self.ip_input = QLineEdit(self.general_tab)
        self.ip_input.setObjectName(u"ip_input")
        self.ip_input.setMinimumSize(QSize(0, 0))
        self.ip_input.setMaximumSize(QSize(110, 16777215))
        self.ip_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.ip_input.setMaxLength(15)
        self.ip_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.header_container.addWidget(self.ip_input)

        self.connect_button = QPushButton(self.general_tab)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setMinimumSize(QSize(78, 0))

        self.header_container.addWidget(self.connect_button)


        self.general_container.addLayout(self.header_container)

        self.vertical_spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.general_container.addItem(self.vertical_spacer)

        self.main_container = QHBoxLayout()
        self.main_container.setObjectName(u"main_container")
        self.informations_group = QGroupBox(self.general_tab)
        self.informations_group.setObjectName(u"informations_group")
        self.informations_group.setEnabled(True)
        self.informations_group.setMinimumSize(QSize(250, 0))
        self.verticalLayout_3 = QVBoxLayout(self.informations_group)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.device_name_text = QLabel(self.informations_group)
        self.device_name_text.setObjectName(u"device_name_text")

        self.verticalLayout_3.addWidget(self.device_name_text)

        self.device_model_text = QLabel(self.informations_group)
        self.device_model_text.setObjectName(u"device_model_text")

        self.verticalLayout_3.addWidget(self.device_model_text)

        self.device_version_text = QLabel(self.informations_group)
        self.device_version_text.setObjectName(u"device_version_text")

        self.verticalLayout_3.addWidget(self.device_version_text)

        self.device_screen_resolution_text = QLabel(self.informations_group)
        self.device_screen_resolution_text.setObjectName(u"device_screen_resolution_text")

        self.verticalLayout_3.addWidget(self.device_screen_resolution_text)


        self.main_container.addWidget(self.informations_group)

        self.horizontal_spacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.main_container.addItem(self.horizontal_spacer_4)

        self.screen_group = QGroupBox(self.general_tab)
        self.screen_group.setObjectName(u"screen_group")
        self.screen_group.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.screen_group.setFlat(False)
        self.screen_layout = QVBoxLayout(self.screen_group)
        self.screen_layout.setSpacing(0)
        self.screen_layout.setObjectName(u"screen_layout")
        self.display_checkbox = QCheckBox(self.screen_group)
        self.display_checkbox.setObjectName(u"display_checkbox")
        self.display_checkbox.setChecked(False)

        self.screen_layout.addWidget(self.display_checkbox)

        self.vertical_spacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.screen_layout.addItem(self.vertical_spacer_5)

        self.screen_inputs_container = QHBoxLayout()
        self.screen_inputs_container.setSpacing(10)
        self.screen_inputs_container.setObjectName(u"screen_inputs_container")
        self.screen_inputs_container.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.screen_inputs_container.setContentsMargins(-1, 0, -1, -1)
        self.width_input = QLineEdit(self.screen_group)
        self.width_input.setObjectName(u"width_input")
        self.width_input.setMaximumSize(QSize(100, 16777215))
        self.width_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.width_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.screen_inputs_container.addWidget(self.width_input)

        self.height_input = QLineEdit(self.screen_group)
        self.height_input.setObjectName(u"height_input")
        self.height_input.setMaximumSize(QSize(100, 16777215))
        self.height_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.height_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.screen_inputs_container.addWidget(self.height_input)


        self.screen_layout.addLayout(self.screen_inputs_container)

        self.screen_button_container = QHBoxLayout()
        self.screen_button_container.setSpacing(10)
        self.screen_button_container.setObjectName(u"screen_button_container")
        self.screen_button_container.setContentsMargins(-1, 10, -1, 0)
        self.horizontal_spacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.screen_button_container.addItem(self.horizontal_spacer_5)

        self.set_screen_button = QPushButton(self.screen_group)
        self.set_screen_button.setObjectName(u"set_screen_button")

        self.screen_button_container.addWidget(self.set_screen_button)

        self.reset_screen_button = QPushButton(self.screen_group)
        self.reset_screen_button.setObjectName(u"reset_screen_button")

        self.screen_button_container.addWidget(self.reset_screen_button)


        self.screen_layout.addLayout(self.screen_button_container)


        self.main_container.addWidget(self.screen_group)


        self.general_container.addLayout(self.main_container)

        self.vertical_spacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.general_container.addItem(self.vertical_spacer_2)

        self.footer_container = QHBoxLayout()
        self.footer_container.setObjectName(u"footer_container")
        self.footer_left_container = QVBoxLayout()
        self.footer_left_container.setObjectName(u"footer_left_container")
        self.battery_container = QHBoxLayout()
        self.battery_container.setObjectName(u"battery_container")
        self.battery_container.setContentsMargins(-1, 0, -1, -1)
        self.battery_input = QLineEdit(self.general_tab)
        self.battery_input.setObjectName(u"battery_input")
        self.battery_input.setMinimumSize(QSize(100, 0))
        self.battery_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.battery_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.battery_container.addWidget(self.battery_input)

        self.set_battery_button = QPushButton(self.general_tab)
        self.set_battery_button.setObjectName(u"set_battery_button")

        self.battery_container.addWidget(self.set_battery_button)

        self.reset_battery_button = QPushButton(self.general_tab)
        self.reset_battery_button.setObjectName(u"reset_battery_button")

        self.battery_container.addWidget(self.reset_battery_button)


        self.footer_left_container.addLayout(self.battery_container)

        self.link_container = QHBoxLayout()
        self.link_container.setObjectName(u"link_container")
        self.link_input = QLineEdit(self.general_tab)
        self.link_input.setObjectName(u"link_input")
        self.link_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.link_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.link_container.addWidget(self.link_input)

        self.link_button = QPushButton(self.general_tab)
        self.link_button.setObjectName(u"link_button")
        self.link_button.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.link_container.addWidget(self.link_button)


        self.footer_left_container.addLayout(self.link_container)


        self.footer_container.addLayout(self.footer_left_container)

        self.horizontal_spacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.footer_container.addItem(self.horizontal_spacer_6)

        self.sliders_container = QVBoxLayout()
        self.sliders_container.setObjectName(u"sliders_container")
        self.brightness_container = QVBoxLayout()
        self.brightness_container.setObjectName(u"brightness_container")
        self.brightness_label = QLabel(self.general_tab)
        self.brightness_label.setObjectName(u"brightness_label")

        self.brightness_container.addWidget(self.brightness_label)

        self.brightness_slider_container = QHBoxLayout()
        self.brightness_slider_container.setObjectName(u"brightness_slider_container")
        self.brightness_slider = QSlider(self.general_tab)
        self.brightness_slider.setObjectName(u"brightness_slider")
        self.brightness_slider.setMinimumSize(QSize(150, 0))
        self.brightness_slider.setMinimum(1)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setOrientation(Qt.Orientation.Horizontal)

        self.brightness_slider_container.addWidget(self.brightness_slider)

        self.brightness_value_text = QLabel(self.general_tab)
        self.brightness_value_text.setObjectName(u"brightness_value_text")
        self.brightness_value_text.setMinimumSize(QSize(38, 0))

        self.brightness_slider_container.addWidget(self.brightness_value_text)


        self.brightness_container.addLayout(self.brightness_slider_container)


        self.sliders_container.addLayout(self.brightness_container)

        self.volume_container = QVBoxLayout()
        self.volume_container.setObjectName(u"volume_container")
        self.volume_label_container = QHBoxLayout()
        self.volume_label_container.setSpacing(10)
        self.volume_label_container.setObjectName(u"volume_label_container")
        self.volume_label = QLabel(self.general_tab)
        self.volume_label.setObjectName(u"volume_label")

        self.volume_label_container.addWidget(self.volume_label)

        self.volume_slider_show_checkbox = QCheckBox(self.general_tab)
        self.volume_slider_show_checkbox.setObjectName(u"volume_slider_show_checkbox")

        self.volume_label_container.addWidget(self.volume_slider_show_checkbox)

        self.horizontal_spacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.volume_label_container.addItem(self.horizontal_spacer_7)


        self.volume_container.addLayout(self.volume_label_container)

        self.volume_slider_container = QHBoxLayout()
        self.volume_slider_container.setObjectName(u"volume_slider_container")
        self.volume_slider = QSlider(self.general_tab)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setMinimumSize(QSize(150, 0))
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.volume_slider_container.addWidget(self.volume_slider)

        self.volume_value_text = QLabel(self.general_tab)
        self.volume_value_text.setObjectName(u"volume_value_text")
        self.volume_value_text.setMinimumSize(QSize(38, 0))

        self.volume_slider_container.addWidget(self.volume_value_text)


        self.volume_container.addLayout(self.volume_slider_container)


        self.sliders_container.addLayout(self.volume_container)


        self.footer_container.addLayout(self.sliders_container)


        self.general_container.addLayout(self.footer_container)


        self.gridLayout_3.addLayout(self.general_container, 0, 0, 1, 1)

        self.tabs.addTab(self.general_tab, "")
        self.media_tab = QWidget()
        self.media_tab.setObjectName(u"media_tab")
        self.media_tab.setEnabled(False)
        self.gridLayout_2 = QGridLayout(self.media_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.buttons_container = QGridLayout()
        self.buttons_container.setObjectName(u"buttons_container")
        self.left_button = QPushButton(self.media_tab)
        self.left_button.setObjectName(u"left_button")
        self.left_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.left_button.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u":/media/src/media/left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.left_button.setIcon(icon1)
        self.left_button.setIconSize(QSize(32, 32))
        self.left_button.setFlat(True)

        self.buttons_container.addWidget(self.left_button, 1, 0, 1, 1)

        self.back_button = QPushButton(self.media_tab)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.back_button.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/media/src/media/back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_button.setIcon(icon2)
        self.back_button.setIconSize(QSize(32, 32))
        self.back_button.setFlat(True)

        self.buttons_container.addWidget(self.back_button, 2, 0, 1, 1)

        self.right_button = QPushButton(self.media_tab)
        self.right_button.setObjectName(u"right_button")
        self.right_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.right_button.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u":/media/src/media/right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.right_button.setIcon(icon3)
        self.right_button.setIconSize(QSize(32, 32))
        self.right_button.setFlat(True)

        self.buttons_container.addWidget(self.right_button, 1, 2, 1, 1)

        self.pause_button = QPushButton(self.media_tab)
        self.pause_button.setObjectName(u"pause_button")
        self.pause_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pause_button.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u":/media/src/media/pause_circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pause_button.setIcon(icon4)
        self.pause_button.setIconSize(QSize(32, 32))
        self.pause_button.setFlat(True)

        self.buttons_container.addWidget(self.pause_button, 2, 2, 1, 1)

        self.down_button = QPushButton(self.media_tab)
        self.down_button.setObjectName(u"down_button")
        self.down_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.down_button.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u":/media/src/media/down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.down_button.setIcon(icon5)
        self.down_button.setIconSize(QSize(32, 32))
        self.down_button.setFlat(True)

        self.buttons_container.addWidget(self.down_button, 2, 1, 1, 1)

        self.enter_button = QPushButton(self.media_tab)
        self.enter_button.setObjectName(u"enter_button")
        self.enter_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.enter_button.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/media/src/media/enter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.enter_button.setIcon(icon6)
        self.enter_button.setIconSize(QSize(32, 32))
        self.enter_button.setFlat(True)

        self.buttons_container.addWidget(self.enter_button, 1, 1, 1, 1)

        self.up_button = QPushButton(self.media_tab)
        self.up_button.setObjectName(u"up_button")
        icon7 = QIcon()
        icon7.addFile(u":/media/src/media/up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.up_button.setIcon(icon7)
        self.up_button.setIconSize(QSize(32, 32))
        self.up_button.setFlat(True)

        self.buttons_container.addWidget(self.up_button, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.buttons_container, 1, 1, 1, 1)

        self.horizontal_spacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontal_spacer_2, 1, 0, 1, 1)

        self.vertical_spacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.vertical_spacer_3, 0, 1, 1, 1)

        self.horizontal_spacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontal_spacer_3, 1, 2, 1, 1)

        self.vertical_spacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.vertical_spacer_4, 2, 1, 1, 1)

        self.tabs.addTab(self.media_tab, "")
        self.apps_tab = QWidget()
        self.apps_tab.setObjectName(u"apps_tab")
        self.apps_tab.setEnabled(False)
        self.tabs.addTab(self.apps_tab, "")
        self.activities_tab = QWidget()
        self.activities_tab.setObjectName(u"activities_tab")
        self.activities_tab.setEnabled(False)
        self.tabs.addTab(self.activities_tab, "")
        self.processes_tab = QWidget()
        self.processes_tab.setObjectName(u"processes_tab")
        self.processes_tab.setEnabled(False)
        self.tabs.addTab(self.processes_tab, "")

        self.gridLayout.addWidget(self.tabs, 0, 0, 1, 1)


        self.retranslateUi(ADBenQ)

        self.tabs.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(ADBenQ)
    # setupUi

    def retranslateUi(self, ADBenQ):
        ADBenQ.setWindowTitle(QCoreApplication.translate("ADBenQ", u"ADBenQ - v0.2.0-alpha", None))
        self.state_text.setText(QCoreApplication.translate("ADBenQ", u"<html><head/><body><p><span style=\" color:#ffffff;\">State:</span><span style=\" color:#ff2600;\"> disconnected</span></p></body></html>", None))
        self.log_text.setText("")
        self.scrcpy_button.setText(QCoreApplication.translate("ADBenQ", u"Scrcpy", None))
        self.settings_button.setText(QCoreApplication.translate("ADBenQ", u"Settings", None))
        self.screenshot_button.setText(QCoreApplication.translate("ADBenQ", u"Screenshot", None))
        self.refresh_button.setText(QCoreApplication.translate("ADBenQ", u"Refresh", None))
        self.ip_input.setPlaceholderText(QCoreApplication.translate("ADBenQ", u"IP", None))
        self.connect_button.setText(QCoreApplication.translate("ADBenQ", u"Connect", None))
        self.informations_group.setTitle(QCoreApplication.translate("ADBenQ", u"Informations", None))
        self.device_name_text.setText(QCoreApplication.translate("ADBenQ", u"Name:", None))
        self.device_model_text.setText(QCoreApplication.translate("ADBenQ", u"Model:", None))
        self.device_version_text.setText(QCoreApplication.translate("ADBenQ", u"Android version:", None))
        self.device_screen_resolution_text.setText(QCoreApplication.translate("ADBenQ", u"Screen resolution:", None))
        self.screen_group.setTitle(QCoreApplication.translate("ADBenQ", u"Screen", None))
        self.display_checkbox.setText(QCoreApplication.translate("ADBenQ", u"Display", None))
        self.width_input.setPlaceholderText(QCoreApplication.translate("ADBenQ", u"Width", None))
        self.height_input.setPlaceholderText(QCoreApplication.translate("ADBenQ", u"Height", None))
        self.set_screen_button.setText(QCoreApplication.translate("ADBenQ", u"Set", None))
        self.reset_screen_button.setText(QCoreApplication.translate("ADBenQ", u"Reset", None))
        self.battery_input.setPlaceholderText(QCoreApplication.translate("ADBenQ", u"Battery level", None))
        self.set_battery_button.setText(QCoreApplication.translate("ADBenQ", u"Set", None))
        self.reset_battery_button.setText(QCoreApplication.translate("ADBenQ", u"Reset", None))
        self.link_input.setText("")
        self.link_input.setPlaceholderText(QCoreApplication.translate("ADBenQ", u"URL", None))
        self.link_button.setText(QCoreApplication.translate("ADBenQ", u"Open", None))
        self.brightness_label.setText(QCoreApplication.translate("ADBenQ", u"Brightness", None))
        self.brightness_value_text.setText(QCoreApplication.translate("ADBenQ", u"-- %", None))
        self.volume_label.setText(QCoreApplication.translate("ADBenQ", u"Volume", None))
        self.volume_slider_show_checkbox.setText(QCoreApplication.translate("ADBenQ", u"Show", None))
        self.volume_value_text.setText(QCoreApplication.translate("ADBenQ", u"-- %", None))
        self.tabs.setTabText(self.tabs.indexOf(self.general_tab), QCoreApplication.translate("ADBenQ", u"General", None))
        self.left_button.setText("")
        self.back_button.setText("")
        self.right_button.setText("")
        self.pause_button.setText("")
        self.down_button.setText("")
        self.enter_button.setText("")
        self.up_button.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.media_tab), QCoreApplication.translate("ADBenQ", u"Media", None))
        self.tabs.setTabText(self.tabs.indexOf(self.apps_tab), QCoreApplication.translate("ADBenQ", u"Apps", None))
        self.tabs.setTabText(self.tabs.indexOf(self.activities_tab), QCoreApplication.translate("ADBenQ", u"Activities", None))
        self.tabs.setTabText(self.tabs.indexOf(self.processes_tab), QCoreApplication.translate("ADBenQ", u"Processes", None))
    # retranslateUi

