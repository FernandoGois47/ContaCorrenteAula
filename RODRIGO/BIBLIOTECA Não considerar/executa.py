from emprestimo import EmprestimoLivro
from aluno import Aluno
from historico import Historico

# Cadastra um aluno

# Cria um livro para empréstimo
livro1 = EmprestimoLivro(numero_livro=101)

#Menu Aluno

Aluno("Fernando", "de Gois", "025.364.632-30"),


# Menu interação
while True:
    print("\n--- MENU BIBLIOTECA ---")
    print("1. Emprestar livro")
    print("2. Devolver livro")
    print("3. Ver histórico")
    print("4. Sair")
    print(livro1.get_status())
    opcao = input("Escolha uma opção: ")


    
    if opcao == "1":
        livro1.emprestar()  # Chama o método de empréstimo
    elif opcao == "2":
        livro1.devolver()   # Chama o método de devolução
    elif opcao == "3":
        livro1.historico.imprime()  # Exibe o histórico
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
        

