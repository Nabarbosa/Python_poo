import os

os.system("cls || clear")

class Endereco:
    def __init__(self, logadouro: str, numero: int) -> None:
        self.logadouro = logadouro
        self.numero = numero

    # def exibir_endereco(self) -> str:
    #     return f"\nLogadouro: {self.logadouro} \nNúmero: {self.numero}"
    
    def __str__ (self) -> str:
        return f"\nLogadouro: {self.logadouro} \nNúmero: {self.numero}"
    

class Aluno:
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        # Atributos.
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __str__ (self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} \nEndereço: {self.endereco}"
    

# Instanciar classes.
#endereco1 = Endereco("Rua A", 10)
#aluno = Aluno("Marta", 22, endereco1)

aluno = Aluno("Marta", 18, Endereco("Rua A", 10))

print(aluno)
