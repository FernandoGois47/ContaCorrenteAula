from funcionario import Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, cpf, cargo, salario, senha, qtd_funcionarios):
        # self._nome = nome
        # self._cpf = cpf
        # self._cargo = cargo
        # self._salario = salario
        super().__init__(nome, cpf, cargo, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

    def autentica(self, senha):
        if self._senha == senha:
            print("Acesso permitido!")
            return True
        else:
            print("Acesso negado!")
            return False
        
    def get_bonificacao(self): #reescrita de método
        return super().get_bonificacao() + 1000.00