import unittest
from src.password_toolkit import PasswordToolkit

class TestPasswordToolkit(unittest.TestCase):
    def setUp(self):
        self.toolkit = PasswordToolkit()
    
    def test_generar_contraseña(self):
        contraseña = self.toolkit.generar_contraseña(longitud=16)
        self.assertEqual(len(contraseña), 16)
    
    def test_contraseña_fuerte(self):
        self.assertTrue(self.toolkit.es_contraseña_fuerte("xQ3!k9@L$vB2#N")[0])
        self.assertFalse(self.toolkit.es_contraseña_fuerte("123456")[0])

if __name__ == "__main__":
    unittest.main()
