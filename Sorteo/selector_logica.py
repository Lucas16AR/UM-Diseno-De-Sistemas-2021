from abc import abstractmethod


class Alumno():
    def __init__(self, nombre: str, apellido: str, puntaje: int):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__puntaje = puntaje

    def __gt__(self, alumno):
        return self.__puntaje > alumno.puntaje

    def __str__(self) -> str:
        return f"{self.__nombre}, {self.__apellido}, {self.__puntaje}"

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellido: str):
        self.__apellido = apellido

    @property
    def puntaje(self):
        return self.__puntaje

    @puntaje.setter
    def puntaje(self, puntaje: int):
        self.__puntaje = puntaje
