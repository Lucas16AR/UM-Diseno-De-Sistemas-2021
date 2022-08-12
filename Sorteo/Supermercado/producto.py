class Producto:

    def __init__(self, precio, codigo, descripcion):
        self.__codigo = codigo
        self.__precio = precio
        self.__descripcion = descripcion

    def __str__(self) -> str:
        return f'producto {self.__codigo} {self.__descripcion} {self.__precio}' 

    def __eq__(self, o: object) -> bool:
        if isinstance(o,Producto):
            return self.__codigo == o.codigo
        return False 

    def __hash__(self) -> int:
        return hash(self.__codigo)

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio: float):
        self.__precio = precio

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str):
        self.__descripcion = descripcion