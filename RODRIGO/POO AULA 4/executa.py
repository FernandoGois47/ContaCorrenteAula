from conta import Conta
from cliente import Cliente
c1 = Cliente("Fernando","de Gois", "025.364.632-30")
c2 = Cliente("Pedro","Godinho","165.060.212-23")
m1 = Conta("123-4", c1, 120.0, 1000.0)
m2 = Conta("166-4", c2, 120.0, 1000.0)

print(m2.titular.nome)
print(m2.titular.sobrenome)
print(m2.titular.cpf)

print(m2.__dict__)
print(m2.titular.__dict__)