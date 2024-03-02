import unittest
from dividir.py import dividir

class TestDividir(unittest.TestCase):
    def test_division_positiva(self):
        self.assertEqual(dividir(6, 3), 2)

    def test_division_negativa(self):
        self.assertEqual(dividir(-6, 3), -2)

    def test_division_cero(self):
        self.assertEqual(dividir(0, 5), 0)

    def test_division_por_cero(self):
        self.assertEqual(dividir(5, 0), "No se puede dividir por cero")

if __name__ == '__main__':
    unittest.main()
