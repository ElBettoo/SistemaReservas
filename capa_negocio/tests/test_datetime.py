import unittest
from date_time import DateTime

class TestDateTime(unittest.TestCase):
    def setUp(self):
        self.datetime0 = DateTime(2024, 9, 26, 20, 29, 30)
        self.datetime1 = DateTime(2024, 9, 26, 20, 29, 30)
        self.datetime2 = DateTime(2024, 9, 28, 20, 29, 30)
        self.datetime3 = DateTime(2024, 8, 26, 20, 29, 30)
        self.datetime4 = DateTime(2024, 8, 26, 20, 29, 31)
        self.datetime5 = DateTime(2024, 8, 26, 20, 28, 30)
    
    def test_01_constructor(self):
        self.assertTrue(isinstance(self.datetime1, DateTime))

    def test_02_fecha_igual_fecha_devuelve_true_cuando_son_iguales(self):
        self.assertTrue(self.datetime0 == self.datetime1)

    def test_03_fecha_igual_fecha_devuelve_false_cuando_no_son_iguales(self):
        self.assertTrue(not (self.datetime2 == self.datetime1))

    def test_04_fecha_mayor_fecha_devuelve_true_cuando_es_mayor(self):
        self.assertTrue(self.datetime2 > self.datetime1)
    
    def test_05_fecha_mayor_fecha_devuelve_false_cuando_no_es_mayor(self):
        self.assertTrue(not (self.datetime3 > self.datetime1))

    def test_06_fecha_menor_fecha_devuelve_true_cuando_es_menor(self):
        self.assertTrue(self.datetime5 < self.datetime1)
    
    def test_07_fecha_menor_fecha_devuelve_false_cuando_no_es_menor(self):
        self.assertTrue(not (self.datetime4 < self.datetime5))