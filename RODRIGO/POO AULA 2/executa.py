from conta import Conta

c1 = Conta("123-4", "Rodrigo", 120.0, 1000.0)
c2 = Conta("153-4", "Fernando", 30.0, 1000.0)
# c1 é um atributo de referência para um objeto para que isso ocorra no python são acionados de forma transparente os métodos mágicos 
# __new__() e __init__() responsáveis por construir e iniciar objetos.
c3 = Conta("156-4","Malaqueiro", 50000.0, 200.0)

# print(c2.saldo)
# c2.depositar(0.50)
# print(c2.saldo)

# print(c1.saldo)
# c1.depositar(10000.0)
# print(c1.saldo)

if(c1 == c3):
    print("Contas são iguais")
else:
    print("Contas são diferentes")