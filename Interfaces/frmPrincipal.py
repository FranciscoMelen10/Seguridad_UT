import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi

class Form_Principal(QtWidgets.QMainWindow):
    def __init__(self):
        super(Form_Principal,self).__init__()
        loadUi("./VentanaPrincipal.ui",self)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    aplicacion = Form_Principal()
    aplicacion.show()
    app.exec()