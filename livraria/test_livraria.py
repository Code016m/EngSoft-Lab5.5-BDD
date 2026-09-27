import unittest

from livraria import pesquisar_livros

class TestLivraria(unittest.TestCase):

    def test_usuario_pesquisa_um_livro(self):
        resultado = pesquisar_livros("Dom Casmurro")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["titulo"], "Dom Casmurro")

    def test_usuario_consulta_informacoes_do_livro(self):
        resultado = pesquisar_livros("Dom Casmurro")
        livro = resultado[0]
        self.assertEqual(livro["titulo"], "Dom Casmurro")
        self.assertEqual(livro["autor"], "Machado de Assis")
        self.assertEqual(livro["preco"], 30.0)

    def test_usuario_consulta_disponibilidade(self):
        resultado = pesquisar_livros("Dom Casmurro")
        livro = resultado[0]
        self.assertTrue(livro["disponivel"])

if __name__ == "__main__":
    unittest.main()