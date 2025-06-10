class Aluno:
    def __init__(self, nome: str, sobrenome: str, cpf: str):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    
    @property
    def sobrenome(self):
        return self.__sobrenome
    
    @property
    def cpf(self):
        return self.__cpf
