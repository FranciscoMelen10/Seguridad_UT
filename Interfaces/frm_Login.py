import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi

# La imagen en el Qt Densinger no la reconoce y es por eso que no aparece al ejecutar al programa
# Además esta sera una practica para usar el crud y los formulario en Qt Desinger




class Form_Estudiante(QtWidgets.QMainWindow):
    def __init__(self):
        super(Form_Estudiante,self).__init__()
        loadUi("./Login.ui",self)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    aplicacion = Form_Estudiante()
    aplicacion.show()
    app.exec()