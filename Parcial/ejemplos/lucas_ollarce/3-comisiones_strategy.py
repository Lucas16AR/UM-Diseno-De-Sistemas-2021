from abc import ABC, abstractmethod

class EstrategiaVenta(ABC):
    @abstractmethod
    def calcular_comision(self, cantidad):
        pass


class EstrategiaComision(EstrategiaVenta):
    def calcular_comision(self, cantidad):
        if cantidad > 0:
            comision = 0
        if 500 <= cantidad <= 1000:
            comision = cantidad * 0.10
        if 1000 <= cantidad <= 1500:
            comision = cantidad * 0.25
        if cantidad > 1500:
            comision = cantidad * 0.35
        return comision


if __name__ == '__main__':
    print("---------COMISIONES---------")
    cantidad = float(input("Ingrese la cantidad vendida: "))
    ventas = EstrategiaComision()
    comision = ventas.calcular_comision(cantidad=cantidad)
    print("Su comision es de $" + str(comision))
