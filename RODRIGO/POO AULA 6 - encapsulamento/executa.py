from conta import Conta
from cliente import Cliente

c1 = Cliente("Fernando","de Gois", "025.364.632-30")
c2 = Cliente("Pedro","Godinho","165.060.212-23")
c3 = Cliente("Pedro","Godinho","565.060.162-23")
conta1 = Conta("123-4", c1, 200.00)
conta2 = Conta("166-4", c2,300.00)
conta3 = Conta("166-5", c3,-100.00)

print(conta1.get_saldo())

conta3.set_saldo(conta1.get_saldo() + conta2.get_saldo())
print(conta3.get_saldo())