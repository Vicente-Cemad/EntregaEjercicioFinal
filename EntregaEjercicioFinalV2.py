#Curso IBM SkillBuild 2024
#Script Python
#Vicente Medina Prados
#Empleando una lista - sin persistencia

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
            raise ('Volviendo a Menú')


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
            raise ('Volviendo a Menú') 

    def validar_precio(self, precio):
        #Precio
        try:
            if precio <= 0:
                print('Precio debe ser mayor que 0')
                raise ValueError("Precio debe ser mayor que 0")
            else:
                print('Precio correcto')
        except:
            raise ('Volviendo a Menú') 

    def validar_cantidad(self, cantidad):
        #Cantidad
        try:
            if cantidad <= 0:
                print('Cantidad debe ser mayor que 0')
                raise ValueError("Cantidad debe ser mayor que 0")
            else:
                print('Cantidad correcta')
        except:
            raise ('Volviendo a Menú') 

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
        try:
            for producto2 in self.__productos:
                if producto2.get_nombre() == nombre:
                    print('Nombre de producto duplicado. ¿Actualizar o eliminar?')
                    return producto2
            self.__productos.append(producto)
            print('Producto añadido')
        except:
            print ('ERROR NO ESPERADO EN INSERCIÓN DE PRODUCTO')            
            raise ('ERROR NO ESPERADO EN INSERCIÓN DE PRODUCTO') 

    def buscar_producto(self, nombre):
        try:
            if not self.__productos:
                producto = None
                return producto
            else:
                for producto in self.__productos:
                    if producto.get_nombre() == nombre:
                        print(producto)
                        return producto
                producto = False
                print('No existe el producto')
                return producto
        except:
            print ('ERROR NO ESPERADO EN BUSQUEDA POR NOMBRE')            
            raise ('ERROR NO ESPERADO EN BUSQUEDA POR NOMBRE') 
    

    def actualizar_producto(self, productoA, productoN):
        try:
            indice = self.__productos.index(productoA)
            self.__productos.insert(indice, productoN)
            self.__productos.remove(productoA)
        except:
            print ('ERROR NO ESPERADO EN ACTUALIZACIÓN DE PRODUCTO')            
            raise ('ERROR NO ESPERADO EN ACTUALIZACIÓN DE PRODUCTO') 

        
    def eliminar_producto(self, nombre):
        try:
            producto = self.buscar_producto(nombre)
            if producto == False:
                print('Introducir otro producto')
            elif producto == None:
                print('No hay productos en inventario')
            else:
                self.__productos.remove(producto)
                print('Producto eliminado')
        except:
            print ('ERROR NO ESPERADO EN ELIMINACIÓN DE PRODUCTO')            
            raise ('ERROR NO ESPERADO EN ELIMINACIÓN DE PRODUCTO') 
        

    def mostrar_producto(self):
        try:
            nombre = input("Nombre del producto a buscar: ")
            producto = None
            producto = self.buscar_producto(nombre)
            if producto == None:
                print('No hay productos en el inventario')
        except:
            print ('ERROR NO ESPERADO EN MOSTRAR PRODUCTO')            
            raise ('ERROR NO ESPERADO EN MOSTRAR PRODUCTO') 

    def mostrar_inventario(self):
        try:
            if not self.__productos:
                print('No hay productos en inventario')
            else:
                for producto in self.__productos:
                    print(producto)
        except:
            print ('ERROR NO ESPERADO EN MOSTRAR INVENTARIO')            
            raise ('ERROR NO ESPERADO EN MOSTRAAR INVENTARIO') 


def menu():
    print("\nGestión de Inventario")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Mostrar inventario")
    print("5. Buscar producto")
    print("6. Salir")

def main():

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
                    #Volviendo a Menú
                else:
                    try:
                        cantidad = int(input("Cantidad en inventario: "))
                        producto.validar_cantidad(cantidad)
                    except:
                        print('Debe ser númerico y entero')
                        #Volviendo a Menú
                    else:
                        producto = Producto(nombre, categoria, precio, cantidad)
                        print(producto)
                        inventario.agregar_producto(nombre, producto)
            except:
                #Volviendo a Menú
                print('Volviendo a Menú')

        elif opcion == "2":
            try:
                nombre = input("Nombre del producto a actualizar: ")
                productoA = inventario.buscar_producto(nombre)
                if productoA == False:
                    #Volviendo a Menú
                    print('Volviendo a Menú')
                elif productoA == None:
                    print('No hay productos en inventario')
                    #raise ValueError('No hay productos en inventario')
                else:
                    try:
                        categoria = input("Mantener o modificar categoría del producto: ")
                        producto.validar_categoria(categoria)
                        try:
                            precio = float(input("Mantener o modificar precio del producto: "))
                            producto.validar_precio(precio)
                        except:
                            print('Debe ser númerico con o sin decimales')
                            #Volviendo a Menú
                        else:
                            try:
                                cantidad = int(input("Mantener o modificar cantidad del producto: "))
                                producto.validar_cantidad(cantidad)
                            except:
                                print('Debe ser númerico y entero')
                                #Volviendo a Menú
                            else:
                                productoN = Producto(nombre, categoria, precio, cantidad)
                                print(productoN)
                                inventario.actualizar_producto(productoA, productoN)
                    except:
                        #Volviendo a Menú
                        print('Volviendo a Menú')
            except:
                #Volviendo a Menú
                print('Volviendo a Menú')

        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)

        elif opcion == "4":
            inventario.mostrar_inventario()

        elif opcion == "5":
            inventario.mostrar_producto()

        elif opcion == "6":
            print("Abandonando Aplicación")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    main()
