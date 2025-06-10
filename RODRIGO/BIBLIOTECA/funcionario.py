from aluno import Aluno

class Funcionario(Aluno):
    def __init__(self, nome, sobrenome, cpf, RA):
        super().__init__(nome, sobrenome, cpf)
        self._RA = RA

    @property
    def RA(self):
        return self._RA
