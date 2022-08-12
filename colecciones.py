from abc import ABC, abstractmethod
from selector_logica import Alumno
import random
import time
import heapq

class Sorteo(ABC):
    
    @abstractmethod
    def agregar(self, alumno):
        pass
    
    @abstractmethod
    def seleccionar(self):
        pass
    
    @abstractmethod
    def elegir(self):
        pass


class PriorityQueue(Sorteo):
    def __init__(self):
        self.alumnos = [] 
        self.sorteo = []

    def agregar(self, alumno: Alumno):
        heapq.heappush(self.alumnos, (alumno, alumno.puntaje))


    def seleccionar(self):
        mitad = int(len(self.alumnos) / 2)
        for a in range(mitad):
            self.sorteo.append(heapq.heappop(self.alumnos))
        return self.sorteo

    def elegir(self):
        random.seed(time.time())
        return random.choice(self.sorteo)

class SorteoLista(Sorteo):

    __lista = []
    __seleccion = []
    def agregar(self, alumno:Alumno):
        self.__lista.append(alumno)

    def seleccionar(self):
        self.__lista.sort(key=lambda x: x.puntaje)
        mitad = int(len(self.__lista) / 2)
        self.__seleccion = self.__lista[:mitad]
        return self.__seleccion

    def elegir(self):
        random.seed(time.time())
        return random.choice(self.__seleccion)

class SorteoColaConPrioridad(Sorteo):

    __cola = []
    __seleccion = []
    def __init__(self) -> None:
        self.__index = 0

    def agregar(self, alumno:Alumno):
        heapq.heappush(self.__cola, (alumno.puntaje, self.__index,alumno))
        self.__index += 1

    def seleccionar(self):
        mitad = int(len(self.__cola) / 2)
        while len(self.__cola) > mitad:
            print("Seleccionados: ", self.__cola[0])
            self.__seleccion.append(heapq.heappop(self.__cola))

    def elegir(self):
        random.seed(time.time())
        print(f"Seleccionado: {0}", self.__convertTuple(random.choice(self.__seleccion)))

    def __convertTuple(self, tupla):
        out = ''
        """for item in tupla:
            out = str(item) + out""" 
        return out.join(str(tupla))
