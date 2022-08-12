from abc import abstractmethod
from selector_logica import Alumno
import random
import time
import heapq

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

    def agregar(self, alumno):
        heapq.heappush(self.alumnos, alumno.puntaje)

    def seleccionar(self, alumno):
        mitad = int(len(self.alumnos, alumno.puntaje) / 2)
        for a in range(mitad):
            heapq.heappop(self.alumnos)



class SorteoLista():

    __lista = []
    __seleccion = []
    def agregar(self, alumno:Alumno):
        self.__lista.append(alumno)

    def seleccionar(self):
        self.__lista.sort(key=lambda x: x.puntaje)
        mitad = int(len(self.__lista) / 2)
        for i in range(mitad):
               self.__seleccion.append(self.__lista[i])
               print("Seleccionados: ", self.__lista[i])

    def elegir(self):
        random.seed(time.time())
        print(random.choice(self.__seleccion))