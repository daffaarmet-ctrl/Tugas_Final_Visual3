# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panen.ui'
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
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(709, 627)
        self.tblPanen = QTableWidget(Form)
        if (self.tblPanen.columnCount() < 5):
            self.tblPanen.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblPanen.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblPanen.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblPanen.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblPanen.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblPanen.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tblPanen.setObjectName(u"tblPanen")
        self.tblPanen.setGeometry(QRect(50, 410, 621, 192))
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 110, 491, 172))
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

        self.tanggalPanenLabel = QLabel(self.formLayoutWidget)
        self.tanggalPanenLabel.setObjectName(u"tanggalPanenLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tanggalPanenLabel)

        self.datePanen = QDateEdit(self.formLayoutWidget)
        self.datePanen.setObjectName(u"datePanen")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.datePanen)

        self.hasilPanenLabel = QLabel(self.formLayoutWidget)
        self.hasilPanenLabel.setObjectName(u"hasilPanenLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.hasilPanenLabel)

        self.sbHasil = QSpinBox(self.formLayoutWidget)
        self.sbHasil.setObjectName(u"sbHasil")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.sbHasil)

        self.totalPanenRpLabel = QLabel(self.formLayoutWidget)
        self.totalPanenRpLabel.setObjectName(u"totalPanenRpLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.totalPanenRpLabel)

        self.editTotal = QLineEdit(self.formLayoutWidget)
        self.editTotal.setObjectName(u"editTotal")
        self.editTotal.setEnabled(True)
        self.editTotal.setReadOnly(False)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editTotal)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 491, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(170, 300, 381, 41))
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

        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(50, 360, 501, 28))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tblPanen.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Panen", None));
        ___qtablewidgetitem1 = self.tblPanen.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"ID karyawan", None));
        ___qtablewidgetitem2 = self.tblPanen.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Tanggal Panen", None));
        ___qtablewidgetitem3 = self.tblPanen.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Hasil Panen", None));
        ___qtablewidgetitem4 = self.tblPanen.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Total Panen", None));
        self.iDPanenLabel.setText(QCoreApplication.translate("Form", u"ID Panen", None))
        self.namaKaryawanLabel.setText(QCoreApplication.translate("Form", u"Nama Karyawan", None))
        self.tanggalPanenLabel.setText(QCoreApplication.translate("Form", u"Tanggal Panen", None))
        self.hasilPanenLabel.setText(QCoreApplication.translate("Form", u"Hasil Panen (Kg)", None))
        self.totalPanenRpLabel.setText(QCoreApplication.translate("Form", u"Total Panen (Rp)", None))
        self.label.setText(QCoreApplication.translate("Form", u"KELOLA DATA PANEN", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"Simpan", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"Ubah", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"Hapus", None))
    # retranslateUi

