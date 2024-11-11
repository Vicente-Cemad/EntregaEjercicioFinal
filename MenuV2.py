
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

class Inventario:

    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                return producto
        return None

    def actualizar_producto(self, producto):
        nombre = input("Nombre del producto: ")
        if len(nombre) <= 0 or nombre.strip() == "" or nombre.strip() == " ":
            print("Nombre no válido")

        categoria = input("Categoría del producto: ")
        if len(categoria) <= 0 or categoria.strip() == "" or categoria.strip() == " ":
            print("Categoria no válida")

        precio = float(input("Precio del producto: "))
        if precio <= 0:
            print("Precio debe ser mayor que 0")

        cantidad = int(input("Cantidad en stock: "))
        if cantidad <= 0:
            print("Cantidad debe ser mayor que 0")

        producto.set_nombre(nombre)
        producto.set_categoria(categoria)
        producto.set_precio(precio)
        producto.set_cantidad(cantidad)
        return producto
        
    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        self.__productos.remove(producto)

    def mostrar_producto(self):
        print(producto)

    def mostrar_inventario(self):
        for producto in self.__productos:
            print(producto)

def menu():
    print("\nGestión de Inventario")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Mostrar inventario")
    print("5. Buscar producto")
    print("6. Salir")

def opciones():
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría del producto: ")
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad en stock: "))

    elif opcion == "2":
        nombre = input("Nombre del producto a actualizar: ")
        categoria = input("Nueva categoria del producto: ")
        precio = float(input("Nuevo precio del producto: "))
        cantidad = int(input("Nueva cantidad en stock: "))

    elif opcion == "3":
        nombre = input("Nombre del producto a eliminar: ")

    elif opcion == "4":
        inventario.mostrar_inventario()

    elif opcion == "5":
        nombre = input("Nombre del producto a buscar: ")
        producto = inventario.buscar_producto(nombre)

    elif opcion == "6":
        print("Saliendo del programa.")

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

inventario = Inventario()

menu()

opciones()
