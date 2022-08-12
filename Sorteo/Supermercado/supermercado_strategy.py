from abc import ABC, abstractmethod

from producto import Producto
from carrito import Carrito
from estrategias import EstrategiaDescuentoCantidad



if __name__== '__main__':
    coca = Producto(50, '1234', 'bebida')
    pan = Producto(100,'321', 'lactal')
    pan_2 =  Producto(120, '321', 'blanco')
    bebida = Producto(60, '7791813800774', 'paso de los toros')
    carrito = Carrito(EstrategiaDescuentoCantidad())
    carrito.agregar(coca,2)
    carrito.agregar(pan,1)
    carrito.agregar(pan_2,1)
    carrito.agregar(bebida,10)
    print(carrito.esta_vacio())
    agregar_codigo = input("Ingrese el codigo de barras del producto: ")
    print(f'{carrito.obtener_producto(agregar_codigo)}')

    for p in carrito.obtener_todos():
        print (f'{p.codigo}\t{p.descripcion}\t{carrito.obtener_todos().get(p)}\t{carrito.descuento(p)}')
    print(f'total: ${carrito.total_precio()}')
    
    carrito.vaciar()
    print(carrito.esta_vacio())