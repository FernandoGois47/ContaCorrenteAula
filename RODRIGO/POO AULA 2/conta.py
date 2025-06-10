class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        # metodos mágicos do python
        self.numero = numero
        self.titular = titular
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

    def pix(self):
        self.sacar -= valor 
        if(self.saldo < valor):
            return False
        else:
            return