# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/bkayranci/workspace/python/calisma/KendiEkranim.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(179, 176)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnYazdir = QtWidgets.QPushButton(self.centralwidget)
        self.btnYazdir.setGeometry(QtCore.QRect(30, 80, 111, 32))
        self.btnYazdir.setObjectName("btnYazdir")
        self.txtAd = QtWidgets.QLineEdit(self.centralwidget)
        self.txtAd.setGeometry(QtCore.QRect(30, 40, 113, 26))
        self.txtAd.setObjectName("txtAd")
        self.lblAd = QtWidgets.QLabel(self.centralwidget)
        self.lblAd.setGeometry(QtCore.QRect(30, 20, 57, 16))
        self.lblAd.setObjectName("lblAd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 179, 28))
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
        self.btnYazdir.setText(_translate("MainWindow", "Yazdır"))
        self.lblAd.setText(_translate("MainWindow", "Ad"))

