from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_adresdefteri import Ui_MainWindow
import sys
import csv

class AdresDefteri(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AdresDefteri, self).__init__()
        self.listem = []
        self.oku()
        
        self.setupUi(self)
        self.btnEkle.clicked.connect(self.ekleme)
    
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
        

    def ekleme(self):
        self.listem.append({
                'ad': self.txtAd.text(),
                'soyad': self.txtSoyad.text(),
                'telefon': self.txtTelefon.text()
            })
        self.dosyayaYaz()


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
