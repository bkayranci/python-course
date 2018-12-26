from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_KendiEkranim import Ui_MainWindow
import sys


class KendiSinifim(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = KendiSinifim()
    mw.show()

    sys.exit(app.exec_())
