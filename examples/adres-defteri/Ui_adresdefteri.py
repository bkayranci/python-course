# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/bkayranci/workspace/python/adres-defteri-sinif/adresdefteri.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(403, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 40, 331, 258))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.txtAd = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtAd.setObjectName("txtAd")
        self.gridLayout.addWidget(self.txtAd, 1, 1, 1, 1)
        self.btnEkle = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnEkle.setObjectName("btnEkle")
        self.gridLayout.addWidget(self.btnEkle, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.txtSoyad = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtSoyad.setObjectName("txtSoyad")
        self.gridLayout.addWidget(self.txtSoyad, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.txtTelefon = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.txtTelefon.setObjectName("txtTelefon")
        self.gridLayout.addWidget(self.txtTelefon, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Soyad"))
        self.btnEkle.setText(_translate("MainWindow", "Ekle"))
        self.label.setText(_translate("MainWindow", "Ad"))
        self.label_3.setText(_translate("MainWindow", "Telefon Numarası"))

