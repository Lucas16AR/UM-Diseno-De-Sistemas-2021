class ArchivoSQL:
    def convertir_archivo(self, source, destiny):
        source = open(source, 'r', encoding='utf8')
        destiny = open(destiny, 'w', encoding='utf8')
        for linea in source:
            lineas = linea.strip().split(";")
            linea_sql = f"INSERT INTO usuarios(nombre, apellido) VALUES ('{lineas[0]}', '{lineas[1]}');\n"
            destiny.writelines(linea_sql)
            print(linea_sql)
        source.close()
        destiny.close()