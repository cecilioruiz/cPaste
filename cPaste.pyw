# -*- coding: utf-8 -*-

__author__ = 'cecilio'
__appName__ = 'cPaste'

from PyQt4 import QtCore, QtGui
from uid import ui_ventana
import sys

class cpp(QtGui.QMainWindow, ui_ventana.Ui_MainWindow):
    def __init__(self, parent = None):
        super(cpp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.__contador = 0
        self.__copia = True # Copia = True copia al portapapeles. False = elimina botón.
        self.mas.clicked.connect(self.agregar)
        self.menos.clicked.connect(self.elimina)

    def agregar(self):
        """Agrega botón con texto."""
        text, ok = QtGui.QInputDialog.getText(self, 'Nuevo','Texto:')
        if ok:
            #self.pushButton.setText(str(text))
            self.__contador +=1
            nombre = str("p%i" %self.__contador)
            self.p1 = QtGui.QPushButton(self.centralwidget)
            self.p1.setMinimumSize(QtCore.QSize(0, 30))
            self.p1.setMaximumSize(QtCore.QSize(1000, 33))
            self.p1.setObjectName(nombre)
            self.p1.setText(str(text))
            self.p1.setStyleSheet("")
            self.p1.setToolTip(QtCore.QString("Pulsa para llevar al portapapeles. (Ctrl+V pega)"))
            self.hbt.addWidget(self.p1)
            self.p1.clicked.connect(self.pega)


    def pega(self):
        """Pega al portapapeles. Según botón pulsado"""
        boton = self.sender()
        if self.__copia:
            s = '%s' % str(boton.text())
            #print s
            clipboard = QtGui.QApplication.clipboard()
            clipboard.setText(s)
        else:
            self.hbt.removeWidget(boton)
            boton.deleteLater()
            self.cambiaEstado()

    def cambiaEstado(self):
        """ Cabia de copiar a borrar."""
        self.__copia = not self.__copia
        if self.__copia: # Ahora es modo de copiar.
            self.menos.setStyleSheet("")
        else: # Ahora es modo de eliminar.
            self.menos.setStyleSheet("background-color: red")


    def elimina(self):
        self.cambiaEstado()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    cpv = cpp()
    cpv.show()
    sys.exit(app.exec_())