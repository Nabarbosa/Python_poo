import os

os.system("cls || clear")# Limpar terminal.

class Livro:
    # Ttulo, Autor, Número de páginas, preço.

    def __init__(self, titulo: str, autor: str, numero_paginas: int, preco: float) -> None:

        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.preco = preco

    def exibir_dados(self) -> str:
        return f"Título: {self.titulo} \nAutor: {self.autor} \nNúmero de páginas: {self.numero_paginas} páginas \nPreço: R$ {self.preco} \n "
    
primeiro_livro = Livro("A", "Abelha", 253, 30.00)
segundo_livro = Livro("B", "Baleia", 100, 15.00)

print(primeiro_livro.exibir_dados())
print(segundo_livro.exibir_dados())
        