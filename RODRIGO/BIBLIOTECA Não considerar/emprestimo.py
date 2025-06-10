from historico import Historico

class EmprestimoLivro:
    def __init__(self, numero_livro, status="disponivel"):
        self.numero_livro = numero_livro
        self._status = status
        self.historico = Historico()

      #metodos SET e GET encapsulamento
    def get_status(self):
        return self._status
    def set_status(self, status):
        self._saldo = status      

    def emprestar(self):
        if self.status == "disponivel":
            self.status = "emprestado"
            print(f"Livro {self.numero_livro} emprestado com sucesso.") 
            self.historico.emprestimo.append("Emprestado {}".format(self.status))
        else:
            print(f"Livro {self.numero_livro} não está disponível para empréstimo.")  

    def devolver(self):
        if self.status == "emprestado":
            self.status = "disponivel"
            print(f"Livro {self.numero_livro} devolvido com sucesso.")  
        else:
            print(f"Livro {self.numero_livro} já está aqui, ué?!.")  