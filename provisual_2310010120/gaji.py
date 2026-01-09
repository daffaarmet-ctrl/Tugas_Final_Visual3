# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class gaji(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        filenya = QFile('gaji.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formgaji = muatfile.load(filenya, self)
        self.aksi = crud()

        self.isiKaryawan()

        self.HARGA_PER_KG = 10000
        self.formgaji.cmbKaryawan.currentIndexChanged.connect(self.hitungGaji)
        self.formgaji.cmbKategori.currentIndexChanged.connect(self.hitungGaji)
        self.formgaji.dateGaji.dateChanged.connect(self.hitungGaji)


        self.formgaji.btnSimpan.clicked.connect(self.simpanGaji)
        self.formgaji.btnUbah.clicked.connect(self.ubahGaji)
        self.formgaji.btnHapus.clicked.connect(self.hapusGaji)

        self.tampilDataGaji()
        self.formgaji.lineCari.textChanged.connect(self.cariDataGaji)


    def simpanGaji(self):
        if not self.formgaji.editID.text().strip():
            QMessageBox.information(None, "Informasi", "Id gaji belum diisi")
            self.formgaji.editID.setFocus()

        else:
            idg = self.formgaji.editID.text()
            idkr = self.formgaji.cmbKaryawan.currentData()
            tgl = self.formgaji.dateGaji.date().toString("yyyy-MM-dd")
            kategori = self.formgaji.cmbKategori.currentText()
            gaji = self.formgaji.editGaji.text()

            self.aksi.tambahGaji(idg, idkr, tgl, kategori, gaji)
            self.tampilDataGaji()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def ubahGaji(self):
        idg = self.formgaji.editID.text()
        idkr = self.formgaji.cmbKaryawan.currentData()
        tgl = self.formgaji.dateGaji.date().toString("yyyy-MM-dd")
        kategori = self.formgaji.cmbKategori.currentText()

        # hitung ulang gaji (biar pasti benar)
        self.hitungGaji()
        gaji = self.formgaji.editGaji.text()

        self.aksi.ubahGaji(idg, idkr, tgl, kategori, gaji)
        self.tampilDataGaji()




    def hapusGaji(self):
        pesan = QMessageBox.information(
            None,
            "Informasi",
            "Apakah yakin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if pesan == QMessageBox.Yes:
            idpn = self.formgaji.editID.text()
            self.aksi.hapusGaji(idpn,)
            self.tampilDataGaji()
        else:
            pass

    def tampilDataGaji(self):
        self.formgaji.tblGaji.setRowCount(0)
        data = self.aksi.dataGaji()

        for i, baris in enumerate(data):
            self.formgaji.tblGaji.insertRow(i)
            self.formgaji.tblGaji.setItem(i, 0, QTableWidgetItem(str(baris["id_gaji"])))
            self.formgaji.tblGaji.setItem(i, 1, QTableWidgetItem(str(baris["nama_karyawan"])))
            self.formgaji.tblGaji.setItem(i, 2, QTableWidgetItem(str(baris["tanggal_gaji"])))
            self.formgaji.tblGaji.setItem(i, 3, QTableWidgetItem(str(baris["kategori"])))
            self.formgaji.tblGaji.setItem(i, 4, QTableWidgetItem(str(baris["jumlah_gaji"])))


    def cariDataGaji(self):
        varCari = self.formgaji.lineCari.text()
        self.formgaji.tblGaji.setRowCount(0)
        data = self.aksi.filterGaji(varCari)

        for i, baris in enumerate(data):
            self.formgaji.tblGaji.insertRow(i)
            self.formgaji.tblGaji.setItem(i, 0, QTableWidgetItem(str(baris["id_gaji"])))
            self.formgaji.tblGaji.setItem(i, 1, QTableWidgetItem(str(baris["nama_karyawan"])))
            self.formgaji.tblGaji.setItem(i, 2, QTableWidgetItem(str(baris["tanggal_gaji"])))
            self.formgaji.tblGaji.setItem(i, 3, QTableWidgetItem(str(baris["kategori"])))
            self.formgaji.tblGaji.setItem(i, 4, QTableWidgetItem(str(baris["jumlah_gaji"])))

    def hitungGaji(self):
        idkr = self.formgaji.cmbKaryawan.currentData()
        kategori = self.formgaji.cmbKategori.currentText()
        tanggal = self.formgaji.dateGaji.date().toString("yyyy-MM-dd")

        if idkr is None:
            return

        if kategori == "Mingguan":
            total = self.aksi.totalPanenMingguan(idkr, tanggal)
        else:   # Bulanan
            total = self.aksi.totalPanenBulanan(idkr, tanggal)

        gaji = total
        self.formgaji.editGaji.setText(str(gaji))



    def isiKaryawan(self):
        aksi = self.aksi.koneksi.cursor()
        aksi.execute("SELECT id_karyawan, nama_karyawan FROM data_karyawan")
        hasil = aksi.fetchall()

        self.formgaji.cmbKaryawan.clear()

        for idp, nama in hasil:
            self.formgaji.cmbKaryawan.addItem(nama, idp)

        aksi.close()


