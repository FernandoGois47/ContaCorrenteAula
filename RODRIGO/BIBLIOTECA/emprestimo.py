from historico import Historico
from multa import EstrategiaMulta, SemMulta  # Estratégias de multa

class EmprestimoLivro:
    def __init__(self, id, status="disponivel", estrategia_multa: EstrategiaMulta = SemMulta()):
        self._id = id
        self._status = status
        self.historico = Historico()
        self.estrategia_multa = estrategia_multa

    def emprestar(self):
        if self._status == "disponivel":
            self._status = "emprestado"
            print(f"Livro {self._id} emprestado com sucesso.") 
            self.historico.emprestimo.append("Emprestado")
        else:
            print(f"Livro {self._id} não está disponível para empréstimo.")  

    def definir_multa(self, estrategia_multa: EstrategiaMulta):
        self.estrategia_multa = estrategia_multa

    def devolver(self, dias):
        if self._status == "disponivel":
            print(f"Livro {self._id} já está disponível.")
            return

        self._status = "disponivel"
        print(f"Livro {self._id} devolvido com sucesso.")
        
        valor_multa = self.estrategia_multa.calcular_multa(dias)
        
        if valor_multa > 0:
            print(f"Multa aplicada: R$ {valor_multa:.2f}")
        else:
            print("Sem multa.")