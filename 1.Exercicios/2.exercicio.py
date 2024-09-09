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

    def __str__(self) -> str:
        return f"Nome: {self.nome} \nE-mail: {self.email} \nSalario: {self.salario} \nEndereço: {self.endereco}"

    @abstractmethod
    def salario_final(self, salario) -> float:
        pass

    def salario_final(self, salario):
        try:
            self.__Verificar_salario(salario)
        except ValorNegativoError as error:
            return f"Erro: {error}"
        
        self._salario_final += salario
        return self._salario_final
    
    def __Verificar_salario(self, salario):
        if salario < 0:
            raise ValorNegativoError("Não é possivel inserir um valor negativo\n")
        

class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, cnh: str, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh = cnh

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCNH: {self.cnh}"
                )

class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, email, salario, endereco)


gerente1 = Gerente("João", "joao@gmail.com", 2000.00, Endereco("Rua a", "11", "Cidade A"))

motoboy1 = Motoboy("Maria", "maria@gmail.com", -1600.00, "123456", Endereco("Rua B", "110", "Cidade B"))

print(motoboy1)
print("\nSalario: ")
print(motoboy1.__Verificar_salario(-1600.00))
print(gerente1)
print(gerente1.__Verificar_salario(2000.00))
