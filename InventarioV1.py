
class Inventario:

    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        if self.buscar_producto(producto.get_nombre()) is None:
            self.__productos.append(producto)
        else:
            raise ValueError("El producto ya existe en el inventario")

    def actualizar_producto(self, nombre, precio=None, cantidad=None):
        producto = self.buscar_producto(nombre)
        if producto:
            if precio is not None:
                producto.set_precio(precio)
            if cantidad is not None:
                producto.set_cantidad(cantidad)
        else:
            raise ValueError("Producto no encontrado")

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self.__productos.remove(producto)
        else:
            raise ValueError("Producto no encontrado")

    def mostrar_inventario(self):
        for producto in self.__productos:
            print(producto)

    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                return producto
        return None

