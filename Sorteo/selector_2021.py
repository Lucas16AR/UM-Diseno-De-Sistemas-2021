from selector_logica import Alumno
from sorteo import SorteoLista

if __name__ == '__main__':
    alumnos = SorteoLista()

    alumnos.agregar(Alumno('Julian', 'Navarrete', 3))
    alumnos.agregar(Alumno('Delfina', 'Quinteros', 3))
    alumnos.agregar(Alumno('Gastón', 'Fenske', 2))
    alumnos.agregar(Alumno('Enzo', 'Fernandez', 1))
    alumnos.agregar(Alumno('Gabriel', 'Almonacid', 3))
    alumnos.agregar(Alumno('Douglas', 'Arenas', 1))
    alumnos.agregar(Alumno('Lucas', 'Galdame', 1))
    alumnos.agregar(Alumno('Santiago', 'Moyano', 1))
    alumnos.agregar(Alumno('José', 'Ruti', 2))
    alumnos.agregar(Alumno('Bruno', 'Romero', 1))
    alumnos.agregar(Alumno('Danilo', 'Cerna', 2))
    beato = Alumno('Daniel', 'Beato', 3)
    alumnos.agregar(beato)
    alumnos.agregar(Alumno('Lucas', 'Ollarce', 4))

    alumnos.seleccionar()
    alumnos.elegir()

    #for a in sorted(alumnos):
        #print(a)

    #colas con prioridad
    