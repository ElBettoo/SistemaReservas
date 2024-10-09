import unittest
from DateTime import Fecha

class TestFecha(unittest.TestCase):
    
    def test_01_constructor(self):
        fecha = Fecha(2024, 9, 26, 20, 29, 30)
        self.assertTrue(isinstance(fecha, Fecha))