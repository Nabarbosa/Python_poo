from abc import ABC, abstractmethod
import os

os.system("cls || clear")

#Class endereço
class Endereco:
    def __init__(self, logadouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logadouro = logadouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

#to string
    def __str__(self) -> str:
        return f"Logadouro: {self.logadouro} \nNúmero: {self.numero} \nComplemento: {self.complemento} \nCEP: {self.cep} \nCidade: {self.cidade}"
        

#Abstract
class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email= email
        self.endereco = endereco
        self.salario = salario

    @abstractmethod
    def salario_final(self) -> float:
        pass

#to string
    def __str__(self) -> str:
        return f"Nome: {self.nome} \nTelefone: {self.telefone} \nE-mail: {self.email} \nSalario: {self.salario_final()} \n\n--- Endereço ---\n{self.endereco}\n"
    

#class engenheiro
class Engenheiro(Funcionario): 
    def __init__(self, nome: str, telefone: str, email: str, salario: float, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crea = crea

#salario final
    def salario_final(self) -> float:
        return 2000.0

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCREA: {self.crea}"
                )

#class medico
class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, crm: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crm = crm

    def salario_final(self) -> float:
        return 5000.0

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCRM: {self.crm}"
                )


engenheiro1 = Engenheiro("Mateus", "719635861", "mateus@gmail.com", 2000.00, "abc", Endereco("Rua A", "11B", "N/D", "41056325812", "Cidade A"))
print(f"\n== Dados do Engenheiro ==")
print(engenheiro1)


medico1 = Medico("Carla", "712658941", "carla@gmail.com", 5000.00, "AV123", Endereco("Rua B", "14B", "N/D", "741256389", "Cidade B"))
print(f"\n== Dados do Médico ==")
print(medico1)