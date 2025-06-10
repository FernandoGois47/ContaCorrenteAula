from emprestimo import EmprestimoLivro
from aluno import Aluno
from historico import Historico

# Dados iniciais
alunos = {
    1: Aluno("Fernando", "de Gois", "025.364.632-30"),
    2: Aluno("Ricardo", "Lima", "055.434.622-05"),
}

# Criando alguns livros para teste
livros = {
    1: EmprestimoLivro(1),
    2: EmprestimoLivro(2),
    3: EmprestimoLivro(3),
}

# Função para validar entradas numéricas
def obter_numero(mensagem):
    while True:
        try:
            numero = input(mensagem)
            if not numero:  # Se a entrada estiver vazia
                print("Entrada inválida. Digite um número.")
                continue
            return int(numero)
        except ValueError:  # Se a conversão para int falhar
            print("Entrada inválida. Digite um número válido.")

def main():
    while True:
        # Exibir as opções disponíveis
        print("\n--- Sistema de Biblioteca ---")
        print("Escolha uma ação:")
        print("1. Emprestar um livro")
        print("2. Devolver um livro")
        print("3. Sair")

        # Solicitar a opção do usuário
        opcao = input("Digite o número da ação desejada: ")

        if opcao == "1":  # Emprestar um livro
            numero_aluno = obter_numero("Digite o ID do Aluno: ")
            if numero_aluno not in alunos:
                print("Aluno não encontrado.")
                continue

            numero_livro = obter_numero("Digite o número do livro que deseja emprestar: ")
            if numero_livro not in livros:
                print("Livro não encontrado.")
                continue

            if livros[numero_livro].emprestar():
                aluno = alunos[numero_aluno]
                print(f"O aluno {aluno.nome} {aluno.sobrenome} (CPF: {aluno.cpf}) emprestou o livro {numero_livro}.")
            else:
                print(f"O livro {numero_livro} já está emprestado.")

        elif opcao == "2":  # Devolver um livro
            numero_aluno = obter_numero("Digite o ID do Aluno: ")
            if numero_aluno not in alunos:
                print("Aluno não encontrado.")
                continue

            numero_livro = obter_numero("Digite o número do livro que deseja devolver: ")
            if numero_livro not in livros:
                print("Livro não encontrado.")
                continue

            if livros[numero_livro].devolver():
                aluno = alunos[numero_aluno]
                print(f"O aluno {aluno.nome} {aluno.sobrenome} (CPF: {aluno.cpf}) devolveu o livro {numero_livro}.")
            else:
                print(f"O livro {numero_livro} já está disponível.")

        elif opcao == "3":  # Sair do programa
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()