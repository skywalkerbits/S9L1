import unittest
from operaciones import dividir, multiplicar, restar, sumar

class Test_Operaciones(unittest.TestCase):
 # division
    def test_division_positiva(self):
        self.assertEqual(dividir(6, 3), 2)

    def test_division_negativa(self):
        self.assertEqual(dividir(-6, 3), -2)

    def test_division_cero(self):
        self.assertEqual(dividir(0, 5), 0)

    def test_division_por_cero(self):
        self.assertEqual(dividir(5, 0), "No se puede dividir por cero")

 # multiplicacion
    def test_multiplicacion_positiva(self):
        self.assertEqual(multiplicar(5, 3), 15)

    def test_multiplicacion_negativa(self):
        self.assertEqual(multiplicar(-5, 3), -15)

    def test_multiplicacion_cero(self):
        self.assertEqual(multiplicar(0, 3), 0)
 # resta
        
    def test_resta_positiva(self):
        self.assertEqual(restar(5, 3), 2)

    def test_resta_negativa(self):
        self.assertEqual(restar(-5, 3), -8)

    def test_resta_cero(self):
        self.assertEqual(restar(0, 3), -3)
 
 # suma

    def test_sumar(self):
        self.assertEqual(sumar(3, 7), 10)
        self.assertEqual(sumar(-3, 3), 0)
        self.assertEqual(sumar(-2, -4), -6)