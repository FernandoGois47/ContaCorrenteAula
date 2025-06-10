from conta import Conta

c1 = Conta("123-4", "Rodrigo", 120.0, 1000.0)
c2 = Conta("153-4", "Fernando", 10.0, 1000.0)
c3 = Conta("156-4","Maloqueiro", 50000.0, 200.0)

print(c2.saldo)
# c1.depositar(100.0)
print(c1.saldo)
c2.depositar(300.0)
print(c2.saldo)
c2.transferencia(c1,30)
print(c1.saldo)
print(c2.saldo)
