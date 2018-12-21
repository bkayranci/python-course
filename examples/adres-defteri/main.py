from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
from Ui_adresdefteri import Ui_MainWindow

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QModelIndex
from Ui_duzenleme import Ui_Dialog

import sys
import csv



duzenleme = None
class Duzenleme(QDialog, Ui_Dialog):
    kisi = None
    def __init__(self, kisi):
        super(Duzenleme, self).__init__()
        self.setupUi(self)
        self.kisi = kisi
        self.txtAd.setText(kisi["ad"])
        self.txtSoyad.setText(kisi["soyad"])
        self.txtTelefon.setText(kisi["telefon"])
        self.accepted.connect(self.ekleme)
        self.rejected.connect(self.iptal)

    def ekleme(self):
        self.kisi["ad"] = self.txtAd.text()
        self.kisi["soyad"] = self.txtSoyad.text()
        self.kisi["telefon"] = self.txtTelefon.text()
        self.close()

    def iptal(self):
        self.close()

class AdresDefteri(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AdresDefteri, self).__init__()
        self.listem = []
        
        
        self.setupUi(self)
        self.oku()
        self.btnEkle.clicked.connect(self.ekleme)
        self.listView.clicked.connect(self.secildi)

    def secildi(self, secilen : QModelIndex):
        kisi = self.listem[secilen.row()]
        global duzenleme
        duzenleme = Duzenleme(kisi)
        duzenleme.exec_()
        self.dosyayaYaz()
        self.listview_doldur()
    
    def oku(self):
    
        with open('kisiler.csv', newline='') as csvfile:
            yazici = csv.DictReader(csvfile, delimiter=',',fieldnames=['ad', 'soyad', 'telefon'])
            for kisi in yazici:
                self.listem.append(kisi)
            if len(self.listem) == 0:
                self.listem.append({
                    'ad': 'ad',
                    'soyad': 'soyad',
                    'telefon': 'telefon'
                })

            self.listview_doldur()
    
    def listview_doldur(self):
        
        
        model = QStandardItemModel()
        for kisi in self.listem:
            item = QStandardItem()
            item.setText(kisi["ad"])
            item.setEditable(False)
            model.appendRow(item)

        
        
        self.listView.setModel(model)
        

    def ekleme(self):
        self.listem.append({
                'ad': self.txtAd.text(),
                'soyad': self.txtSoyad.text(),
                'telefon': self.txtTelefon.text()
            })
        self.dosyayaYaz()
        self.listview_doldur()


    def dosyayaYaz(self):
        with open('kisiler.csv', 'w') as csvfile:
            yazici = csv.DictWriter(csvfile, 
            fieldnames=['ad', 'soyad', 'telefon'])
            if len(self.listem) == 1:
                yazici.writeheader()
            for kisi in self.listem:
                yazici.writerow(kisi)
           

app = QApplication(sys.argv)

adresdefteri = AdresDefteri()
adresdefteri.show()

sys.exit(app.exec_())
