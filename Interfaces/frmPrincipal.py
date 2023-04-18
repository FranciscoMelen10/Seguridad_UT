import sys
from datetime import datetime

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi

from Datos import dt_Usuario


class Form_Principal(QtWidgets.QMainWindow):
    def __init__(self):
        super(Form_Principal,self).__init__()
        loadUi("./VentanaPrincipal.ui",self)

        #Acciones de botones

        #Botones de Usuario
        self.bt_Guardar_Usuario.clicked.connect(self.guardarUsuario)
        #self.bt_Editar_Usuario.clicked.connect(self.editarUsuario)
        #self.bt_Eliminar_Usuario.clicked.connect(self.eliminiarUsuario)
        self.bt_Vaciar_Usuario.clicked.connect(self.limpiarCampos)

        '''#Botones de Rol
        self.bt_Guardar_Rol.clicked.connect(self.guardarRol)
        self.bt_Editar_Rol.clicked.connect(self.editarRol)
        self.bt_Eliminar_Rol.clicked.connect(self.eliminiarRol)
        self.bt_Vaciar_Rol.clicked.connect(self.limpiarCampos)

        #Botones de Opcion
        self.bt_Guardar_Opcion.clicked.connect(self.guardarOpcion)
        self.bt_Editar_Opcion.clicked.connect(self.editarOpcion)
        self.bt_Eliminar_Opcion.clicked.connect(self.eliminiarOpcion)
        self.bt_Vaciar_Opcion.clicked.connect(self.limpiarCampos)'''

        #Acciones de tabla

        #Usuarios
        self.llenarTablaUsuario(dt_Usuario.Dt_Usuarios.listarUsuarios())
        self.tb_Usuario.itemSelectionChanged.connect(self.obtenerDatosTablaUsuario)

    '''***********************************************  Funciones reutilizables   ******************************************'''

    def limpiarCampos(self):
        self.line_Usuario_Id.clear()
        self.line_Usuario_Nombre.clear()
        self.line_Usuario_Apellido.clear()
        self.line_Usuario_User.clear()
        self.line_Usuario_Password.clear()

        '''self.line_Rol_Id.clear()
        self.line_Rol.clear()
        self.line_Rol_Descripcion.clear()

        self.line_Opciones_Id.clear()
        self.line_Opciones.clear()
        self.line_Opciones_Descripcion.clear()'''

    def notifMensaje(self, indicador, resultado):
        if indicador == 1:
            QMessageBox.about(self, "Registrado", "Datos " + resultado + " Correctamente")
        else:
            QMessageBox.about(self, "Error", "Error de registros de datos")




        '''***********************************************  Usuario   ******************************************'''

    def guardarUsuario(self):


        try:
            # Tramsformar la fecha en formato "yyyy-MM-dd"
            #fechaTransformada = QDate.fromString(self.line_Usuario_Fecha.text(), '%d/%m/%Y')

            fecha = self.line_Usuario_Fecha.text()
            fecha_objeto = datetime.strptime(fecha, "%d/%m/%Y")
            fechaTransformada = fecha_objeto.strftime("%Y-%m-%d")

            print(fecha)


            print(fechaTransformada)

            if not self.line_Usuario_Nombre.text()== "" and not self.line_Usuario_Apellido.text()== "" and not self.line_Usuario_User.text()== "" and not self.line_Usuario_Password.text()== "" and not self.line_Usuario_Fecha.text()== "":
                self.indicador = 1  # Se coloca el 1 como modificador a la hora de entrar a la función de Notificación, en donde asegura que el usuario ingreso los datos correctamente

                dt_Usuario.Dt_Usuarios.guardarUsuario(self.line_Usuario_Nombre.text(),self.line_Usuario_Apellido.text(),self.line_Usuario_User.text(),self.line_Usuario_Password.text(), fechaTransformada)  # Recoge los datos en los "Lines" de Qt Desinger para guardarlos en la base de datos

                self.notifMensaje(self.indicador,"guardados")  # Se pasa por parametro el indicador que en este caso vale "1" y el resultado es que se guardo correctamente en la base de datos

                self.limpiarCampos()

                self.llenarTablaUsuario(dt_Usuario.Dt_Usuarios.listarUsuarios())  # Se reinicia la tabla para poder recargar los datos guardados

            else:

                self.notifMensaje(0, "")

        except Exception as e:
            print(f"Error: {e}")


    def obtenerDatosTablaUsuario(self):

        #Selecciona la fila de la tabla
        filaSeleccionada = self.tb_Usuario.currentRow()
        id = self.tb_Usuario.item(filaSeleccionada, 0).text()
        nombre = self.tb_Usuario.item(filaSeleccionada, 1).text()
        apellido = self.tb_Usuario.item(filaSeleccionada, 2).text()
        username = self.tb_Usuario.item(filaSeleccionada, 3).text()
        clave = self.tb_Usuario.item(filaSeleccionada, 4).text()
        fecha = self.tb_Usuario.item(filaSeleccionada, 5).text()

        #Tramsformar la fecha en formato "yyyy-MM-dd"
        fechaTransformada = QDate.fromString(fecha, "yyyy-MM-dd")

        #Asigna el contenido de la tabla seleccionada a los Edits Lines Correspondientes
        self.line_Usuario_Id.setText(id)
        self.line_Usuario_Nombre.setText(nombre)
        self.line_Usuario_Apellido.setText(apellido)
        self.line_Usuario_User.setText(username)
        self.line_Usuario_Password.setText(clave)
        self.line_Usuario_Fecha.setDate(fechaTransformada)


    def llenarTablaUsuario(self, datos):
        print("Datos de la Tablas")
        i = len(datos)
        self.tb_Usuario.setRowCount(i)
        tablerow = 0

        for row in datos:
            print(row)
            self.tb_Usuario.setItem(tablerow, 0, QTableWidgetItem(str(row["idusuario"])))
            self.tb_Usuario.setItem(tablerow, 1, QTableWidgetItem((row["nombre"])))
            self.tb_Usuario.setItem(tablerow, 2, QTableWidgetItem((row["apellido"])))
            self.tb_Usuario.setItem(tablerow, 3, QTableWidgetItem((row["user"])))
            self.tb_Usuario.setItem(tablerow, 4, QTableWidgetItem((row["clave"])))
            self.tb_Usuario.setItem(tablerow, 5, QTableWidgetItem(str(row["fecha_creacion"])))
            self.tb_Usuario.setItem(tablerow, 6, QTableWidgetItem(str(row["estado"])))
            tablerow = tablerow + 1


        '''******************************************  Rol   ******************************************'''






        '''******************************************  Opcion   ******************************************'''









if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    aplicacion = Form_Principal()
    aplicacion.show()
    app.exec()