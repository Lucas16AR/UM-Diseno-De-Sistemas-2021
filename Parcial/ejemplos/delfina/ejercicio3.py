"""
Tenemos una aplicación que se encarga de venta de PC, la cual paga diferentes
comisiones a sus vendedores según el monto de venta.
Las comisiones son las siguientes:
▪ Si el monto > U$S 500 < U$S 1000 10% de comisión.
▪ Si el monto > U$S 1000 < U$S 1500 25% de comisión.
▪ Si el monto > U$S 1500 35% de comisión.
Se necesita saber por cada compra total que comisiones son obtenidas por el
vendedor
"""
from abc import ABC, abstractmethod


class Venta(ABC):

    @abstractmethod
    def calcular_comision(self, monto: float):
        pass

    @abstractmethod
    def calcular_precio(self, monto: float, comision: float):
        pass


class Comision(Venta):

    def calcular_comision(self, monto: float):
        if monto < 500:
            comision = 0
        if 500 < monto > 1000:
            comision = 0.10
        if 1000 < monto > 1500:
            comision = 0.25
        if monto > 1500:
            comision = 0.35
        return comision

    def calcular_precio(self, monto: float, comision: float):
        c = monto * comision
        precio_final = monto - c
        print(f'El precio final del produto es ${precio_final} y la comision es de ${c}')
        return c, precio_final


if __name__ == '__main__':
    monto = float(input("Ingrese el monto de la PC: "))
    venta = Comision()
    comision = float(venta.calcular_comision(monto=monto))
    precio = venta.calcular_precio(monto=monto, comision=comision)