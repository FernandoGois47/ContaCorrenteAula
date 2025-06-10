from emprestimo import EmprestimoLivro
from aluno import Aluno
from livros import Livros
from funcionario import Funcionario
from multa import SemMulta, MultaSimples, MultaGrave

# Dados iniciais
aluno = Aluno("Fernando", "de Gois", "0654646046-163")
funcionario = Funcionario("Carlos", "Aberto", "26516516-166", "123")
livro = Livros("Engenharia de Software", "Paula Filho", "Estudo", "1600")
emprestimo = EmprestimoLivro(livro.isbn, livro.status)

print("====Menu====")
print("Você é um:")
print("1 - Funcionário")
print("2 - Aluno")
opcao = int(input("Opção: "))

if opcao == 1:
    print(f"\nVocê é o Funcionário: {funcionario.nome} {funcionario.sobrenome}")
    print("Função em construção...")

elif opcao == 2:
    print(f"\nVocê é o Aluno: {aluno.nome} {aluno.sobrenome}")
    
    while True:  # Loop principal para o aluno
        print("\n======== Menu Aluno ========")
        print("1 - Emprestar Livro")
        print("2 - Devolver Livro")
        print("0 - Sair")
        opcao_aluno = int(input("Opção: "))
        
        if opcao_aluno == 0:
            print("Saindo...")
            break
            
        elif opcao_aluno == 1:
            if emprestimo._status == "disponivel":
                emprestimo.emprestar()
                print(f"\nLivro '{livro.titulo}' emprestado para {aluno.nome}")
            else:
                print("\nO livro já está emprestado!")
                
        elif opcao_aluno == 2:
            if emprestimo._status == "emprestado":
                try:
                    dias = int(input("\nQuantos dias você ficou com o livro? "))
                    
                    # Definir estratégia de multa
                    if dias <= 7:
                        emprestimo.definir_multa(SemMulta())
                    elif 8 <= dias <= 14:
                        emprestimo.definir_multa(MultaSimples())
                    else:
                        emprestimo.definir_multa(MultaGrave())
                    
                    emprestimo.devolver(dias)
                    print(f"\nLivro '{livro.titulo}' devolvido por {aluno.nome}")
                    
                except ValueError:
                    print("Digite um número válido de dias!")
            else:
                print("\nNão há livro para devolver - você não tem empréstimos ativos!")
        
        else:
            print("Opção inválida!")
else:
    print("Opção inválida!")