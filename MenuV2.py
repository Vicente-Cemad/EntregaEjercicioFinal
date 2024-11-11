
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    def validar_nombre(self, nombre):
        #Nombre
        try:
            if len(nombre) <= 0:
                print('Nombre no puede dejarse vacío')
                raise ValueError("Nombre no válido")
            elif nombre.strip() == "":
                print('Nombre no puede dejarse vacío')
                raise ValueError("Nombre no válido")
            elif nombre.strip() == " ":
                print('Nombre no puede ser blancos')
                raise ValueError("Nombre no válido")
            else:
                print('Nombre correcto')
        except:
            print('Volver al menú')

    def validar_categoria(self, categoria):
        #Categoría
        try:
            if len(categoria) <= 0:
                print('Categoría no puede dejarse vacío')
                raise ValueError("Categoría no válida")
            elif categoria.strip() == "":
                print('Categoría no puede dejarse vacío')
                raise ValueError("Categoría no válida")
            elif categoria.strip() == " ":
                print('Categoría no puede ser blancos')
                raise ValueError("Categoría no válida")
            else:
                print('Categoría correcta')
        except:
            print('Volver al menú')

    def validar_precio(self, precio):
        #Precio
        try:
            if precio <= 0:
                print('Precio debe ser mayor que 0')
                raise ValueError("Precio debe ser mayor que 0")
            else:
                print('Precio correcto')
        except:
            print('Volver al menú')

    def validar_cantidad(self, cantidad):
        #Cantidad
        try:
            if cantidad <= 0:
                print('Cantidad debe ser mayor que 0')
                raise ValueError("Cantidad debe ser mayor que 0")
            else:
                print('Cantidad correcta')
        except:
            print('Volver al menú')

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.validar_nombre(nombre)
        self.__nombre = nombre
        
    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        self.validar_categoria(categoria)
        self.__categoria = categoria

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.validar_precio(precio)
        self.__precio = precio

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        self.validar_cantidad(cantidad)
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
        print('No existe el producto')
        raise ValueError("No existe el producto")

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

    producto = Producto(nombre=None, categoria=None, precio=None, cantidad=None)
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            producto.set_nombre(nombre)
            categoria = input("Categoría del producto: ")
            producto.set_categoria(categoria)
            try:
                precio = float(input("Precio del producto: "))
                producto.set_precio(precio)
            except:
                print('Debe ser númerico con o sin decimales')
            try:
                cantidad = int(input("Cantidad en stock: "))
                producto.set_cantidad(cantidad)
            except:
                print('Debe ser númerico y entero')
            
            print(producto)

        elif opcion == "2":
            nombre = input("Nombre del producto a actualizar: ")
            producto = inventario.buscar_producto(nombre)
            categoria = input("Nueva categoría del producto: ")
            producto.set_categoria(categoria)
            try:
                precio = float(input("Nuevo precio del producto: "))
                producto.set_precio(precio)
            except:
                print('Debe ser númerico con o sin decimales')
            try:
                cantidad = int(input("Nueva cantidad en stock: "))
                producto.set_cantidad(cantidad)
            except:
                print('Debe ser númerico y entero')
            
            print(producto)
            return producto
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
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

opciones()
