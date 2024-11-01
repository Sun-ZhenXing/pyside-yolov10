# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QGridLayout,
    QGroupBox,
    QLabel,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QSplitter,
    QStatusBar,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(999, 519)
        icon = QIcon()
        icon.addFile(
            ":/res/assets/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        MainWindow.setWindowIcon(icon)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        icon1 = QIcon()
        icon1.addFile(
            ":/res/assets/FluentDismiss24Regular.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.actionExit.setIcon(icon1)
        self.actionExit.setMenuRole(QAction.MenuRole.QuitRole)
        self.actionAboutQt = QAction(MainWindow)
        self.actionAboutQt.setObjectName("actionAboutQt")
        icon2 = QIcon()
        icon2.addFile(
            ":/res/assets/LogosQt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off
        )
        self.actionAboutQt.setIcon(icon2)
        self.actionAboutQt.setMenuRole(QAction.MenuRole.AboutQtRole)
        self.actionSetting = QAction(MainWindow)
        self.actionSetting.setObjectName("actionSetting")
        icon3 = QIcon()
        icon3.addFile(
            ":/res/assets/FluentWrenchScrewdriver24Regular.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.actionSetting.setIcon(icon3)
        self.actionSetting.setMenuRole(QAction.MenuRole.PreferencesRole)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        icon4 = QIcon()
        icon4.addFile(
            ":/res/assets/FluentApps24Regular.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.actionAbout.setIcon(icon4)
        self.actionOpenPicture = QAction(MainWindow)
        self.actionOpenPicture.setObjectName("actionOpenPicture")
        icon5 = QIcon()
        icon5.addFile(
            ":/res/assets/FluentFolder24Regular.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.actionOpenPicture.setIcon(icon5)
        self.actionOpenVideo = QAction(MainWindow)
        self.actionOpenVideo.setObjectName("actionOpenVideo")
        self.actionOpenVideo.setIcon(icon5)
        self.actionCamera = QAction(MainWindow)
        self.actionCamera.setObjectName("actionCamera")
        icon6 = QIcon()
        icon6.addFile(
            ":/res/assets/FluentPlayCircle24Regular.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.actionCamera.setIcon(icon6)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        icon7 = QIcon()
        icon7.addFile(
            ":/res/assets/FluentRecordStop24Regular.svg",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.actionClose.setIcon(icon7)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.gridLayoutWidget = QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_1 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.image_label = QLabel(self.gridLayoutWidget)
        self.image_label.setObjectName("image_label")
        self.image_label.setMinimumSize(QSize(400, 0))
        self.image_label.setStyleSheet("background-color: #090909")

        self.gridLayout_1.addWidget(self.image_label, 0, 0, 1, 1)

        self.splitter.addWidget(self.gridLayoutWidget)
        self.gridLayoutWidget_2 = QWidget(self.splitter)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QPushButton(self.gridLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")

        self.gridLayout_3.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_3.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.groupBox = QGroupBox(self.gridLayoutWidget_2)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.confSlider = QSlider(self.groupBox)
        self.confSlider.setObjectName("confSlider")
        self.confSlider.setMinimum(1)
        self.confSlider.setSingleStep(1)
        self.confSlider.setValue(25)
        self.confSlider.setOrientation(Qt.Orientation.Horizontal)
        self.confSlider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.confSlider.setTickInterval(10)

        self.gridLayout_4.addWidget(self.confSlider, 0, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName("label")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.gridLayout_3.addWidget(self.groupBox, 3, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.splitter.addWidget(self.gridLayoutWidget_2)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 999, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuOption = QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAboutQt)
        self.menuOption.addAction(self.actionSetting)
        self.menuOption.addAction(self.actionOpenPicture)
        self.menuOption.addAction(self.actionOpenVideo)
        self.menuOption.addAction(self.actionCamera)
        self.menuOption.addAction(self.actionClose)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionAboutQt.triggered.connect(MainWindow.aboutQt)
        self.actionSetting.triggered.connect(MainWindow.actionSettingClicked)
        self.actionAbout.triggered.connect(MainWindow.about)
        self.actionOpenPicture.triggered.connect(MainWindow.openPicture)
        self.actionOpenVideo.triggered.connect(MainWindow.openVideo)
        self.actionCamera.triggered.connect(MainWindow.openCamera)
        self.actionClose.triggered.connect(MainWindow.closeVideo)
        self.pushButton.clicked.connect(MainWindow.openPicture)
        self.pushButton_2.clicked.connect(MainWindow.openVideo)
        self.pushButton_3.clicked.connect(MainWindow.openCamera)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow", "YOLOv10 \u76ee\u6807\u68c0\u6d4b", None
            )
        )
        self.actionExit.setText(
            QCoreApplication.translate("MainWindow", "\u9000\u51fa(&X)", None)
        )
        self.actionAboutQt.setText(
            QCoreApplication.translate("MainWindow", "\u5173\u4e8e Qt(&Q)", None)
        )
        self.actionSetting.setText(
            QCoreApplication.translate("MainWindow", "\u8bbe\u7f6e(&S)", None)
        )
        # if QT_CONFIG(shortcut)
        self.actionSetting.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+E", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u5173\u4e8e\u76ee\u6807\u68c0\u6d4b\u5de5\u5177(&A)",
                None,
            )
        )
        self.actionOpenPicture.setText(
            QCoreApplication.translate(
                "MainWindow", "\u6253\u5f00\u56fe\u7247(&P)", None
            )
        )
        self.actionOpenVideo.setText(
            QCoreApplication.translate(
                "MainWindow", "\u6253\u5f00\u89c6\u9891(&V)", None
            )
        )
        self.actionCamera.setText(
            QCoreApplication.translate(
                "MainWindow", "\u6253\u5f00\u6444\u50cf\u5934(&C)", None
            )
        )
        self.actionClose.setText(
            QCoreApplication.translate("MainWindow", "\u5173\u95ed(&C)", None)
        )
        self.image_label.setText("")
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u5f00\u56fe\u7247", None)
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "\u6253\u5f00\u89c6\u9891", None)
        )
        self.pushButton_3.setText(
            QCoreApplication.translate(
                "MainWindow", "\u6253\u5f00\u6444\u50cf\u5934", None
            )
        )
        self.groupBox.setTitle(
            QCoreApplication.translate(
                "MainWindow", "\u7f6e\u4fe1\u5ea6\u9608\u503c\uff08conf\uff09", None
            )
        )
        self.label.setText(
            QCoreApplication.translate(
                "MainWindow", "\u5f53\u524d\u503c\uff1a0.25", None
            )
        )
        self.menuFile.setTitle(
            QCoreApplication.translate("MainWindow", "\u6587\u4ef6(&F)", None)
        )
        self.menuHelp.setTitle(
            QCoreApplication.translate("MainWindow", "\u5e2e\u52a9(&H)", None)
        )
        self.menuOption.setTitle(
            QCoreApplication.translate("MainWindow", "\u9009\u9879(&O)", None)
        )

    # retranslateUi
