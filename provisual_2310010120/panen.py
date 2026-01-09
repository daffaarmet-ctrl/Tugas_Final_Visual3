# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class panen(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        filenya = QFile('panen.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formpanen = muatfile.load(filenya,self)
        self.aksi = crud()

        self.isiKaryawan()

        self.HARGA_PER_KG = 10000  #harga
        self.formpanen.sbHasil.valueChanged.connect(self.hitungTotal)


        self.formpanen.btnSimpan.clicked.connect(self.simpanPanen)
        self.formpanen.btnUbah.clicked.connect(self.ubahPanen)
        self.formpanen.btnHapus.clicked.connect(self.hapusPanen)
        self.tampilDataPanen()
        self.formpanen.lineCari.textChanged.connect(self.cariDataPanen)

    def simpanPanen(self):
        if not self.formpanen.editID.text().strip():
            QMessageBox.information(None, "Informasi", "Id panen belum diisi")
            self.formpanen.editID.setFocus()

        elif self.formpanen.sbHasil.value() == 0:
            QMessageBox.information(None, "Informasi", "Hasil panen tidak boleh 0")
            self.formpanen.sbHasil.setFocus()

        else:
            idpn = self.formpanen.editID.text()
            idkr = self.formpanen.cmbKaryawan.currentData()
            tgl = self.formpanen.datePanen.date().toString("yyyy-MM-dd")
            hasil = self.formpanen.sbHasil.value()
            total = self.formpanen.editTotal.text()

            self.aksi.tambahPanen(idpn, idkr, tgl, hasil, total)
            self.tampilDataPanen()
            QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def ubahPanen(self):
        idpn = self.formpanen.editID.text()
        idkr = self.formpanen.cmbKaryawan.currentData()
        tgl = self.formpanen.datePanen.date().toString("yyyy-MM-dd")
        hasil = self.formpanen.sbHasil.value()
        total = self.formpanen.editTotal.text()

        self.aksi.ubahPanen(idpn, idkr, tgl, hasil, total)
        self.tampilDataPanen()



    def hapusPanen(self):
        pesan = QMessageBox.information(
            None,
            "Informasi",
            "Apakah yakin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
        )

        if pesan == QMessageBox.Yes:
            idpn = self.formpanen.editID.text()
            self.aksi.hapusPanen(idpn,)
            self.tampilDataPanen()
        else:
            pass

    def tampilDataPanen(self):
        self.formpanen.tblPanen.setRowCount(0)
        data = self.aksi.dataPanen()

        for i, baris in enumerate(data):
            self.formpanen.tblPanen.insertRow(i)
            self.formpanen.tblPanen.setItem(i, 0, QTableWidgetItem(str(baris["id_panen"])))
            self.formpanen.tblPanen.setItem(i, 1, QTableWidgetItem(str(baris["nama_karyawan"])))
            self.formpanen.tblPanen.setItem(i, 2, QTableWidgetItem(str(baris["tanggal_panen"])))
            self.formpanen.tblPanen.setItem(i, 3, QTableWidgetItem(str(baris["hasil_panen"])))
            self.formpanen.tblPanen.setItem(i, 4, QTableWidgetItem(str(baris["total_panen"])))


    def cariDataPanen(self):
        varCari = self.formpanen.lineCari.text()
        self.formpanen.tblPanen.setRowCount(0)
        data = self.aksi.filterPanen(varCari)

        for i, baris in enumerate(data):
            self.formpanen.tblPanen.insertRow(i)
            self.formpanen.tblPanen.setItem(i, 0, QTableWidgetItem(str(baris["id_panen"])))
            self.formpanen.tblPanen.setItem(i, 1, QTableWidgetItem(str(baris["nama_karyawan"])))
            self.formpanen.tblPanen.setItem(i, 2, QTableWidgetItem(str(baris["tanggal_panen"])))
            self.formpanen.tblPanen.setItem(i, 3, QTableWidgetItem(str(baris["hasil_panen"])))
            self.formpanen.tblPanen.setItem(i, 4, QTableWidgetItem(str(baris["total_panen"])))


    def hitungTotal(self):
        hasil = self.formpanen.sbHasil.value()
        total = hasil * self.HARGA_PER_KG
        self.formpanen.editTotal.setText(str(total))


    def isiKaryawan(self):
        aksi = self.aksi.koneksi.cursor()
        aksi.execute("SELECT id_karyawan, nama_karyawan FROM data_karyawan")
        hasil = aksi.fetchall()

        self.formpanen.cmbKaryawan.clear()

        for idp, nama in hasil:
            self.formpanen.cmbKaryawan.addItem(nama, idp)

        aksi.close()


