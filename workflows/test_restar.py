import unittest
from restar import restar

class TestRestar(unittest.TestCase):
    def test_resta_positiva(self):
        self.assertEqual(restar(5, 3), 2)

    def test_resta_negativa(self):
        self.assertEqual(restar(-5, 3), -8)

    def test_resta_cero(self):
        self.assertEqual(restar(0, 3), -3)

if __name__ == '__main__':
    unittest.main()
