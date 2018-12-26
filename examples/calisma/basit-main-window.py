from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)

mw = QMainWindow()
mw.setWindowTitle('selam')
mw.show()

sys.exit(app.exec_())
