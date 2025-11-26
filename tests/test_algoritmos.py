import unittest
from algoritmos.algoritmo_01 import soma
from algoritmos.algoritmo_02 import fatorial
from algoritmos.algoritmo_03 import eh_palindromo

class TestAlgoritmos(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma([1, 2, 3]), 6)

    def test_fatorial(self):
        self.assertEqual(fatorial(5), 120)

    def test_palindromo(self):
        self.assertTrue(eh_palindromo("arara"))

if __name__ == "__main__":
    unittest.main()
