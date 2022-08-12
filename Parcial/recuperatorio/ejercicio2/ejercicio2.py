"""
Crear una aplicación de turnos presenciales para un Banco, con los siguientes
requisitos:
▪ La Persona que saca el turno debe ingresar por teclado Nombre, Apellido y tipo
de cliente del banco(JUBILADO,CLIENTE DEL BANCO, PUBLICO GENERAL).
▪ Existe una prioridad que se debe respetar:
• 1ro JUBILADOS
• 2do CLIENTES DEL BANCO
• 3ro PUBLICO EN GENERAL
▪ Después que existan más de 5 personas en cola, mostrar por pantalla cuales es el
orden en que deben ser atendidas.
▪ Ejecutar la aplicación hasta que el Banco no atienda más público.
"""

print("Bienvenido cliente al Banco San Rafael")

import heapq
from os import name

class Persona:
    """Clase general persona"""

    def __init__(self, nombre: str, apellido: str, dni: int):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

class Cliente(Persona):
    """Clase cliente que hereda de persona"""

    def __init__(self, nombre: str, apellido: str, dni: int, tipo: str):
        super().__init__(nombre, apellido, dni)
        self.tipo = tipo


    def __repr__(self) -> str:
        return f'({self.nombre}, {self.apellido}, {self.dni}, {self.tipo})'

class PriorytyQueue:

    def obtener_cliente(numerodeveces):
        numerodeveces = int(input("Ingrese cuantos clientes dejara entrar: "))
        cliente = []
        for i in range(0, numerodeveces):
            name = str(input("Ingrese su nombre: "))
            cliente.append(name)
            surname = str(input("Ingrese su apellido: "))
            cliente.append(surname)
            tipe = str(input("Ingrese el numero de tipo de cliente: "))
            cliente.append(tipe)

    def agregar_cliente(self, cliente: Cliente):
        self.cliente[cliente.nombre] = cliente.tipo

    def ordenar_cola(self):
        self.alumnos = {k: v for k, v in sorted(self.cliente.items(), key=lambda item: (item[1])* -1)}
        return self.cliente



cola = PriorytyQueue()
cola.agregar_cliente(cliente)
cola.agregar_cliente(cliente)
cola.agregar_cliente(cliente)
cola.agregar_cliente(cliente)
print(cola.cliente, '[COLA NORMAL]')
print(cola.ordenar_cola(), '[COLA ORDENADA POR PRIORIDAD]')

    