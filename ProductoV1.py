
class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0")

    def __str__(self):
        return f"Producto(nombre={self.nombre}, categoria={self.categoria}, precio={self.precio}, cantidad={self.cantidad})"

nombre = input("Nombre del producto: ")
categoria = input("Categoría del producto: ")
precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad en stock: "))

print (nombre)
print (categoria)
print (precio)
print (cantidad)
