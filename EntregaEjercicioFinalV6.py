# Curso IBM SkillBuild 2024
# Script Python
# Vicente Medina Prados
# https://github.com/Vicente-Cemad/EntregaEjercicioFinal
# Empleando una lista - sin persistencia
# Se elimina la opción de modificación de "categoria"
# al no ser un requisito solicitado en el enunciado del proyecto

class Producto():
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad

    def validar_nombre(self):
        #Nombre
        try:
            if len(self.__nombre) <= 0:
                print('Nombre no puede dejarse vacío')
                raise ValueError("Nombre no puede dejarse vacío")
            elif self.__nombre.strip() == "":
                print('Nombre no puede dejarse vacío')
                raise ValueError("Nombre no puede dejarse vacío")
            elif self.__nombre.strip() == " ":
                print('Nombre no puede ser blancos')
                raise ValueError("Nombre no puede ser blancos")
            elif self.__nombre.isnumeric():
                print('Nombre no puede ser numérico')
                raise ValueError('Nombre no puede ser numérico')
            elif not self.__nombre.strip():
                print('Nombre no puede dejarse vacío')
                raise ValueError("Nombre no puede dejarse vacío")  
            else:
                print('Nombre correcto')
        except: 
            raise ValueError('Volviendo a Menú')


    def validar_categoria(self):
        #Categoría
        try:
            if len(self.__categoria) <= 0:
                print('Categoría no puede dejarse vacío')
                raise ValueError("Categoría no válida")
            elif self.__categoria.strip() == "":
                print('Categoría no puede dejarse vacío')
                raise ValueError("Categoría no válida")
            elif self.__categoria.strip() == " ":
                print('Categoría no puede ser blancos')
                raise ValueError("Categoría no válida")
            elif self.__categoria.isnumeric():
                print('Categoria no puede ser numérico')
                raise ValueError('Categoria no puede ser numérico')
            elif not self.__categoria.strip():
                print('Categoria no puede dejarse vacío')
                raise ValueError("Categoria no puede dejarse vacío")
            else:
                print('Categoría correcta')
        except:
            raise ValueError('Volviendo a Menú')

    def validar_precio(self):
        #Precio
        try:
            if self.__precio <= 0:
                print('Precio debe ser mayor que 0')
                raise ValueError("Precio debe ser mayor que 0")
            else:
                print('Precio correcto')
        except:
            raise ValueError('Volviendo a Menú') 

    def validar_cantidad(self):
        #Cantidad
        try:
            if self.__cantidad < 0:
                print('Cantidad debe ser mayor o igual que 0')
                raise ValueError("Cantidad debe ser mayor o igual que 0")
            else:
                print('Cantidad correcta')
        except:
            raise ValueError('Volviendo a Menú') 

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        #self.validar_nombre()
        self.__nombre = nombre
        
    def get_categoria(self):
        return self.__categoria

    def set_categoria(self, categoria):
        #self.validar_categoria()
        self.__categoria = categoria

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        #self.validar_precio()
        self.__precio = precio

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, cantidad):
        #self.validar_cantidad()
        self.__cantidad = cantidad

    def __str__(self):
        return f"Producto(nombre={self.__nombre}, categoria={self.__categoria}, precio={self.__precio}, cantidad={self.__cantidad})"

