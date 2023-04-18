from Datos import Conexion


class Dt_Usuarios:

    @classmethod
    def listarUsuarios(cls):
        cursor = Conexion.Conexion.obtenerConexion().cursor()
        cursor.execute("SELECT * FROM usuario")
        querys = cursor.fetchall()
        cursor.close()
        return querys


    @classmethod
    def guardarUsuario(cls, nombre, apellido, user, clave, fecha):

        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''INSERT INTO usuario ( nombre, apellido, user, clave, fecha_creacion, estado) VALUES ('{nombre}','{apellido}','{user}','{clave}','{fecha}','{1}')''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")

        except Exception as e:
            print(f"Error en guardarUsuario: {e}")


    @classmethod
    def editarUsuario(cls, id, nombre, apellido, user, clave, fecha):
        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''UPDATE usuario SET nombre = "{nombre}" , apellido = "{apellido}" , user = "{user}", clave = "{clave}", fecha_creacion = "{fecha}", estado = "{2}" WHERE idusuario = {id}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Editado")

        except Exception as e:
            print(f"Error en editarUsuario: {e}")

    @classmethod
    def eliminarUsuario(cls, id):
        try:
            cursor = Conexion.Conexion.obtenerConexion().cursor()
            sql = (f'''DELETE FROM usuario WHERE idusuario = {id}''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Eliminado")


        except Exception as ex:
            print(f"Error en eliminarUsuario: {ex}")





if __name__ == '__main__':
    print(Dt_Usuarios.listarUsuarios)

