from enum import Enum

import os
os.system("cls||clear")

class Sexo(Enum):
    """Definindo valores Enum."""
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Pessoa:
    def __init__(self, nome: str, idade: int, sexo: Sexo) -> None:
        """Construtor."""
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def __str__(self) -> str:
        """Equivalente ao toString()do Java."""
        return (f"\n Nome: {self.nome}"
                f"\n Idade: {self.idade}"
                f"\n Sexo: {self.sexo.value}"
                )
    
"""Instanciando classe pessoa."""
pessoa_1 = Pessoa("Marta", 20, Sexo.FEMININO)

print(pessoa_1)