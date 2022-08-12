"""
Tenemos una aplicación que se encarga de venta de PC, la cual paga diferentes
comisiones a sus vendedores según el monto de venta.
Las comisiones son las siguientes:
▪ Si el monto > U$S 500 < U$S 1000 10% de comisión.
▪ Si el monto > U$S 1000 < U$S 1500 25% de comisión.
▪ Si el monto > U$S 1500 35% de comisión.
Se necesita saber por cada compra total que comisiones son obtenidas por el
vendedor.
"""

from abc import abstractclassmethod

class Comision():

    @abstractclassmethod
    def comision(self, monto):
        pass

    @abstractclassmethod
    def precio(self, monto, precio):
        pass


class Comision10():

    def comision(self, monto):
        return monto * 0.10

class Comision25():

    def comision(self, monto):
        return monto * 0.25

class Comision35():

    def comision(self, monto):
        return monto * 0.35

class Venta():

    def precio(self, monto: float, comision: float):
        comision1 = monto * comision
        precio_final = monto - comision1
        print(f'Precio final del produto: ${precio_final}')
        print(f'Comision: ${comision1}')
        return comision1, precio_final

    if __name__ == '__main__':
        monto = float(input("Ingrese el monto de la PC: "))
        venta = Comision()
        comision = float(venta.precio(monto = monto))
        precio_final = venta.comision(monto = monto, comision = comision)