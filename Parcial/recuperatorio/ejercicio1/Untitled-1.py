"""
Crear una Aplicación que automatiza y simula la creación de perfiles de usuario en
Redes Sociales (Linkedin, Facebook, Instagram)
Pedir el ingreso de datos de:
▪ apellido, nombre, email, usuario, password y selección de la red social en donde
desea crear la cuenta.
▪ Imprimir la información de la cuenta creada.
"""

from abc import ABC, abstractclassmethod

class Users(ABC):
    def __init__ (self, apellido, nombre, email, usuario, contrasena):
        self.apellido = apellido
        self.nombre = nombre
        self.email = email
        self.usuario = usuario
        self.contrasena = contrasena

    def __str__(self):
        return f'Apellido: {self.apellido}, Nombre: {self.nombre}, Email: {self.email}, Usuario: {self.usuario}, Contraseña: {self.contrasena}'

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido


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
    def contrasena(self):
        return self.__contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self.__contrasena = contrasena

 
class Ingreso(Users):

    """@abstractclassmethod
    def crear_cuenta(self):
"""
    def crear_cuenta (self):
        print("Ingrese los siguientes datos")
        self.apellido = str(input("Ingrese su Apellido: "))
        self.nombre = str(input("Ingrese su Nombre: "))
        self.email = str(input("Ingrese su Email :"))
        self.usuario = str(input("Ingrese su Usuario: "))
        self.contrasena = int(input("Ingrese su Contraseña Numerica: "))

        


class Facebook(Users):
    def ingresar(crear_cliente):     
        return Ingreso.crear_cliente()
    

class Instagram(Users): 
    def ingresar(crear_cliente):     
        return Ingreso.crear_cliente()

 
class Linkedin(Users):
    def ingresar(crear_cliente):    
        return Ingreso.crear_cliente()


def read_factory() -> Users:
    
    factories = {
        'Facebook': Facebook,
        'Instagram': Instagram,
        'Linkedin': Linkedin
    }

    while True:
        option = str(input('Ingrese la aplicacion que desea abrir (Facebook - Instagram - Linkedin): '))
        if option in factories:
            return factories[option]
        else:
            print('Esa opcion no es correcta')

if __name__ == '__main__':

    while True:
        factory = read_factory()
        Users('apellido', 'nombre', 'email', 'usuario', 'contrasena')