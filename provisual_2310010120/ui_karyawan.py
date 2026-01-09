# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'karyawan.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(633, 635)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 50, 461, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(70, 110, 461, 171))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDKaryawanLabel = QLabel(self.formLayoutWidget)
        self.iDKaryawanLabel.setObjectName(u"iDKaryawanLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDKaryawanLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.namaKaryawanLabel = QLabel(self.formLayoutWidget)
        self.namaKaryawanLabel.setObjectName(u"namaKaryawanLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaKaryawanLabel)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.alamatLabel = QLabel(self.formLayoutWidget)
        self.alamatLabel.setObjectName(u"alamatLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.alamatLabel)

        self.editAlamat = QLineEdit(self.formLayoutWidget)
        self.editAlamat.setObjectName(u"editAlamat")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editAlamat)

        self.umurLabel = QLabel(self.formLayoutWidget)
        self.umurLabel.setObjectName(u"umurLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.umurLabel)

        self.sbUmur = QSpinBox(self.formLayoutWidget)
        self.sbUmur.setObjectName(u"sbUmur")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.sbUmur)

        self.noTelpLabel = QLabel(self.formLayoutWidget)
        self.noTelpLabel.setObjectName(u"noTelpLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.noTelpLabel)

        self.editTelp = QLineEdit(self.formLayoutWidget)
        self.editTelp.setObjectName(u"editTelp")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editTelp)

        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(70, 350, 451, 28))
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(180, 300, 341, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnSimpan = QPushButton(self.horizontalLayoutWidget)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.horizontalLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(self.horizontalLayoutWidget)
        self.btnUbah.setObjectName(u"btnUbah")

        self.horizontalLayout.addWidget(self.btnUbah)

        self.btnHapus = QPushButton(self.horizontalLayoutWidget)
        self.btnHapus.setObjectName(u"btnHapus")

        self.horizontalLayout.addWidget(self.btnHapus)

        self.tblKaryawan = QTableWidget(Form)
        if (self.tblKaryawan.columnCount() < 5):
            self.tblKaryawan.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblKaryawan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblKaryawan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblKaryawan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblKaryawan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblKaryawan.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblKaryawan.setObjectName(u"tblKaryawan")
        self.tblKaryawan.setGeometry(QRect(70, 390, 501, 192))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"KELOLA DATA KARYAWAN", None))
        self.iDKaryawanLabel.setText(QCoreApplication.translate("Form", u"ID Karyawan", None))
        self.namaKaryawanLabel.setText(QCoreApplication.translate("Form", u"Nama Karyawan", None))
        self.alamatLabel.setText(QCoreApplication.translate("Form", u"Alamat", None))
        self.umurLabel.setText(QCoreApplication.translate("Form", u"Umur", None))
        self.noTelpLabel.setText(QCoreApplication.translate("Form", u"No Telp", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        ___qtablewidgetitem = self.tblKaryawan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Karyawan", None));
        ___qtablewidgetitem1 = self.tblKaryawan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem2 = self.tblKaryawan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Alamat", None));
        ___qtablewidgetitem3 = self.tblKaryawan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Umur", None));
        ___qtablewidgetitem4 = self.tblKaryawan.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"No Telp", None));
    # retranslateUi

