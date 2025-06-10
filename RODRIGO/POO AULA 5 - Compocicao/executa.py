from conta import Conta
from cliente import Cliente
c1 = Cliente("Fernando","de Gois", "025.364.632-30")
c2 = Cliente("Pedro","Godinho","165.060.212-23")
m1 = Conta("123-4", c1, 120.0, 1000.0)
m2 = Conta("166-4", c2, 120.0, 1000.0)

m1.depositar(100.00)
m1.extrato()
m1.sacar(50.00)
m1.extrato()
m1.transferencia(m2, 100.00)
m1.extrato()
m1.historico.imprime()
m2.historico.imprime()