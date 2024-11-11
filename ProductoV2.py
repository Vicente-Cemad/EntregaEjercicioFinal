
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

        if len(nombre) <= 0 or nombre.strip() == "" or nombre.strip() == " ":
            raise ValueError("Nombre no válido")
        if len(categoria) <= 0 or categoria.strip() == "" or categoria.strip() == " ":
            raise ValueError("Categoria no válida")
        if precio <= 0:
            raise ValueError("Precio debe ser mayor que 0")
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser mayor que 0")

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if len(nombre) <= 0 or nombre.strip() == "" or nombre.strip() == " ":
            raise ValueError("Nombre no válido")
        else:
            self.__nombre = nombre
        
    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        if len(categoria) <= 0 or categoria.strip() == "" or categoria.strip() == " ":
            raise ValueError("Categoria no válido")
        else:
            self.__categoria = categoria

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        if precio <= 0:
            raise ValueError("Precio debe ser mayor que 0")
        else:
            self.__precio = precio

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser mayor 0")
        else:
            self.__cantidad = cantidad

    def __str__(self):
        return f"Producto(nombre={self.__nombre}, categoria={self.__categoria}, precio={self.__precio}, cantidad={self.__cantidad})"

producto = Producto('a', 'a', 1, 1)

print (producto)

nombre = input("Nombre del producto: ")
categoria = input("Categoría del producto: ")
precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad en stock: "))

producto = Producto(nombre, categoria, precio, cantidad)

print (producto)
