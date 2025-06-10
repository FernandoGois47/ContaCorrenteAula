class Conta:
    def __init__(self, numero, cliente, saldo, limite=1000.0):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor
        if(self.saldo < valor):
            return False
        else:
            return

    def extrato(self):
        print("numero: {} \nSaldo: {}".format(self.numero, self.saldo))

    def transferencia(self, destino, valor):
        retirou = self.sacar(valor)
        if(retirou == False):
            return False
        else:
            destino.depositar(valor)
            return True