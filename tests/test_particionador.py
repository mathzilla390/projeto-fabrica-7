
import unittest
from particionador_shards import separar_pares_impares

class TestParticionador(unittest.TestCase):
    def test_misto_preserva_ordem(self):
        ids = [1024, 77, 0, -3, -2]
        pares, impares = separar_pares_impares(ids)
        self.assertEqual(pares, [1024, 0, -2])   # 0 é par, ordem preservada
        self.assertEqual(impares, [77, -3])

    def test_apenas_pares(self):
        ids = [2, 4, 6]
        pares, impares = separar_pares_impares(ids)
        self.assertEqual(pares, [2, 4, 6])
        self.assertEqual(impares, [])

    def test_apenas_impares(self):
        ids = [1, 3, 5]
        pares, impares = separar_pares_impares(ids)
        self.assertEqual(pares, [])
        self.assertEqual(impares, [1, 3, 5])

if __name__ == '__main__':
    unittest.main()
