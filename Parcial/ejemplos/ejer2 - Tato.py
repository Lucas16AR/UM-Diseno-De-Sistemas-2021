import queue

cola_prioridad = queue.PriorityQueue()

class Persona():
    def __init__(self):
        self.__nombre = ''
        self.__apellido = ''
        self.__dni = ''


class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, matricula, email, promedio_nota):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__matricula = matricula
        self.__email = email
        self.__promedio_nota = promedio_nota
        cola_prioridad.put((int(self.__promedio_nota)*-1, self))



    def __repr__(self):
        return 'Nombre: %r, Apellido: %r,Promedio: %r' % (self.__nombre, self.__apellido, self.__promedio_nota)


    @property
    def get_nombre(self):
        return self.__nombre


    @property
    def get_apellido(self):
        return self.__apellido


    @property
    def get_dni(self):
        return self.__dni


    @property
    def get_matricula(self):
        return self.__matricula


    @property
    def get_email(self):
        return self.__email


    @property
    def get_promedio_nota(self):
        return self.__promedio_nota

persona1 = Alumno("Santiago", "Moyano", "41456789", "59119", 'santimoyano@gmail.com', '9')
persona2 = Alumno("Daniel", "Beato", "42469132", "59109", 'danielbeatoramirez@gmail.com', '8')
persona3 = Alumno("Delfina", "Quinteros", "43678901", "59339", 'delfiquinteros@gmail.com', '10')
persona4 = Alumno("Danilo", "Cerna", "38109234", "59065", 'danilocerna@gmail.com', '6')
persona5 = Alumno("Douglas", "Arenas", "42681098", "59101", 'douglasarena@gmail.com', '7')

while cola_prioridad.empty() == False:
    print(cola_prioridad.get()[1])












'''cola_prioridad = []


class Persona():
    nombre = ''
    apellido = ''
    dni = ''


class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, matricula, email, promedio_nota):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.matricula = matricula
        self.email = email
        self.promedio_nota = int(promedio_nota)
        cola_prioridad.append([int(self.promedio_nota), self.nombre, self])


persona1 = Alumno("Santiago", "Moyano", "41456789", "59119", 'santimoyano@gmail.com', '9')
persona1 = Alumno("Daniel", "Beato", "42469132", "59109", 'danielbeatoramirez@gmail.com', '8')
persona1 = Alumno("Delfina", "Quinteros", "43678901", "59339", 'delfiquinteros@gmail.com', '10')
persona1 = Alumno("Danilo", "Cerana", "38109234", "59065", 'danilocerna@gmail.com', '6')
persona1 = Alumno("Douglas", "Arenas", "42681098", "59101", 'douglasarena@gmail.com', '7')
cola_prioridad.sort(reverse=True)
print(cola_prioridad)'''