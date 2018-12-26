from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_KendiEkranim import Ui_MainWindow
import sys

def yazdir():
    print("yazildim")

class KendiSinifim(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnYazdir.clicked.connect(self.yazdir)
    
    def yazdir(self):
        print("sinifin icinden yazildim")


app = QApplication(sys.argv)

mw = KendiSinifim()
mw.show()

sys.exit(app.exec_())
