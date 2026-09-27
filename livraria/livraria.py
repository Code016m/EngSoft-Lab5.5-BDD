def pesquisar_livros(termo):
    livros = listar_livros()
    resultado = []
    for livro in livros:
        if termo.lower() in livro["titulo"].lower():
            resultado.append(livro)
    return resultado

def listar_livros():
    return [
        {
            "titulo": "Dom Casmurro",
            "autor": "Machado de Assis",
            "preco": 30.0,
            "disponivel": True
        },
        {
            "titulo": "Memórias Póstumas de Brás Cubas",
            "autor": "Machado de Assis",
            "preco": 35.0,
            "disponivel": True
        },
        {
            "titulo": "O Cortiço",
            "autor": "Aluísio Azevedo",
            "preco": 25.0,
            "disponivel": False
        }
    ]