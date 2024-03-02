import unittest
from multiplicar.py import multiplicar

class TestMultiplicar(unittest.TestCase):
    def test_multiplicacion_positiva(self):
        self.assertEqual(multiplicar(5, 3), 15)

    def test_multiplicacion_negativa(self):
        self.assertEqual(multiplicar(-5, 3), -15)

    def test_multiplicacion_cero(self):
        self.assertEqual(multiplicar(0, 3), 0)

if __name__ == '__main__':
    unittest.main()
