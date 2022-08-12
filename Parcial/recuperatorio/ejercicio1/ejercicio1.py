"""
Crear una Aplicación que automatiza y simula la creación de perfiles de usuario en
Redes Sociales (Linkedin, Facebook, Instagram)
Pedir el ingreso de datos de:
▪ apellido, nombre, email, usuario, password y selección de la red social en donde
desea crear la cuenta.
▪ Imprimir la información de la cuenta creada.
"""

class Users(object):
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
    
    def crear_cuenta (self):
        print("Ingrese los siguientes datos")
        self.apellido = str(input("Apellido: "))
        self.nombre = str(input("Nombre: "))
        self.email = str(input("Email :"))
        self.usuario = str(input("Usuario: "))
        self.contrasena = int(input("Contraseña Numerica: "))


opc = True
while opc:
    print ("""
    [1] Facebook
    [2] Instagram
    [3] Linkedin
    [4] Salir
    """)
    opc = input("Que opcion desea elegir?: ")
            
    if opc == "1":
        print ("Bienvenido a Facebook")
        usuarios = Users("","","@", "", 1234567890)
        usuarios.apellido = input("Ingresar su apellido: ")
        usuarios.nombre = input("Ingresar su nombre: ")
        usuarios.email = input("Email: ")
        usuarios.usuario = input("Usuario: ")
        usuarios.contrasena = int(input("Contraseña Numerica: "))
        print(usuarios)


    elif opc == "2":
        print ("Bienvenido a Instagram")
        usuarios = Users("","","@", "", 1234567890)
        usuarios.apellido = input("Ingresar su apellido: ")
        usuarios.nombre = input("Ingresar su nombre: ")
        usuarios.email = input("Email: ")
        usuarios.usuario = input("Usuario: ")
        usuarios.contrasena = int(input("Contraseña Numerica: "))
        print(usuarios)


    elif opc == "3":
        print ("Bienvenido a Linkedin")
        usuarios = Users("","","@", "", 1234567890)
        usuarios.apellido = input("Ingresar su apellido: ")
        usuarios.nombre = input("Ingresar su nombre: ")
        usuarios.email = input("Email: ")
        usuarios.usuario = input("Usuario: ")
        usuarios.contrasena = int(input("Contraseña Numerica: "))
        print(usuarios)


    elif opc !="":
      print("\n Opcion incorrecta")