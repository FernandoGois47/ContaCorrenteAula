class Pessoa:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def exibirNome(self):
        print("O nome da pessoa é: ", self.nome)
    def exibirIdade(self):  
        print("Ele tem ", self.idade, " anos.")
    def exibirSalario(self):
        print("E seu salário é de R$ ", self.salario)


