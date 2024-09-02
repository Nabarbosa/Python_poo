from abc import ABC, abstractmethod
import os 

os.system("cls || clear") # Limpa terminal.

class Funcionario(ABC):
    # Construtor.
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario

    @abstractmethod
    def calcular_salario(self) -> float:
        pass


class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        # Acréscimo de 20%
        BONIFICACAO = 1.2
        salario_final = self.salario * BONIFICACAO
        return salario_final


class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh

    def calcular_salario(self) -> float:
        # Acréscimo de 10%
        BONIFICACAO = 1.1
        salario_final = self.salario * BONIFICACAO
        return salario_final


# Instanciar classes.

# funcionario1 = Funcionario("Jose", 36, 2500.00)
# print(f"Nome: {funcionario1.nome})


gerente1 = Gerente("Marta", 22, 2000.00)
print(f"Nome: {gerente1.nome}")
print(f"Sálario: {gerente1.calcular_salario()}")


mototboy1 = Motoboy("Jose", 32, 1000.00, "1322fgfdg")
print(f"Nome: {mototboy1.nome}")
print(f"Sálario: {mototboy1.calcular_salario()}")
print(f"CNH: {mototboy1.cnh}")