# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
        self.state_layout = QHBoxLayout()
        self.state_layout.setObjectName(u"state_layout")
        self.state_text = QLabel(ADBenQ)
        self.state_text.setObjectName(u"state_text")

        self.state_layout.addWidget(self.state_text)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.state_layout.addItem(self.horizontalSpacer)

        self.info_text = QLabel(ADBenQ)
        self.info_text.setObjectName(u"info_text")

        self.state_layout.addWidget(self.info_text)


        self.gridLayout.addLayout(self.state_layout, 1, 0, 1, 1)

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
        self.general_layout = QVBoxLayout()
        self.general_layout.setObjectName(u"general_layout")
        self.header_layout = QHBoxLayout()
        self.header_layout.setObjectName(u"header_layout")
        self.scrcpy_button = QPushButton(self.general_tab)
        self.scrcpy_button.setObjectName(u"scrcpy_button")

        self.header_layout.addWidget(self.scrcpy_button)

        self.settings_button = QPushButton(self.general_tab)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setEnabled(True)

        self.header_layout.addWidget(self.settings_button)

        self.screenshot_button = QPushButton(self.general_tab)
        self.screenshot_button.setObjectName(u"screenshot_button")
        self.screenshot_button.setMinimumSize(QSize(0, 0))

        self.header_layout.addWidget(self.screenshot_button)

        self.refresh_button = QPushButton(self.general_tab)
        self.refresh_button.setObjectName(u"refresh_button")

        self.header_layout.addWidget(self.refresh_button)

        self.ip_input = QLineEdit(self.general_tab)
        self.ip_input.setObjectName(u"ip_input")
        self.ip_input.setMinimumSize(QSize(0, 0))
        self.ip_input.setMaximumSize(QSize(110, 16777215))
        self.ip_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.ip_input.setMaxLength(15)
        self.ip_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.header_layout.addWidget(self.ip_input)

        self.connect_button = QPushButton(self.general_tab)
        self.connect_button.setObjectName(u"connect_button")
        self.connect_button.setMinimumSize(QSize(78, 0))

        self.header_layout.addWidget(self.connect_button)


        self.general_layout.addLayout(self.header_layout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.general_layout.addItem(self.verticalSpacer)

        self.main_layout = QHBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
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

        self.device_screen_text = QLabel(self.informations_group)
        self.device_screen_text.setObjectName(u"device_screen_text")

        self.verticalLayout_3.addWidget(self.device_screen_text)


        self.main_layout.addWidget(self.informations_group)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.main_layout.addItem(self.horizontalSpacer_3)

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

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.screen_layout.addItem(self.verticalSpacer_3)

        self.screen_inputs_layout = QHBoxLayout()
        self.screen_inputs_layout.setSpacing(10)
        self.screen_inputs_layout.setObjectName(u"screen_inputs_layout")
        self.screen_inputs_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.screen_inputs_layout.setContentsMargins(-1, 0, -1, -1)
        self.width_input = QLineEdit(self.screen_group)
        self.width_input.setObjectName(u"width_input")
        self.width_input.setMaximumSize(QSize(100, 16777215))
        self.width_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.width_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.screen_inputs_layout.addWidget(self.width_input)

        self.height_input = QLineEdit(self.screen_group)
        self.height_input.setObjectName(u"height_input")
        self.height_input.setMaximumSize(QSize(100, 16777215))
        self.height_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.height_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.screen_inputs_layout.addWidget(self.height_input)


        self.screen_layout.addLayout(self.screen_inputs_layout)

        self.screen_button_layout = QHBoxLayout()
        self.screen_button_layout.setSpacing(10)
        self.screen_button_layout.setObjectName(u"screen_button_layout")
        self.screen_button_layout.setContentsMargins(-1, 10, -1, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.screen_button_layout.addItem(self.horizontalSpacer_2)

        self.screen_button = QPushButton(self.screen_group)
        self.screen_button.setObjectName(u"screen_button")

        self.screen_button_layout.addWidget(self.screen_button)

        self.reset_screen_button = QPushButton(self.screen_group)
        self.reset_screen_button.setObjectName(u"reset_screen_button")

        self.screen_button_layout.addWidget(self.reset_screen_button)


        self.screen_layout.addLayout(self.screen_button_layout)


        self.main_layout.addWidget(self.screen_group)


        self.general_layout.addLayout(self.main_layout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.general_layout.addItem(self.verticalSpacer_2)

        self.footer_layout = QHBoxLayout()
        self.footer_layout.setObjectName(u"footer_layout")
        self.footer_left_layout = QVBoxLayout()
        self.footer_left_layout.setObjectName(u"footer_left_layout")
        self.battery_layout = QHBoxLayout()
        self.battery_layout.setObjectName(u"battery_layout")
        self.battery_layout.setContentsMargins(-1, 0, -1, -1)
        self.battery_input = QLineEdit(self.general_tab)
        self.battery_input.setObjectName(u"battery_input")
        self.battery_input.setMinimumSize(QSize(100, 0))
        self.battery_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.battery_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.battery_layout.addWidget(self.battery_input)

        self.battery_button = QPushButton(self.general_tab)
        self.battery_button.setObjectName(u"battery_button")

        self.battery_layout.addWidget(self.battery_button)

        self.reset_battery_button = QPushButton(self.general_tab)
        self.reset_battery_button.setObjectName(u"reset_battery_button")

        self.battery_layout.addWidget(self.reset_battery_button)


        self.footer_left_layout.addLayout(self.battery_layout)

        self.link_layout = QHBoxLayout()
        self.link_layout.setObjectName(u"link_layout")
        self.link_input = QLineEdit(self.general_tab)
        self.link_input.setObjectName(u"link_input")
        self.link_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.link_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.link_layout.addWidget(self.link_input)

        self.link_button = QPushButton(self.general_tab)
        self.link_button.setObjectName(u"link_button")
        self.link_button.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.link_layout.addWidget(self.link_button)


        self.footer_left_layout.addLayout(self.link_layout)


        self.footer_layout.addLayout(self.footer_left_layout)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.footer_layout.addItem(self.horizontalSpacer_5)

        self.sliders_layout = QVBoxLayout()
        self.sliders_layout.setObjectName(u"sliders_layout")
        self.brightness_layout = QVBoxLayout()
        self.brightness_layout.setObjectName(u"brightness_layout")
        self.brightness_label = QLabel(self.general_tab)
        self.brightness_label.setObjectName(u"brightness_label")

        self.brightness_layout.addWidget(self.brightness_label)

        self.brightness_slider_layout = QHBoxLayout()
        self.brightness_slider_layout.setObjectName(u"brightness_slider_layout")
        self.brightness_slider = QSlider(self.general_tab)
        self.brightness_slider.setObjectName(u"brightness_slider")
        self.brightness_slider.setMinimumSize(QSize(150, 0))
        self.brightness_slider.setMinimum(1)
        self.brightness_slider.setMaximum(100)
        self.brightness_slider.setOrientation(Qt.Orientation.Horizontal)

        self.brightness_slider_layout.addWidget(self.brightness_slider)

        self.brightness_value = QLabel(self.general_tab)
        self.brightness_value.setObjectName(u"brightness_value")
        self.brightness_value.setMinimumSize(QSize(38, 0))

        self.brightness_slider_layout.addWidget(self.brightness_value)


        self.brightness_layout.addLayout(self.brightness_slider_layout)


        self.sliders_layout.addLayout(self.brightness_layout)

        self.volume_layout = QVBoxLayout()
        self.volume_layout.setObjectName(u"volume_layout")
        self.volume_label = QLabel(self.general_tab)
        self.volume_label.setObjectName(u"volume_label")

        self.volume_layout.addWidget(self.volume_label)

        self.volume_slider_layout = QHBoxLayout()
        self.volume_slider_layout.setObjectName(u"volume_slider_layout")
        self.volume_slider = QSlider(self.general_tab)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setMinimumSize(QSize(150, 0))
        self.volume_slider.setMinimum(0)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.volume_slider_layout.addWidget(self.volume_slider)

        self.volume_value = QLabel(self.general_tab)
        self.volume_value.setObjectName(u"volume_value")
        self.volume_value.setMinimumSize(QSize(38, 0))

        self.volume_slider_layout.addWidget(self.volume_value)


        self.volume_layout.addLayout(self.volume_slider_layout)


        self.sliders_layout.addLayout(self.volume_layout)


        self.footer_layout.addLayout(self.sliders_layout)


        self.general_layout.addLayout(self.footer_layout)


        self.gridLayout_3.addLayout(self.general_layout, 0, 0, 1, 1)

        self.tabs.addTab(self.general_tab, "")
        self.media_tab = QWidget()
        self.media_tab.setObjectName(u"media_tab")
        self.media_tab.setEnabled(False)
        self.gridLayout_2 = QGridLayout(self.media_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.buttons_layout = QGridLayout()
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.left_button = QPushButton(self.media_tab)
        self.left_button.setObjectName(u"left_button")
        self.left_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.left_button.setAutoFillBackground(False)
        icon1 = QIcon()
        icon1.addFile(u"src/ui/media/left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.left_button.setIcon(icon1)
        self.left_button.setIconSize(QSize(32, 32))
        self.left_button.setFlat(True)

        self.buttons_layout.addWidget(self.left_button, 1, 0, 1, 1)

        self.right_button = QPushButton(self.media_tab)
        self.right_button.setObjectName(u"right_button")
        self.right_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.right_button.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u"src/ui/media/right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.right_button.setIcon(icon2)
        self.right_button.setIconSize(QSize(32, 32))
        self.right_button.setFlat(True)

        self.buttons_layout.addWidget(self.right_button, 1, 2, 1, 1)

        self.enter_button = QPushButton(self.media_tab)
        self.enter_button.setObjectName(u"enter_button")
        self.enter_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.enter_button.setAutoFillBackground(False)
        icon3 = QIcon()
        icon3.addFile(u"src/ui/media/enter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.enter_button.setIcon(icon3)
        self.enter_button.setIconSize(QSize(32, 32))
        self.enter_button.setFlat(True)

        self.buttons_layout.addWidget(self.enter_button, 1, 1, 1, 1)

        self.up_button = QPushButton(self.media_tab)
        self.up_button.setObjectName(u"up_button")
        palette = QPalette()
        brush = QBrush(QColor(255, 147, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.up_button.setPalette(palette)
        self.up_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.up_button.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u"src/ui/media/up.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.up_button.setIcon(icon4)
        self.up_button.setIconSize(QSize(32, 32))
        self.up_button.setFlat(True)

        self.buttons_layout.addWidget(self.up_button, 0, 1, 1, 1)

        self.back_button = QPushButton(self.media_tab)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.back_button.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u"src/ui/media/back.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_button.setIcon(icon5)
        self.back_button.setIconSize(QSize(32, 32))
        self.back_button.setFlat(True)

        self.buttons_layout.addWidget(self.back_button, 2, 0, 1, 1)

        self.down_button = QPushButton(self.media_tab)
        self.down_button.setObjectName(u"down_button")
        self.down_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.down_button.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u"src/ui/media/down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.down_button.setIcon(icon6)
        self.down_button.setIconSize(QSize(32, 32))
        self.down_button.setFlat(True)

        self.buttons_layout.addWidget(self.down_button, 2, 1, 1, 1)

        self.pause_button = QPushButton(self.media_tab)
        self.pause_button.setObjectName(u"pause_button")
        self.pause_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.pause_button.setAutoFillBackground(False)
        icon7 = QIcon()
        icon7.addFile(u"src/ui/media/pause-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pause_button.setIcon(icon7)
        self.pause_button.setIconSize(QSize(32, 32))
        self.pause_button.setFlat(True)

        self.buttons_layout.addWidget(self.pause_button, 2, 2, 1, 1)


        self.gridLayout_2.addLayout(self.buttons_layout, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 1, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 2, 1, 1, 1)

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

        self.tabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ADBenQ)
    # setupUi

    def retranslateUi(self, ADBenQ):
        ADBenQ.setWindowTitle(QCoreApplication.translate("ADBenQ", u"ADBenQ", None))
        self.state_text.setText(QCoreApplication.translate("ADBenQ", u"<html><head/><body><p><span style=\" color:#ffffff;\">State:</span><span style=\" color:#ff2600;\"> disconnected</span></p></body></html>", None))
        self.info_text.setText("")
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
        self.device_screen_text.setText(QCoreApplication.translate("ADBenQ", u"Screen resolution:", None))
        self.screen_group.setTitle(QCoreApplication.translate("ADBenQ", u"Screen", None))
        self.display_checkbox.setText(QCoreApplication.translate("ADBenQ", u"Display", None))
        self.width_input.setPlaceholderText(QCoreApplication.translate("ADBenQ", u"Width", None))
        self.height_input.setPlaceholderText(QCoreApplication.translate("ADBenQ", u"Height", None))
        self.screen_button.setText(QCoreApplication.translate("ADBenQ", u"Set", None))
        self.reset_screen_button.setText(QCoreApplication.translate("ADBenQ", u"Reset", None))
        self.battery_input.setPlaceholderText(QCoreApplication.translate("ADBenQ", u"Battery level", None))
        self.battery_button.setText(QCoreApplication.translate("ADBenQ", u"Set", None))
        self.reset_battery_button.setText(QCoreApplication.translate("ADBenQ", u"Reset", None))
        self.link_input.setText("")
        self.link_input.setPlaceholderText(QCoreApplication.translate("ADBenQ", u"URL", None))
        self.link_button.setText(QCoreApplication.translate("ADBenQ", u"Open", None))
        self.brightness_label.setText(QCoreApplication.translate("ADBenQ", u"Brightness", None))
        self.brightness_value.setText(QCoreApplication.translate("ADBenQ", u"-- %", None))
        self.volume_label.setText(QCoreApplication.translate("ADBenQ", u"Volume", None))
        self.volume_value.setText(QCoreApplication.translate("ADBenQ", u"-- %", None))
        self.tabs.setTabText(self.tabs.indexOf(self.general_tab), QCoreApplication.translate("ADBenQ", u"General", None))
        self.left_button.setText("")
        self.right_button.setText("")
        self.enter_button.setText("")
        self.up_button.setText("")
        self.back_button.setText("")
        self.down_button.setText("")
        self.pause_button.setText("")
        self.tabs.setTabText(self.tabs.indexOf(self.media_tab), QCoreApplication.translate("ADBenQ", u"Media", None))
        self.tabs.setTabText(self.tabs.indexOf(self.apps_tab), QCoreApplication.translate("ADBenQ", u"Apps", None))
        self.tabs.setTabText(self.tabs.indexOf(self.activities_tab), QCoreApplication.translate("ADBenQ", u"Activities", None))
        self.tabs.setTabText(self.tabs.indexOf(self.processes_tab), QCoreApplication.translate("ADBenQ", u"Processes", None))
    # retranslateUi

