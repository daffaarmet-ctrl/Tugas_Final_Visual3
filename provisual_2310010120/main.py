# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from karyawan import karyawan
from inventory import inventory
from panen import panen
from gaji import gaji


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya = QFile('form.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formutama = muatfile.load(filenya,self)
        self.resize(self.formutama.size())
        self.setMenuBar(self.formutama.menuBar())
        self.formutama.actionKARYAWAN.triggered.connect(self.bukakaryawan)
        self.formutama.actionINVENTORY.triggered.connect(self.bukainventory)
        self.formutama.actionPANEN.triggered.connect(self.bukapanen)
        self.formutama.actionGAJI.triggered.connect(self.bukagaji)


    def bukakaryawan(self):
        self.formkaryawan = karyawan()
        self.formkaryawan.show()

    def bukainventory(self):
        self.forminventory = inventory()
        self.forminventory.show()


    def bukapanen(self):
        self.formpanen = panen()
        self.formpanen.show()

    def bukagaji(self):
        self.formgaji = gaji()
        self.formgaji.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
