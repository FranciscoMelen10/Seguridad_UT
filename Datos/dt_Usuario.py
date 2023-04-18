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
            print(fecha)
            cursor = Conexion.Conexion.obtenerConexion().cursor()

            sql = (f'''INSERT INTO usuario ( nombre, apellido, user, clave, fecha_creacion, estado) VALUES ('{nombre}','{apellido}','{user}','{clave}','{fecha}','{1}')''')
            cursor.execute(sql)
            cursor.connection.commit()
            cursor.close()
            print("Guardado")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    print(Dt_Usuarios.listarUsuarios)

