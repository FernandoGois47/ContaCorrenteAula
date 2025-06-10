from conta import Conta #instanciar class conta

conta = Conta('123-4', 'Rodrigo', 120.0, 1000.0)
type(conta)

print(conta.titular)
conta.extrato()

conta.depositar(200.0)
conta.extrato()

conta.sacar(50.0)
conta.extrato()

consegui = conta.sacar(222.0)
if(consegui):
    print("Consegui Sacar")
    print("Restam ainda: {}".format(conta.saldo))
else:
    print("Saldo insuficiente!")