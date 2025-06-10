from historico import Historico

class Conta:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, saldo):
        if(self._saldo < 0):
            print("Saldo não pode ser negativo!")
        else:
            self._saldo = saldo
      