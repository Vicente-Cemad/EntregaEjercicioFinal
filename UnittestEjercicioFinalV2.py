
import unittest
from EntregaEjercicioFinalV2 import Producto, Inventario

class TestProducto(unittest.TestCase):

    def setUp(self):
        self.producto = Producto("a", "a", 1.5, 10)
        self.producto = Producto("b", "b", 2.5, 20)
        self.producto = Producto("c", "c", 3.5, 30)
        self.producto = Producto("d", "d", 4.5, 40)
        self.producto = Producto("e", "e", 5.5, 50)
        self.producto = Producto("f", "f", 6.5, 60)
        self.producto = Producto("g", "g", 7.5, 70)

    def test_validar_nombre(self):
        with self.assertRaises(ValueError):
            self.producto.validar_nombre("")
        with self.assertRaises(ValueError):
            self.producto.validar_nombre("123")
        self.producto.validar_nombre("h")

    def test_validar_categoria(self):
        with self.assertRaises(ValueError):
            self.producto.validar_categoria("")
        with self.assertRaises(ValueError):
            self.producto.validar_categoria("123")
        self.producto.validar_categoria("h")

    def test_validar_precio(self):
        with self.assertRaises(ValueError):
            self.producto.validar_precio(-1)
        self.producto.validar_precio(2.5)

    def test_validar_cantidad(self):
        with self.assertRaises(ValueError):
            self.producto.validar_cantidad(-1)
        self.producto.validar_cantidad(5)

class TestInventario(unittest.TestCase):

    def setUp(self):
        self.inventario = Inventario()
        self.producto = Producto("Manzana", "Fruta", 1.5, 10)
        self.inventario.agregar_producto("Manzana", self.producto)

    def test_agregar_producto(self):
        producto_nuevo = Producto("Pera", "Fruta", 2.0, 20)
        self.inventario.agregar_producto("Pera", producto_nuevo)
        self.assertEqual(len(self.inventario._Inventario__productos), 2)

    def test_buscar_producto(self):
        producto = self.inventario.buscar_producto("Manzana")
        self.assertIsNotNone(producto)
        with self.assertRaises(ValueError):
            self.inventario.buscar_producto("Pera")

    def test_actualizar_producto(self):
        producto_nuevo = Producto("Manzana", "Fruta", 2.0, 20)
        self.inventario.actualizar_producto(self.producto, producto_nuevo)
        producto_actualizado = self.inventario.buscar_producto("Manzana")
        self.assertEqual(producto_actualizado.get_precio(), 2.0)

    def test_eliminar_producto(self):
        self.inventario.eliminar_producto("Manzana")
        with self.assertRaises(ValueError):
            self.inventario.buscar_producto("Manzana")

if __name__ == '__main__':
    unittest.main()
