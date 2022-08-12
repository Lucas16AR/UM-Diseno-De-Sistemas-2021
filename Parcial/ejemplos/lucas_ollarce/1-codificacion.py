from abc import ABC, abstractmethod
import hashlib
import getopt
import sys


class Strategy(ABC):
    @abstractmethod
    def aplicar_codificacion(self, data):
        pass


class Archivo():
    def __init__(self, codificacion: Strategy) -> None:
        self.__codificacion = codificacion

    def __str__(self) -> str:
        return f"archivo: {self.__codificacion}"

    @property
    def codificacion(self) -> Strategy:
        return self.__codificacion

    @codificacion.setter
    def codificacion(self, codificacion: Strategy) -> None:
        self.__codificacion = codificacion

    def leer(self, archivo):
        file = open(archivo, 'rb')
        lines = file.read()
        file.close()
        return lines

    def codificar(self, data) -> None:
        result = self.__codificacion.aplicar_codificacion(self.leer(data))
        return result


class CodificacionMD5(Strategy):
    def aplicar_codificacion(self, data):
        return hashlib.md5(data).hexdigest()


class CodificacionSHA256(Strategy):
    def aplicar_codificacion(self, data):
        return hashlib.sha256(data).hexdigest()


class CodificacionSHA3(Strategy):
     def aplicar_codificacion(self, data):
         return hashlib.sha3_512(data).hexdigest()


if __name__ == "__main__":
    try:
        opt, arg = getopt.getopt(sys.argv[1:], 'c:a:')
    except getopt.GetoptError as err:
        sys.exit()

    arch = ''
    codif = ''

    for(op, ar) in opt:
        if op == '-a':
            arch = ar
        elif op == '-c':
            codif = ar
        else:
            sys.exit(2)

    if codif == 'md5':
        cod = Archivo(CodificacionMD5())
    elif codif == 'sha256':
        cod = Archivo(CodificacionSHA256())
    elif codif == 'sha3':
        cod = Archivo(CodificacionSHA3())
    else:
        print("Opcion invalida, -c debe ser md5, sha256 o sha3")
        sys.exit()

    print(cod.codificar(arch))
