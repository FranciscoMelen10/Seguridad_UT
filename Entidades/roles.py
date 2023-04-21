# Francisco de Jesús Melendez Simplina
#Entidad Rol

class Rol:
    def __init__(self,idRol, rol, descripcionRol, estado):
        self.idRol = idRol
        self.rol = rol
        self.descripcionRol = descripcionRol
        self.estado = estado

    def __str__(self):
        return f'''
        idRol: {self.idRol}
        rol: {self.rol}
        descripcionRol: {self.descripcionRol}
        estado: {self.estado}
        '''

    @property
    def idRol(self):
        return self.idRol

    @idRol.setter
    def idRol(self, idRol):
        self.idRol = idRol

    @property
    def rol(self):
        return self.rol

    @rol.setter
    def idRol(self, rol):
        self.rol = rol

    @property
    def descripcionRol(self):
        return self.descripcionRol

    @descripcionRol.setter
    def descripcionRol(self, descripcionRol):
        self.descripcionRol = descripcionRol

    @property
    def estado(self):
        return self.estado

    @estado.setter
    def estado(self, estado):
        self.estado = estado


