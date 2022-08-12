"""
Crear una aplicación que se encarga de mostrar el precio de distintos productos,
dependiendo del forma de pago varía su valor monetario.
Formas de pago:
▪ Efectivo: 10% de descuento del valor de lista.
▪ Tarjeta de Debito: 0% de descuento.
▪ Tarjeta ahora 12: 25% de interes.
▪ Tarjeta Credito: 20% de interes.
Se pide mostrar los distintos precios de un producto seleccionado de una lista de
productos previamente cargada.
"""


import os
import sys

from abc import ABC, abstractmethod

class Producto(object):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f'Producto ==> Producto: {self.nombre}, Precio: {self.precio}'

Productos = []
Productos.append(['Cereal Nesquik', 240])
Productos.append(['Leche Descremada La Serenisima', 100])
Productos.append(['Coca Cola 500 ml', 90])
Productos.append(['Alfajor Milka', 85])
Productos.append(['Galletas Oreo', 110])



class ComisionStrategy(ABC):
    
    @abstractmethod
    def calcular_precioFinal(self, cantidad):
        """Calcular precio final"""

class forma_efectivo(ComisionStrategy):

    def calcular_precioFinal(self, cantidad):
        return cantidad * 0.90

class forma_debito(ComisionStrategy):

    def calcular_precioFinal(self, cantidad):
        return cantidad * 1.0

class forma_ahoraDoce(ComisionStrategy):

    def calcular_precioFinal(self, cantidad):
        return cantidad * 1.25

class forma_credito(ComisionStrategy):

    def calcular_precioFinal(self, cantidad):
        return cantidad * 1.20


class Calculator:

    @staticmethod
    def set_strategy(key):
        strategy = {
            '-10': forma_efectivo(),
            '0': forma_debito(),
            '+25': forma_ahoraDoce(),
            '+20': forma_credito()
        }
        return strategy[key]


if __name__ == '__main__':
    print(Productos)
    cantidad = int(input("Ingrese el precio bruto: "))


opc = True
while opc:
    print ("""
    [1] Efectivo (10% de interes)
    [2] Tarjeta de Debito (Sin interes y descuento)
    [3] Tarjeta de Ahora 12 (25% de interes)
    [4] Tarjeta de Credito (20% de interes)
    [5] Mostrar Productos
    [6] Salir
    """)
    opc = input("Que opcion desea elegir?: ")

    if opc == "1": 
        strategy = Calculator.set_strategy('-10')
        r = strategy.calcular_precioFinal(cantidad)
        print(f"Efectivo, precio final: {r}") 
    elif opc == "2":
        strategy = Calculator.set_strategy('0')
        r = strategy.calcular_precioFinal(cantidad)
        print(f" Tarjeta de Debito, precio final: {r}") 
    elif opc == "3":
        strategy = Calculator.set_strategy('+25')
        r = strategy.calcular_precioFinal(cantidad)
        print(f" Tarjeta de Ahora 12, precio final: {r}") 
    elif opc == "4":
        strategy = Calculator.set_strategy('+20')
        r = strategy.calcular_precioFinal(cantidad)
        print(f" Tarjeta de Credito, precio final: {r}") 
    elif opc == "5":
        print(Productos)
    elif opc == "6":
        break
    elif opc !="":
      print("\n Opcion incorrecta")