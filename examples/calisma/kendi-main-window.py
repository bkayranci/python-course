from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_KendiEkranim import Ui_MainWindow
import sys

app = QApplication(sys.argv)

mw = QMainWindow()

ui = Ui_MainWindow()
ui.setupUi(mw)

def yazdir():
    print(ui.txtAd.text())

ui.btnYazdir.clicked.connect(yazdir)
mw.show()

sys.exit(app.exec_())
