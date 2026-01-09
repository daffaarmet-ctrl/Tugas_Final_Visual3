# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inventory.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(637, 658)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(80, 120, 451, 171))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDBarangLabel = QLabel(self.formLayoutWidget)
        self.iDBarangLabel.setObjectName(u"iDBarangLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDBarangLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.namaBarangLabel = QLabel(self.formLayoutWidget)
        self.namaBarangLabel.setObjectName(u"namaBarangLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaBarangLabel)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.kategoriLabel = QLabel(self.formLayoutWidget)
        self.kategoriLabel.setObjectName(u"kategoriLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.kategoriLabel)

        self.cmbKategori = QComboBox(self.formLayoutWidget)
        self.cmbKategori.addItem("")
        self.cmbKategori.addItem("")
        self.cmbKategori.addItem("")
        self.cmbKategori.setObjectName(u"cmbKategori")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.cmbKategori)

        self.satuanLabel = QLabel(self.formLayoutWidget)
        self.satuanLabel.setObjectName(u"satuanLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.satuanLabel)

        self.cmbSatuan = QComboBox(self.formLayoutWidget)
        self.cmbSatuan.addItem("")
        self.cmbSatuan.addItem("")
        self.cmbSatuan.addItem("")
        self.cmbSatuan.setObjectName(u"cmbSatuan")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cmbSatuan)

        self.jumlahLabel = QLabel(self.formLayoutWidget)
        self.jumlahLabel.setObjectName(u"jumlahLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.jumlahLabel)

        self.sbJum = QSpinBox(self.formLayoutWidget)
        self.sbJum.setObjectName(u"sbJum")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.sbJum)

        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(180, 320, 351, 41))
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

        self.tblInventory = QTableWidget(Form)
        if (self.tblInventory.columnCount() < 4):
            self.tblInventory.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblInventory.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tblInventory.setObjectName(u"tblInventory")
        self.tblInventory.setGeometry(QRect(70, 430, 501, 192))
        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(70, 390, 461, 28))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 60, 451, 20))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDBarangLabel.setText(QCoreApplication.translate("Form", u"ID Barang", None))
        self.namaBarangLabel.setText(QCoreApplication.translate("Form", u"Nama Barang", None))
        self.kategoriLabel.setText(QCoreApplication.translate("Form", u"Kategori", None))
        self.cmbKategori.setItemText(0, QCoreApplication.translate("Form", u"Pupuk", None))
        self.cmbKategori.setItemText(1, QCoreApplication.translate("Form", u"Peralatan", None))
        self.cmbKategori.setItemText(2, QCoreApplication.translate("Form", u"Obat", None))

        self.satuanLabel.setText(QCoreApplication.translate("Form", u"Satuan", None))
        self.cmbSatuan.setItemText(0, QCoreApplication.translate("Form", u"Kg", None))
        self.cmbSatuan.setItemText(1, QCoreApplication.translate("Form", u"Pcs", None))
        self.cmbSatuan.setItemText(2, QCoreApplication.translate("Form", u"Botol", None))

        self.jumlahLabel.setText(QCoreApplication.translate("Form", u"Jumlah", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
        ___qtablewidgetitem = self.tblInventory.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Barang", None));
        ___qtablewidgetitem1 = self.tblInventory.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem2 = self.tblInventory.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Kategori", None));
        ___qtablewidgetitem3 = self.tblInventory.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Jumlah", None));
        self.label.setText(QCoreApplication.translate("Form", u"KELOLA DATA INVENTORY", None))
    # retranslateUi