class Inventario():

    def __init__(self):
        self.__lista = []

    def existe_producto(self, nombre):
        try:
            for X in self.__lista:
                if X.get_nombre() == nombre:
                    #print('Nombre de producto duplicado. ¿Actualizar o eliminar?')
                    return X
        except:
            print ('ERROR NO ESPERADO EN EXISTE PRODUCTO')            
            raise ValueError('ERROR NO ESPERADO EN EXISTE PRODUCTO')           

    def agregar_producto(self, producto):
        try:
            self.__lista.append(producto)
            print('Producto añadido')
        except:
            print ('ERROR NO ESPERADO EN INSERCIÓN DE PRODUCTO')            
            raise ValueError('ERROR NO ESPERADO EN INSERCIÓN DE PRODUCTO') 

    def buscar_producto(self, nombre):
        try:
            if not self.__lista:
                X = None
                return X
            else:
                for X in self.__lista:
                    if X.get_nombre() == nombre:
                        print(X)
                        return X
                X = False
                print('No existe el producto')
                return X
        except:
            print ('ERROR NO ESPERADO EN BUSQUEDA POR NOMBRE')            
            raise ValueError('ERROR NO ESPERADO EN BUSQUEDA POR NOMBRE') 
    

    def actualizar_producto(self, producto, productoB):
        try:
            indice = self.__lista.index(producto)
            self.__lista.insert(indice, productoB)
            self.__lista.remove(producto)
        except:
            print ('ERROR NO ESPERADO EN ACTUALIZACIÓN DE PRODUCTO')            
            raise ValueError('ERROR NO ESPERADO EN ACTUALIZACIÓN DE PRODUCTO') 

        
    def eliminar_producto(self, nombre):
        try:
            producto = self.buscar_producto(nombre)
            if producto == False:
                print('Introducir otro producto')
            elif producto == None:
                print('No hay productos en inventario')
            else:
                self.__lista.remove(producto)
                print('Producto eliminado')
        except:
            print ('ERROR NO ESPERADO EN ELIMINACIÓN DE PRODUCTO')            
            raise ValueError('ERROR NO ESPERADO EN ELIMINACIÓN DE PRODUCTO') 
        

    def mostrar_producto(self):
        try:
            nombreA = input("Nombre del producto a buscar: ")
            nombre = nombreA.upper()
            producto = self.buscar_producto(nombre)
            if producto == None:
                print('No hay productos en el inventario')
        except:
            print ('ERROR NO ESPERADO EN MOSTRAR PRODUCTO')            
            raise ValueError('ERROR NO ESPERADO EN MOSTRAR PRODUCTO') 

    def mostrar_inventario(self):
        try:
            if not self.__lista:
                print('No hay productos en inventario')
            else:
                for X in self.__lista:
                    print(X)
        except:
            print ('ERROR NO ESPERADO EN MOSTRAR INVENTARIO')            
            raise ValueError('ERROR NO ESPERADO EN MOSTRAR INVENTARIO') 

    def __str__(self):
        return f"Inventario(nombre={self.__nombre}, producto={self.__producto})"

def menu():
    print("\nGestión de Inventario")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Mostrar inventario")
    print("5. Buscar producto")
    print("6. Salir")

def main():

    inventario = Inventario()

    while True:
        
        menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            #producto = Producto(nombre=None, categoria=None, precio=None, cantidad=None)
            try:
                nombreA = input("Nombre del producto: ")
                nombre = nombreA.upper()
                producto = Producto(nombre, None, None, None)
                producto.validar_nombre()
                # antes de continuar con la inserción, comprueba su existencia, ofreciendo su eliminación o actualización
                X = None
                X = inventario.existe_producto(nombre)
                if X != None:
                    print(f'Producto {nombre} duplicado. ¿Actualizar o eliminar?')
                    raise ValueError('Nombre de producto duplicado. ¿Actualizar o eliminar?')
                categoriaA = input("Categoría del producto: ")
                categoria = categoriaA.upper()
                producto.set_categoria(categoria)
                producto.validar_categoria()
                try:
                    precio = float(input("Precio del producto: "))
                    producto.set_precio(precio)
                    producto.validar_precio()
                except:
                    print('Solo números con o sin decimales ¡con .!')
                    #Volviendo a Menú
                else:
                    try:
                        cantidad = int(input("Cantidad en inventario: "))
                        producto.set_cantidad(cantidad)
                        producto.validar_cantidad()
                    except:
                        print('Debe ser "solo" números enteros')
                        #Volviendo a Menú
                    else:
                        print(producto)
                        inventario.agregar_producto(producto)
            except:
                #Volviendo a Menú
                print('Volviendo a Menú')

        elif opcion == "2":
            try:
                nombreA = input("Nombre del producto a actualizar: ")
                nombre = nombreA.upper()
                producto = inventario.buscar_producto(nombre)
                if producto == False:
                    #Volviendo a Menú
                    print('Volviendo a Menú')
                elif producto == None:
                    print('No hay productos en inventario')
                    raise ValueError('No hay lista en inventario')
                else:
                    try:
                        # categoriaA = input("Mantener o modificar categoría del producto: ")
                        # categoria = categoriaA.upper()
                        # productoB = Producto(nombre, categoria, None, None)
                        # productoB.validar_categoria()
                        categoria = producto.get_categoria()
                        productoB = Producto(nombre, categoria, None, None)
                        try:
                            precio = float(input("Mantener o modificar precio del producto: "))
                            productoB.set_precio(precio)
                            productoB.validar_precio()
                        except:
                            print('Solo números con o sin decimales ¡con .!')
                            #Volviendo a Menú
                        else:
                            try:
                                cantidad = int(input("Mantener o modificar cantidad del producto: "))
                                productoB.set_cantidad(cantidad)
                                productoB.validar_cantidad()
                            except:
                                print('Debe ser númerico y entero')
                                #Volviendo a Menú
                            else:
                                print(productoB)
                                inventario.actualizar_producto(producto, productoB)
                    except:
                        #Volviendo a Menú
                        print('Volviendo a Menú')
            except:
                #Volviendo a Menú
                print('Volviendo a Menú')

        elif opcion == "3":
            nombreA = input("Nombre del producto a eliminar: ")
            nombre = nombreA.upper()
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
