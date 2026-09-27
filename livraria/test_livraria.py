import unittest

from livraria import pesquisar_livro

class TestLivraria(unittest.TestCase):

    def test_usuario_pesquisa_um_livro(self):
        resultado = pesquisar_livro("Dom Casmurro")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["titulo"], "Dom Casmurro")

if __name__ == "__main__":
    unittest.main()