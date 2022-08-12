from abc import ABC, abstractmethod

class EstrategiaDescuento(ABC):
    @abstractmethod
    def calcular_descuento(self, cantidad):
        pass


class EstrategiaDescuentoCantidad(EstrategiaDescuento):
    def calcular_descuento(self, cantidad):
        descuento = 0
        if cantidad > 0:
            descuento = 0
            if cantidad == 1:
                descuento = 0
            if 5 <= cantidad <= 20:
                descuento =  0.15
            if 20 <= cantidad <= 50:
                descuento =  0.21
            if cantidad > 50:
                descuento =  0.30
        return descuento


class EstrategiaDescuentoDias(EstrategiaDescuento):
    def __init__(self, dia):
        self.__dia = dia
        
    def calcular_descuento(self, cantidad):
        if self.__dia == 3:
            descuento = 0.20
        if self.__dia == 5:
            descuento = 0.35
        return descuento


class EstrategiaDescuentoMayorista(EstrategiaDescuento):
    def calcular_descuento(self, cantidad):
        pass


class ProductoContext:
    def __init__(self, precio, estrategia:EstrategiaDescuento):
        self.__precio = precio
        self.__estrategia = estrategia


    def calcular_precio(self):
        self.__estrategia.calcular_precio_con_descuento(self.__precio)