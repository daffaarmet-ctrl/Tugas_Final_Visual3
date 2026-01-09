# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class inventory(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        filenya = QFile('inventory.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.forminventory = muatfile.load(filenya,self)
        self.aksi = crud()


        self.forminventory.btnSimpan.clicked.connect(self.simpanInventory)
        self.forminventory.btnUbah.clicked.connect(self.ubahInventory)
        self.forminventory.btnHapus.clicked.connect(self.hapusInventory)
        self.tampilDataInventory()
        self.forminventory.lineCari.textChanged.connect(self.cariDataInventory)

    def simpanInventory(self):
        if not self.forminventory.editID.text().strip():
            QMessageBox.information(None, "Informasi", "Id Barang belum diisi")
            self.forminventory.editID.setFocus()

        elif not self.forminventory.editNama.text().strip():
            QMessageBox.information(None, "Informasi", "Nama Barang belum diisi")
            self.forminventoryeditNama.setFocus()

        elif not self.forminventory.sbJum.value():
            QMessageBox.information(None, "Informasi", "Jumlah tidak boleh 0")
            self.forminventory.sbJum.setFocus()

        else:
            id = self.forminventory.editID.text()
            nama = self.forminventory.editNama.text()
            kategori = self.forminventory.cmbKategori.currentText()
            satuan = self.forminventory.cmbSatuan.currentText()
            jumlah = self.forminventory.sbJum.value()

            self.aksi.tambahInventory(id, nama, kategori, satuan, jumlah)
            self.tampilDataInventory()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def ubahInventory(self):
        id = self.forminventory.editID.text()
        nama = self.forminventory.editNama.text()
        kategori = self.forminventory.cmbKategori.currentText()
        satuan = self.forminventory.cmbSatuan.currentText()
        jumlah = self.forminventory.sbJum.value()

        self.aksi.ubahInventory(id, nama, kategori, satuan, jumlah)
        self.tampilDataInventory()


    def hapusInventory(self):
        pesan = QMessageBox.information(
            None,
            "Informasi",
            "Apakah yakin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if pesan == QMessageBox.Yes:
            id = self.forminventory.editID.text()
            self.aksi.hapusInventory(id,)
            self.tampilDataInventory()
        else:
            pass

    def tampilDataInventory(self):
        self.forminventory.tblInventory.setRowCount(0)
        data = self.aksi.dataInventory()
        for i, baris in enumerate(data):
            self.forminventory.tblInventory.insertRow(i)
            self.forminventory.tblInventory.setItem(i, 0, QTableWidgetItem(str(baris["id_barang"])))
            self.forminventory.tblInventory.setItem(i, 1, QTableWidgetItem(str(baris["nama_barang"])))
            self.forminventory.tblInventory.setItem(i, 2, QTableWidgetItem(str(baris["kategori"])))
            self.forminventory.tblInventory.setItem(i, 3, QTableWidgetItem(str(baris["satuan"])))
            self.forminventory.tblInventory.setItem(i, 4, QTableWidgetItem(str(baris["jumlah"])))


    def cariDataInventory(self):
        varCari = self.forminventory.lineCari.text()
        self.forminventory.tblInventory.setRowCount(0)
        data = self.aksi.filterInventory(varCari)

        for i, baris in enumerate(data):
            self.forminventory.tblInventory.insertRow(i)
            self.forminventory.tblInventory.setItem(i, 0, QTableWidgetItem(str(baris["id_barang"])))
            self.forminventory.tblInventory.setItem(i, 1, QTableWidgetItem(str(baris["nama_barang"])))
            self.forminventory.tblInventory.setItem(i, 2, QTableWidgetItem(str(baris["kategori"])))
            self.forminventory.tblInventory.setItem(i, 3, QTableWidgetItem(str(baris["satuan"])))
            self.forminventory.tblInventory.setItem(i, 4, QTableWidgetItem(str(baris["jumlah"])))




