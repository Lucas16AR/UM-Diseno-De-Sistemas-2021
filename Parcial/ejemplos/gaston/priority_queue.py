import heapq

class Persona:
    """Clase general persona"""

    def __init__(self, nombre: str, apellido: str, dni: int):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni


class Alumno(Persona):
    """Clase alumno que ereda de persona"""

    def __init__(self, nombre: str, apellido: str, dni: int, matricula: int, email: str, promedio: int):
        super().__init__(nombre, apellido, dni)
        self.matricula = matricula
        self.email = email
        self.promedio = promedio

    def __repr__(self) -> str:
        return f'({self.nombre}, {self.promedio})'


class PriorytyQueue:

    alumnos = {}

    def agregar_alumno(self, alumno: Alumno):
        """Agregamos un objeto alumno a la cola"""
        self.alumnos[alumno.nombre] = alumno.promedio

    def ordenar_cola(self):
        """Ordenamos los alumnos segun su promedio"""
        self.alumnos = {k: v for k, v in sorted(self.alumnos.items(), key=lambda item: (item[1])* -1)}
        return self.alumnos


alumno = Alumno('Gaston', 'Fenske', 42265179, 59117, 's.fenske@alumno.um.edu.ar', 4)
alumno2 = Alumno('Lucas', 'Galdame', 44000444, 59111, 'capi@.com', 10)
alumno3 = Alumno('Matatan', 'Moyano', 44000445, 517892, 'matatan.com', 7)
alumno4 = Alumno('Bruno', 'Romero', 44000444, 51789, 'badbruny@net.com', 2)

cola = PriorytyQueue()
cola.agregar_alumno(alumno)
cola.agregar_alumno(alumno2)
cola.agregar_alumno(alumno3)
cola.agregar_alumno(alumno4)
print(cola.alumnos, '[COLA NORMAL]')
print(cola.ordenar_cola(), '[COLA ORDENADA POR PRIORIDAD]')

        