import unittest
from EntregaEjercicioFinalV6 import Producto, Inventario

class TestProducto(unittest.TestCase):

    def test_validar_nombre(self):
        self.assertRaises(ValueError, Producto, "", "Fruta", 1.5, 10)
        self.assertRaises(ValueError, Producto, " ", "Fruta", 1.5, 10)
        self.assertRaises(ValueError, Producto, "123", "Fruta", 1.5, 10)
        self.producto.set_nombre("Pera")
        self.assertEqual(self.producto.get_nombre(), "Pera")

    def test_validar_categoria(self):
        self.assertRaises(ValueError, Producto, "Manzana", "", 1.5, 10)
        self.assertRaises(ValueError, Producto, "Manzana", " ", 1.5, 10)
        self.assertRaises(ValueError, Producto, "Manzana", "123", 1.5, 10)
        self.producto.set_categoria("Verdura")
        self.assertEqual(self.producto.get_categoria(), "Verdura")

    def test_validar_precio(self):
        self.assertRaises(ValueError, Producto, "Manzana", "Fruta", -1, 10)
        self.producto.set_precio(2.0)
        self.assertEqual(self.producto.get_precio(), 2.0)

    def test_validar_cantidad(self):
        self.assertRaises(ValueError, Producto, "Manzana", "Fruta", 1.5, -1)
        self.producto.set_cantidad(20)
        self.assertEqual(self.producto.get_cantidad(), 20)
'''        
    def setUp(self):
        self.producto = Producto("Manzana", "Fruta", 1.5, 10)
        self.producto = Producto("MANZANA", "Fruta", 1.5, 10)
        self.producto = Producto("pERA", "FRUTA", 1.5, 10)
        self.producto = Producto(" ", "FRUTA", 1.5, 10)
        self.producto = Producto("mandarina", " ", 1.5, 10)
        self.producto = Producto("mandarina", "cítrico", "", 10)
        self.producto = Producto("mandarina", "cítrico", .6, "")

    def setUp(self):
        self.inventario = Inventario()
        self.producto = Producto("Manzana", "Fruta", 1.5, 10)
        self.inventario.agregar_producto(self.producto)

    def test_agregar_producto(self):
        self.assertIn(self.producto, self.inventario._Inventario__lista)

    def test_validar_nombre(self):
        self.assertRaises(ValueError, Producto, "", "Fruta", 1.5, 10)
        self.assertRaises(ValueError, Producto, " ", "Fruta", 1.5, 10)
        self.assertRaises(ValueError, Producto, "123", "Fruta", 1.5, 10)
        self.producto.set_nombre("Pera")
        self.assertEqual(self.producto.get_nombre(), "Pera")

    def test_validar_categoria(self):
        self.assertRaises(ValueError, Producto, "Manzana", "", 1.5, 10)
        self.assertRaises(ValueError, Producto, "Manzana", " ", 1.5, 10)
        self.assertRaises(ValueError, Producto, "Manzana", "123", 1.5, 10)
        self.producto.set_categoria("Verdura")
        self.assertEqual(self.producto.get_categoria(), "Verdura")

    def test_validar_precio(self):
        self.assertRaises(ValueError, Producto, "Manzana", "Fruta", -1, 10)
        self.producto.set_precio(2.0)
        self.assertEqual(self.producto.get_precio(), 2.0)

    def test_validar_cantidad(self):
        self.assertRaises(ValueError, Producto, "Manzana", "Fruta", 1.5, -1)
        self.producto.set_cantidad(20)
        self.assertEqual(self.producto.get_cantidad(), 20)

class TestInventario(unittest.TestCase):

    def setUp(self):
        self.inventario = Inventario()
        self.producto = Producto("Manzana", "Fruta", 1.5, 10)
        self.inventario.agregar_producto(self.producto)

    def test_agregar_producto(self):
        self.assertIn(self.producto, self.inventario._Inventario__lista)

    def test_buscar_producto(self):
        self.assertEqual(self.inventario.buscar_producto("MANZANA"), self.producto)
        self.assertIsNone(self.inventario.buscar_producto("PERA"))

    def test_actualizar_producto(self):
        producto_nuevo = Producto("Manzana", "Fruta", 2.0, 15)
        self.inventario.actualizar_producto(self.producto, producto_nuevo)
        self.assertIn(producto_nuevo, self.inventario._Inventario__lista)
        self.assertNotIn(self.producto, self.inventario._Inventario__lista)

    def test_eliminar_producto(self):
        self.inventario.eliminar_producto("MANZANA")
        self.assertNotIn(self.producto, self.inventario._Inventario__lista)
'''
        
if __name__ == '__main__':
    unittest.main()
