
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
            elif nombre.isnumeric():
                print('Nombre no puede ser numérico')
                raise ValueError('Nombre no puede ser numérico')
            else:
                print('Nombre correcto')
        except:
            raise ValueError('Volver al menú')

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
            elif categoria.isnumeric():
                print('Categoria no puede ser numérico')
                raise ValueError('Categoria no puede ser numérico')
            else:
                print('Categoría correcta')
        except:
            raise ValueError('Volver al menú')

    def validar_precio(self, precio):
        #Precio
        try:
            if precio <= 0:
                print('Precio debe ser mayor que 0')
                raise ValueError("Precio debe ser mayor que 0")
            else:
                print('Precio correcto')
        except:
            raise ValueError('Volver al menú')

    def validar_cantidad(self, cantidad):
        #Cantidad
        try:
            if cantidad <= 0:
                print('Cantidad debe ser mayor que 0')
                raise ValueError("Cantidad debe ser mayor que 0")
            else:
                print('Cantidad correcta')
        except:
            raise ValueError('Volver al menú')

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

    def agregar_producto(self, nombre, producto):
        for producto2 in self.__productos:
            if producto2.get_nombre() == nombre:
                print('Nombre de producto duplicado. ¿Actualizar o eliminar?')
                return producto2
        self.__productos.append(producto)
        print('Producto añadido')

    def buscar_producto(self, nombre):
        if not self.__productos:
            print('No hay productos en inventario')
            raise ValueError('No hay productos en inventario')
        else:
            for producto in self.__productos:
                if producto.get_nombre() == nombre:
                    print(producto)
                    return producto
            print('No existe el producto')
            raise ValueError('No existe el producto')

    def actualizar_producto(self, productoA, productoN):
        try:
            indice = self.__productos.index(productoA)
            self.__productos.insert(indice, productoN)
            self.__productos.remove(productoA)
        except:
            print('ERROR, en actualización')
            raise ValueError('ERROR, en actualización')

        
    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        print(producto)
        self.__productos.remove(producto)

    def mostrar_producto(self):
        nombre = input("Nombre del producto a buscar: ")
        self.buscar_producto(nombre)

    def mostrar_inventario(self):
        if not self.__productos:
            print('No hay productos en inventario')
        else:
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
            try:
                nombre = input("Nombre del producto: ")
                producto.validar_nombre(nombre)
                categoria = input("Categoría del producto: ")
                producto.validar_categoria(categoria)
                try:
                    precio = float(input("Precio del producto: "))
                    producto.validar_precio(precio)
                except:
                    print('Debe ser númerico con o sin decimales')
                    #Volver al menú
                else:
                    try:
                        cantidad = int(input("Cantidad en stock: "))
                        producto.validar_cantidad(cantidad)
                    except:
                        print('Debe ser númerico y entero')
                        #Volver al menú
                    else:
                        producto = Producto(nombre, categoria, precio, cantidad)
                        print(producto)
                        inventario.agregar_producto(nombre, producto)
            except:
                #Volver al menú
                print('Volver al menú')

        elif opcion == "2":
            try:
                nombre = input("Nombre del producto a actualizar: ")
                productoA = inventario.buscar_producto(nombre)
                try:
                    categoria = input("Mantener o modificar categoría del producto: ")
                    producto.validar_categoria(categoria)
                    try:
                        precio = float(input("Mantener o modificar precio del producto: "))
                        producto.validar_precio(precio)
                    except:
                        print('Debe ser númerico con o sin decimales')
                        #Volver al menú
                    else:
                        try:
                            cantidad = int(input("Mantener o modificar cantidad del producto: "))
                            producto.validar_cantidad(cantidad)
                        except:
                            print('Debe ser númerico y entero')
                            #Volver al menú
                        else:
                            productoN = Producto(nombre, categoria, precio, cantidad)
                            print(productoN)
                            inventario.actualizar_producto(productoA, productoN)
                except:
                    #Volver al menú
                    print('Volver al menú')
            except:
                #Volver al menú
                print('Volver al menú')

        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            inventario.mostrar_producto()

        elif opcion == "6":
            print("Saliendo del programa")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

opciones()
