from abc import ABC, abstractmethod

class IFigura(ABC):
    """Interfaz de figura"""

class Rectangulo(IFigura):
    def __init__(self, alto, ancho) -> None:
        self.alto = alto
        self.ancho = ancho

class Triangulo(IFigura):
    def __init__(self, alto, ancho) -> None:
        self.alto = alto
        self.ancho = ancho


class IFiguraArea(ABC):
    """Interfaz del calculador de area"""

    @abstractmethod
    def calcular_area(figura: IFigura) -> int:
        """Calcula el area mediante una figura que le pases"""
        area = 0
        return area

class RectanguloArea(IFiguraArea):

    def calcular_area(figura: IFigura) -> int:
        area = 0
        return area

class TrianguloArea(IFiguraArea):

    def calcular_area(figura: IFigura) -> int:
        area = 0
        return area

class FactoryArea(ABC):

    @abstractmethod
    def calcular_area_de_figura(figura_a_calcular: IFiguraArea):
        """Le pasamos el tipo de area que queremos calcular:
        (area de un rectangulo, de un triangulo, etc)"""

    
def main():

    factories = {
        'rectangulo': 
    }