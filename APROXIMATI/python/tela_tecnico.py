import tkinter as tk
from tkinter import messagebox
from tecnico import criar_tecnico, listar_tecnicos, deletar_tecnico

def tela_tecnico():
    def atualizar_lista():
        listbox.delete(0, tk.END)
        for tecnico in listar_tecnicos():
            listbox.insert(tk.END, f"{tecnico.id} - {tecnico.nome} ({tecnico.email})")

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_senha.delete(0, tk.END)
        entry_cidade.delete(0, tk.END)
        entry_especialidade.delete(0, tk.END)

    def botao_cadastrar():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()
        cidade = entry_cidade.get()
        especialidade = entry_especialidade.get()

        if nome and email and senha and cidade and especialidade:
            criar_tecnico(nome, email, senha, cidade, especialidade)
            atualizar_lista()
            limpar_campos()
            messagebox.showinfo("Sucesso", "Técnico cadastrado!")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    def botao_deletar():
        try:
            selecionado = listbox.get(listbox.curselection())
            id_selecionado = int(selecionado.split(" - ")[0])
            deletar_tecnico(id_selecionado)
            atualizar_lista()
            messagebox.showinfo("Sucesso", "Técnico deletado!")
        except:
            messagebox.showwarning("Erro", "Selecione um técnico para deletar.")

    janela = tk.Tk()
    janela.title("CRUD de Técnicos - AproximaTI")
    janela.geometry("450x450")

    tk.Label(janela, text="Nome:").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Email:").pack()
    entry_email = tk.Entry(janela)
    entry_email.pack()

    tk.Label(janela, text="Senha:").pack()
    entry_senha = tk.Entry(janela, show="*")
    entry_senha.pack()

    tk.Label(janela, text="Cidade:").pack()
    entry_cidade = tk.Entry(janela)
    entry_cidade.pack()

    tk.Label(janela, text="Especialidade:").pack()
    entry_especialidade = tk.Entry(janela)
    entry_especialidade.pack()

    tk.Button(janela, text="Cadastrar Técnico", command=botao_cadastrar).pack(pady=10)

    listbox = tk.Listbox(janela)
    listbox.pack(fill=tk.BOTH, expand=True)

    tk.Button(janela, text="Deletar Técnico", command=botao_deletar).pack(pady=5)

    atualizar_lista()
    janela.mainloop()
