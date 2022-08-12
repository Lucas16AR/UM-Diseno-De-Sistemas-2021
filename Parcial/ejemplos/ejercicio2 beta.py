"""
Crear una clase simple Alumno con los siguientes atributos: matricula, email,
promedio de nota, que herede Persona con atributos como: nombre, apellido, dni,
Demostrar:
▪ Que se puede añadir múltiples elementos de tipo Alumno con su promedio de
nota a una Cola con Prioridad
▪ Que una vez finalizada la carga de alumnos, se puede obtener el total de alumnos
ordenanos de mayor a menor por promedio de nota.
"""

class Persona(object):

    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f'Persona: Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}'

"""
per1 = Persona("Lucas Alejandro", "Galdame Villegas", 44666111)
per2 = Persona("Delfina", "Quinteros", 44332123)

print(per1)
print(per2)
"""

class Alumno(Persona):

    def __init__(self, nombre, apellido, dni, matricula, email, promedio):

        Persona.__init__(self, nombre, apellido, dni)

        self.matricula = matricula
        self.email = email
        self.promedio = promedio

    def __str__(self):
        return f'Alumno: Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}, Matricula: {self.matricula}, Email: {self.email}, Nota: {self.promedio}'

alum1 = Alumno('Lucas', 'Galdame', 44555666, 500,"luqui0008@gmail.com",6.7)
alum2 = Alumno('Delfina', 'Quinteros', 44555667, 501,"ander34@gmail.com",7.8)
alum3 = Alumno('Danilo', 'Cerna', 44190873, 502,"dan1@gmail.com",7.8)
alum4 = Alumno('Daniel', 'Beato', 41125560, 503,"tatovelez@gmail.com",9.1)
alum5 = Alumno('Lucila', 'Martinez', 42008753, 504,"lara12@gmail.com",8.6)
alum6 = Alumno('Santiago', 'Moyano', 44555667, 505,"santix@gmail.com",6.5)
alum7 = Alumno('Bruno', 'Romero', 42656354, 506,"qw2346adf@gmail.com",7.9)
alum8 = Alumno('Yamila', 'Palavecino', 43515657, 507,"chos435df@gmail.com",8.1)
alum9 = Alumno('Enzo', 'Fernandez', 44317888, 508,"endotaxix@gmail.com",6.2)


print(alum1)
print(alum2)
print(alum3)
print(alum4)
print(alum5)
print(alum6)
print(alum7)
print(alum8)
print(alum9)