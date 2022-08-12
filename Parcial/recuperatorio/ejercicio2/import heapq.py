import heapq

class Persona:

    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, tipo: int):
        super().__init__(nombre, apellido)
        self.tipo = tipo

    def __repr__(self) -> str:
        return f'({self.nombre}, {self.apellido}, {self.tipo})'


class PriorytyQueue:

    Cliente = {}

    def agregar_cliente(self, cliente: Cliente):
        self.Cliente[cliente.nombre] = cliente.tipo

    def ordenar_cola(self):
        self.Cliente = {k: v for k, v in sorted(self.Cliente.items(), key=lambda item: (item[1])* 1)}
        return self.Cliente



cliente1 = Cliente('Gaston', 'Fenske', 3) 
cliente2 = Cliente('Lucas', 'Galdame', 1)
cliente3 = Cliente('Santiago', 'Moyano', 2)
cliente4 = Cliente('Bruno', 'Romero', 1)
cliente5 = Cliente('Douglas', 'Arenas', 3)
 

cola = PriorytyQueue()
cola.agregar_cliente(cliente1)
cola.agregar_cliente(cliente2)
cola.agregar_cliente(cliente3)
cola.agregar_cliente(cliente4)
print(cola.Cliente, '[COLA NORMAL]')
print(cola.ordenar_cola(), '[COLA ORDENADA POR PRIORIDAD]')