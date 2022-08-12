import json

class ArchivoJson:
    def convertir_archivo(self):
        filename = 'archivo.txt'
        diccionario = {}
        with open(filename) as file:
            for line in file:
                eliminar_finales, lineas = line.strip().split(None, 1)
                diccionario[eliminar_finales] = lineas.strip()
        out_file = open("archivo.json", "w")
        json.dump(diccionario, out_file, indent=4)
        out_file.close()