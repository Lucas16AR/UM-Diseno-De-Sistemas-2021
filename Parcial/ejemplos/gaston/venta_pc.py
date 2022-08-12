from abc import ABC, abstractmethod

class ComisionStrategy(ABC):
    
    @abstractmethod
    def calcular_comision(self, cantidad):
        """Calculamos la comision segun la cantidad vendida"""

class x10Comision(ComisionStrategy):

    def calcular_comision(self, cantidad):
        return cantidad * 0.10

class x25Comision(ComisionStrategy):

    def calcular_comision(self, cantidad):
        return cantidad * 0.25

class x35Comision(ComisionStrategy):

    def calcular_comision(self, cantidad):
        return cantidad * 0.35


class Calculator:

    @staticmethod
    def set_strategy(key):
        strategy = {
            'x10': x10Comision(),
            'x25': x25Comision(),
            'x35': x35Comision()
        }
        return strategy[key]

if __name__ == '__main__':

    cantidad = int(input('Ingrese la cantidad que vendio: '))
    if 500 <= cantidad < 1000:
        strategy = Calculator.set_strategy('x10')
        r = strategy.calcular_comision(cantidad)
    elif 1000 <= cantidad <= 1500:
        strategy = Calculator.set_strategy('x25')
        r = strategy.calcular_comision(cantidad)
    elif cantidad > 1500:
        strategy = Calculator.set_strategy('x35')
        r = strategy.calcular_comision(cantidad)
    print(r)