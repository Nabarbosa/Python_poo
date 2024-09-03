from abc import ABC, abstractmethod

import os

os.system("cls || clear")

class ValorNegativoError(Exception):
    pass

class Endereco:
    def __init__(self, logadouro: str, numero: str, cidade: str) -> None:
        self.logadouro = logadouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return f"Logadouro: {self.logadouro} \nNúmero: {self.numero} \nCidade: {self.cidade}"


class Funcionario(ABC):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

    def salario_final(self, salario) -> float:
        try:
            self.__Verificar_salario(salario)
        except ValorNegativoError as error:
            return f"Erro: {error}"
        
        self.salario_finalo += salario
        return self.salario_final
    
    def __Verificar_salario(self, salario):
        if salario < 0:
            raise ValorNegativoError("Não é possivel inserir um valor negativo")