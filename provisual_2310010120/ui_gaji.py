# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gaji.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(747, 632)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 40, 481, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(80, 110, 481, 171))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDPanenLabel = QLabel(self.formLayoutWidget)
        self.iDPanenLabel.setObjectName(u"iDPanenLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDPanenLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.namaKaryawanLabel = QLabel(self.formLayoutWidget)
        self.namaKaryawanLabel.setObjectName(u"namaKaryawanLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaKaryawanLabel)

        self.cmbKaryawan = QComboBox(self.formLayoutWidget)
        self.cmbKaryawan.setObjectName(u"cmbKaryawan")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cmbKaryawan)

        self.tanggalGajiLabel = QLabel(self.formLayoutWidget)
        self.tanggalGajiLabel.setObjectName(u"tanggalGajiLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tanggalGajiLabel)

        self.dateGaji = QDateEdit(self.formLayoutWidget)
        self.dateGaji.setObjectName(u"dateGaji")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dateGaji)

        self.kategoriPembayaranLabel = QLabel(self.formLayoutWidget)
        self.kategoriPembayaranLabel.setObjectName(u"kategoriPembayaranLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.kategoriPembayaranLabel)

        self.cmbKategori = QComboBox(self.formLayoutWidget)
        self.cmbKategori.addItem("")
        self.cmbKategori.addItem("")
        self.cmbKategori.addItem("")
        self.cmbKategori.setObjectName(u"cmbKategori")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbKategori)

        self.jumlahGajiLabel = QLabel(self.formLayoutWidget)
        self.jumlahGajiLabel.setObjectName(u"jumlahGajiLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.jumlahGajiLabel)

        self.editGaji = QLineEdit(self.formLayoutWidget)
        self.editGaji.setObjectName(u"editGaji")
        self.editGaji.setReadOnly(False)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editGaji)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(230, 290, 331, 31))
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

        self.tblGaji = QTableWidget(Form)
        if (self.tblGaji.columnCount() < 5):
            self.tblGaji.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblGaji.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblGaji.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblGaji.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblGaji.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblGaji.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblGaji.setObjectName(u"tblGaji")
        self.tblGaji.setGeometry(QRect(80, 390, 631, 192))
        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(80, 350, 481, 28))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"KELOLA DATA GAJI", None))
        self.iDPanenLabel.setText(QCoreApplication.translate("Form", u"ID Panen", None))
        self.namaKaryawanLabel.setText(QCoreApplication.translate("Form", u"Nama Karyawan", None))
        self.tanggalGajiLabel.setText(QCoreApplication.translate("Form", u"Tanggal Gaji", None))
        self.kategoriPembayaranLabel.setText(QCoreApplication.translate("Form", u"Kategori Pembayaran", None))
        self.cmbKategori.setItemText(0, QCoreApplication.translate("Form", u"Bulanan", None))
        self.cmbKategori.setItemText(1, QCoreApplication.translate("Form", u"Mingguan", None))
        self.cmbKategori.setItemText(2, "")

        self.jumlahGajiLabel.setText(QCoreApplication.translate("Form", u"Jumlah Gaji", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        ___qtablewidgetitem = self.tblGaji.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Gaji", None));
        ___qtablewidgetitem1 = self.tblGaji.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama Karyawan", None));
        ___qtablewidgetitem2 = self.tblGaji.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Tanggal Gaji", None));
        ___qtablewidgetitem3 = self.tblGaji.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Kategori Pembayaran", None));
        ___qtablewidgetitem4 = self.tblGaji.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Jumlah Gaji", None));
    # retranslateUi

