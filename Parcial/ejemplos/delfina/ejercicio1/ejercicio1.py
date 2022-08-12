"""
Tenemos una Aplicación que necesita realizar una codificación (MD5, SHA-256, SHA-3)
sobre un texto de un archivo. Dependiendo lo que se elija desde la entrada de consola
de la aplicación cliente, es la codificación que se aplicara sobre dicho texto
"""

import hashlib


class Codificacion:
    def codificar(self, parametro):
        file = open('archivo.txt', 'rb')
        data = file.read()
        h = hashlib.new(parametro, b'file')
        h.update(data)
        hexdigest = h.hexdigest()
        print('%s: %s' % (parametro, hexdigest))
        return h.hexdigest()


if __name__ == '__main__':
    parametro = input("Ingrese el tipo de codificacion: ")
    cod = Codificacion()
    cod.codificar(parametro=parametro)