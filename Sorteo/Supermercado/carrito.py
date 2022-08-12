from producto import Producto
from estrategias import EstrategiaDescuento

class Carrito():
    __productos = dict()

    def __init__(self, estrategia:EstrategiaDescuento):
        self.__estrategia = estrategia
    
    def agregar(self, producto:Producto, cantidad:int):
        self.__productos[producto] = cantidad + self.__productos.get(producto,0)
     
    def borrar(self, producto:Producto):
        self.__productos.pop(producto)

    def modificar_cantidad(self, producto:Producto, cantidad:int):
        if cantidad > 0:
            self.__productos[producto] = cantidad
        if cantidad == 0:
            self.borrar(producto)
   
    def modificar(self, producto1:Producto, producto2:Producto):  
        self.borrar(producto1)
        self.agregar(producto2)
        
    def obtener_producto(self, codigo:str):
        for p in self.__productos:
            if p.codigo == codigo:
                return p
        return None
        
    def obtener_todos(self,):
        return self.__productos
    
    def total_precio(self):
        suma = 0
        for p in self.__productos:
            suma += p.precio - (p.precio * self.__estrategia.calcular_descuento(self.__productos.get(p))) * self.__productos.get(p)
        return suma 
    
    def esta_vacio(self):
        if len(self.__productos) == 0:
            return True
        return False            
    
    def vaciar(self):
        self.__productos.clear()

    def descuento(self, producto: Producto)-> float:
        return self.__estrategia.calcular_descuento(self.__productos.get(producto)) 
