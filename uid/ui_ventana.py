# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\AAA_PyQt\cPaste\uid\ventana.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(499, 50)
        MainWindow.setMinimumSize(QtCore.QSize(0, 35))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 50))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tbotones = QtGui.QHBoxLayout()
        self.tbotones.setSpacing(3)
        self.tbotones.setObjectName(_fromUtf8("tbotones"))
        self.mas = QtGui.QPushButton(self.centralwidget)
        self.mas.setMinimumSize(QtCore.QSize(0, 30))
        self.mas.setMaximumSize(QtCore.QSize(25, 30))
        self.mas.setObjectName(_fromUtf8("mas"))
        self.tbotones.addWidget(self.mas)
        self.menos = QtGui.QPushButton(self.centralwidget)
        self.menos.setMinimumSize(QtCore.QSize(25, 30))
        self.menos.setMaximumSize(QtCore.QSize(25, 30))
        self.menos.setObjectName(_fromUtf8("menos"))
        self.tbotones.addWidget(self.menos)
        self.horizontalLayout.addLayout(self.tbotones)
        self.hbt = QtGui.QHBoxLayout()
        self.hbt.setContentsMargins(5, -1, -1, -1)
        self.hbt.setSpacing(5)
        self.hbt.setObjectName(_fromUtf8("hbt"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hbt.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.hbt)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "copia y pega", None))
        self.mas.setToolTip(_translate("MainWindow", "Agregar boton", None))
        self.mas.setText(_translate("MainWindow", "+", None))
        self.menos.setToolTip(_translate("MainWindow", "Eliminar boton", None))
        self.menos.setText(_translate("MainWindow", "-", None))

