"""
Tenemos una Aplicación que necesita realizar una codificación (MD5, SHA-256, SHA-3)
sobre un texto de un archivo. Dependiendo lo que se elija desde la entrada de consola
de la aplicación cliente, es la codificación que se aplicara sobre dicho texto.
"""

import hashlib

dirFichero = 'archivo.txt'
with open(dirFichero, 'r') as reader:
    for line in reader:
        print(line)

class Code:
    
    def codificar(self, parametro):

        file = open('archivo.txt', 'rb')
        data = file.read()
        h = hashlib.new(parametro, b'file')
        h.update(data)
        hexdigest = h.hexdigest()     
        print('%s: %s' % (parametro, hexdigest))
        return h.hexdigest()


if __name__ == '__main__':
    parametro = input("""Ingrese un tipo de codificacion: 
                                                            [MD5] = md5
                                                            [SHA-256] = sha256
                                                            [SHA-3] = sha1
    """)

"""
    if parametro == 1:
        hashlib.md5
    elif parametro == 2:
        hashlib.sha256
    elif parametro == 3:
        hashlib.sha1
    else:
        close
"""

cod = Code()
cod.codificar(parametro=parametro)