from funcionario import Funcionario
from gerente import Gerente

gerente = Gerente("Rodrigo", "465461446-165", "Gerente", 20000.00, "123", 12)

print(gerente.get_bonificacao())
#print(vars(gerente))
gerente.autentica("123")

funcionario = Funcionario("Alessandra", "46454646-131", "Analista", 5000.00)

print(funcionario.get_bonificacao())