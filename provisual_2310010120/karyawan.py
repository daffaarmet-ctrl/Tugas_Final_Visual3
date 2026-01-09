# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class karyawan(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        filenya = QFile('karyawan.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formkaryawan = muatfile.load(filenya,self)
        self.aksi = crud()
        self.formkaryawan.sbUmur.setMinimum(20)


        self.formkaryawan.btnSimpan.clicked.connect(self.simpanKaryawan)
        self.formkaryawan.btnUbah.clicked.connect(self.ubahKaryawan)
        self.formkaryawan.btnHapus.clicked.connect(self.hapusKaryawan)
        self.tampilDataKaryawan()
        self.formkaryawan.lineCari.textChanged.connect(self.cariDataKaryawan)

    def simpanKaryawan(self):
        if not self.formkaryawan.editID.text().strip():
            QMessageBox.information(None, "Informasi", "Id Karyawan belum diisi")
            self.formkaryawan.editID.setFocus()

        elif not self.formkaryawan.editNama.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Karyawan belum diisi")
            self.formkaryawan.editNama.setFocus()

        elif not self.formkaryawan.editTelp.text().strip():
            QMessageBox.information(None, "Informasi", "No Telepon belum diisi")
            self.formkaryawan.editTelp.setFocus()

        else:
            id = self.formkaryawan.editID.text()
            nama = self.formkaryawan.editNama.text()
            alamat = self.formkaryawan.editAlamat.text()
            umur = self.formkaryawan.sbUmur.value()
            telepon = self.formkaryawan.editTelp.text()

            self.aksi.tambahKaryawan(id, nama, alamat, umur, telepon)
            self.tampilDataKaryawan()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def ubahKaryawan(self):
        id = self.formkaryawan.editID.text()
        nama = self.formkaryawan.editNama.text()
        alamat = self.formkaryawan.editAlamat.text()
        umur = self.formkaryawan.sbUmur.value()
        telepon = self.formkaryawan.editTelp.text()
        self.aksi.ubahKaryawan(id, nama, alamat, umur, telepon)
        self.tampilDataKaryawan()


    def hapusKaryawan(self):
        pesan = QMessageBox.information(
            None,
            "Informasi",
            "Apakah yakin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if pesan == QMessageBox.Yes:
            id = self.formkaryawan.editID.text()
            self.aksi.hapusKaryawan(id,)
            self.tampilDataKaryawan()
        else:
            pass

    def tampilDataKaryawan(self):
        self.formkaryawan.tblKaryawan.setRowCount(0)
        data = self.aksi.dataKaryawan()
        for i, baris in enumerate(data):
            self.formkaryawan.tblKaryawan.insertRow(i)
            self.formkaryawan.tblKaryawan.setItem(i, 0, QTableWidgetItem(str(baris["id_karyawan"])))
            self.formkaryawan.tblKaryawan.setItem(i, 1, QTableWidgetItem(str(baris["nama_karyawan"])))
            self.formkaryawan.tblKaryawan.setItem(i, 2, QTableWidgetItem(str(baris["alamat"])))
            self.formkaryawan.tblKaryawan.setItem(i, 3, QTableWidgetItem(str(baris["umur"])))
            self.formkaryawan.tblKaryawan.setItem(i, 4, QTableWidgetItem(str(baris["no_telp"])))



    def cariDataKaryawan(self):
        varCari = self.formkaryawan.lineCari.text()
        self.formkaryawan.tblKaryawan.setRowCount(0)
        data = self.aksi.filterKaryawan(varCari)
        for i, baris in enumerate(data):
            self.formkaryawan.tblKaryawan.insertRow(i)
            self.formkaryawan.tblKaryawan.setItem(i, 0, QTableWidgetItem(str(baris["id_karyawan"])))
            self.formkaryawan.tblKaryawan.setItem(i, 1, QTableWidgetItem(str(baris["nama_karyawan"])))
            self.formkaryawan.tblKaryawan.setItem(i, 2, QTableWidgetItem(str(baris["alamat"])))
            self.formkaryawan.tblKaryawan.setItem(i, 3, QTableWidgetItem(str(baris["umur"])))
            self.formkaryawan.tblKaryawan.setItem(i, 4, QTableWidgetItem(str(baris["no_telp"])))



