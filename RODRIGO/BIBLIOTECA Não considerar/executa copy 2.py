from emprestimo import EmprestimoLivro
from aluno import Aluno
from historico import Historico

# Cadastra um aluno

# Cria um livro para empréstimo
_livro1 = EmprestimoLivro(numero_livro=101)

#Menu Aluno

Aluno("Fernando", "de Gois", "025.364.632-30"),


# Menu interação
while True:
    print("\n--- MENU BIBLIOTECA ---")
    print("1. Emprestar livro")
    print("2. Devolver livro")
    print("3. Ver histórico")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        _livro1.emprestar()  # Chama o método de empréstimo
    elif opcao == "2":
        _livro1.devolver()   # Chama o método de devolução
    elif opcao == "3":
        _livro1.historico.imprime()  # Exibe o histórico
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")

