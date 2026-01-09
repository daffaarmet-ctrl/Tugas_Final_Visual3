# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        self.actionKARYAWAN = QAction(Main)
        self.actionKARYAWAN.setObjectName(u"actionKARYAWAN")
        self.actionINVENTORY = QAction(Main)
        self.actionINVENTORY.setObjectName(u"actionINVENTORY")
        self.actionPANEN = QAction(Main)
        self.actionPANEN.setObjectName(u"actionPANEN")
        self.actionGAJI = QAction(Main)
        self.actionGAJI.setObjectName(u"actionGAJI")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuKELOLA_MENU = QMenu(self.menubar)
        self.menuKELOLA_MENU.setObjectName(u"menuKELOLA_MENU")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuKELOLA_MENU.menuAction())
        self.menuKELOLA_MENU.addAction(self.actionKARYAWAN)
        self.menuKELOLA_MENU.addAction(self.actionINVENTORY)
        self.menuKELOLA_MENU.addAction(self.actionPANEN)
        self.menuKELOLA_MENU.addAction(self.actionGAJI)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.actionKARYAWAN.setText(QCoreApplication.translate("Main", u"KARYAWAN", None))
        self.actionINVENTORY.setText(QCoreApplication.translate("Main", u"INVENTORY", None))
        self.actionPANEN.setText(QCoreApplication.translate("Main", u"PANEN", None))
        self.actionGAJI.setText(QCoreApplication.translate("Main", u"GAJI", None))
        self.menuKELOLA_MENU.setTitle(QCoreApplication.translate("Main", u"KELOLA MENU", None))
    # retranslateUi

