
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

menu()

opciones()
