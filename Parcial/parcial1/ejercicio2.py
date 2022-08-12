import heapq

class Persona(object):

    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f'Persona ==> Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}'


class Alumno(Persona):

    def __init__(self, nombre, apellido, dni, matricula, email, promedio):

        Persona.__init__(self, nombre, apellido, dni)

        self.matricula = matricula
        self.email = email
        self.promedio = promedio

    def __str__(self):
        return f'Alumno ==> Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}, Matricula: {self.matricula}, Email: {self.email}, Nota: {self.promedio}'

Alumnos = [
        {'Nombre': 'Lucas', 'Apellido': 'Galdame', 'DNI': 1122, 'Matricula': 500, 'Email': "thebitw16@gmail.com", 'Promedio': 7.5},
        {'Nombre': 'Delfina', 'Apellido': 'Quinteros', 'DNI': 1234, 'Matricula': 501, 'Email': "ander34@gmail.com", 'Promedio': 8.8},
        {'Nombre': 'Danilo', 'Apellido': 'Cerna', 'DNI': 1243, 'Matricula': 502, 'Email': "dan1@gmail.com", 'Promedio': 7.8},
        {'Nombre': 'Daniel', 'Apellido': 'Beato', 'DNI': 1576, 'Matricula': 503, 'Email': "tatovelez@gmail.com", 'Promedio': 9.1},
        {'Nombre': 'Lucila', 'Apellido': 'Martinez', 'DNI': 1237, 'Matricula': 504, 'Email': "lara12@gmail.com", 'Promedio': 8.6},
        {'Nombre': 'Santiago', 'Apellido': 'Moyano', 'DNI': 1986, 'Matricula': 505, 'Email': "santix@gmail.com", 'Promedio': 6.5},
        {'Nombre': 'Bruno', 'Apellido': 'Romero', 'DNI': 1111, 'Matricula': 506, 'Email': "qw2346adf@gmail.com", 'Promedio': 7.9},
        {'Nombre': 'Yamila', 'Apellido': 'Palavecino', 'DNI': 1767, 'Matricula': 507, 'Email': "chos435df@gmail.com", 'Promedio': 8.1},
        {'Nombre': 'Enzo', 'Apellido': 'Fernandez', 'DNI': 1543, 'Matricula': 508, 'Email': "endotaxix@gmail.com", 'Promedio': 6.2}
]

bajo = heapq.nsmallest(1, Alumnos, key = lambda p : p ['Promedio'])
alto = heapq.nlargest(1, Alumnos, key = lambda p : p ['Promedio'])

print("Notas Bajas: ", bajo)
print("Notas Altas: ", alto)