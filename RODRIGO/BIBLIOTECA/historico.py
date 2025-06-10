import datetime

class Historico:
    def __init__(self):
        self.data_emprestimo = datetime.datetime.today()
        self.emprestimo = []        

    def imprime(self):
        print("Data do emprestimo: {}".format(self.data_emprestimo))
        print("Transações: ")
        for t in self.emprestimo:
            print("", t)