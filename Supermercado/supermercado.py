from datetime import datetime

class Producto:

    def _init__(self, precio):
        #self.__codigo = codigo
        self.__precio = precio
        #self.__descripcion = descripcion
       
        
    def calcular_precio_con_descuento(self, precio:float, cantidad:int):
        if cantidad > 0:
            
            if cantidad == 1:
                descuento = 0
            if 5 <= cantidad <= 20:
                descuento = precio * 0.15
            if 20 > cantidad <= 50:
                descuento = precio * 0.21
            if cantidad > 50:
                descuento = precio * 0.30
        self.__calcular_precio(precio, descuento, cantidad)
        

    def calcular_precio_con_descuento(self, precio:float, cantidad:int, dia:int):
        descuento = 0
        print("Dia de la semana: ", dia)
        if dia == 3:
            print ("calcula descuento dia 3: ")
            descuento = precio * 0.20
        elif dia == 5:
            print("calcula descuento dia 5: ")
            descuento = precio * 0.35
        self.__calcular_precio(precio, descuento, cantidad)
        
    
    def calcular_precio_con_descuento(self, precio:float, cantidad:int, tarjeta_del_local:bool):
        
        if tarjeta_del_local:
            descuento = precio * 0.10
        self.__calcular_precio(precio, descuento, cantidad)
    
    
    def __calcular_precio(self, precio, descuento, cantidad):
        
        precio_final = (precio - descuento) * cantidad
        return print(precio_final)


if __name__ == "__main__":

    producto = Producto()
    precio = float(input("Digite el precio: "))
    cantidad = int(input("Cantidad: "))
    dia = int(input("Ingregar dia por numero: ")) #ej : domingo n° 0
    #producto.calcular_precio_con_descuento(precio, cantidad,dia)
    tarjeta = str(input("tiene tarjeta? Si/No: "))
    
    if tarjeta == "S" or "si" or "Si" or "s":
        tarjeta = True
    else:
        tarjeta = False 
    producto.calcular_precio_con_descuento(precio, cantidad, tarjeta)