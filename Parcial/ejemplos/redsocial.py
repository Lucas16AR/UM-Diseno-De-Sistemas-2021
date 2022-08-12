'''Crear una Aplicación que automatiza y simula la creación de perfiles de usuario en
Redes Sociales (Linkedin, Facebook, Instagram)
Pedir el ingreso de datos de:
▪ apellido, nombre, email, usuario, password y selección de la red social en donde
desea crear la cuenta.
▪ Imprimir la información de la cuenta creada.'''

class Usuarios(object):
    def __init__ (self, nombre, email, usuario, password):
        self.nombre = nombre
        self.email = email
        self.usuario = usuario
        self.password = password

    def __str__(self):
        return f'Nombre: {self.nombre}, Email: {self.email}, Usuario {self.usuario}, Password: {self.password}'

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password


    
class Sing_in(Usuarios):
    
    def crear_cuenta (self):
        self.nombre = str(input("Nombre:"))
        self.email = str(input("Email:"))
        self.usuario = str(input("Usuario:"))
        self.password = int(input("Password:"))


        
if __name__ == "__main__":
    print ("Bienvenido a Facebook, por favor ingresar una cuenta para continuar")
    user = Usuarios("a","aa@","a", 123)
    user.nombre = input("Ingresar nombre de usuario: ")
    user.email = input("Email")
    user.usuario = input("Usuario")
    user.password = int(input("Password"))
    print(user)