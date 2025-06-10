import tkinter as tk
from tkinter import messagebox
from cliente import criar_cliente, listar_clientes, deletar_cliente

def tela_cliente():
    clientes = listar_clientes()

    def atualizar_lista():
        listbox.delete(0, tk.END)
        for cliente in listar_clientes():
            listbox.insert(tk.END, f"{cliente.id} - {cliente.nome} ({cliente.email})")

    def limpar_campos():
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_senha.delete(0, tk.END)

    def botao_cadastrar():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()

        if nome and email and senha:
            criar_cliente(nome, email, senha)
            atualizar_lista()
            limpar_campos()
            messagebox.showinfo("Sucesso", "Cliente cadastrado!")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos.")

    def botao_deletar():
        try:
            selecionado = listbox.get(listbox.curselection())
            id_selecionado = int(selecionado.split(" - ")[0])
            deletar_cliente(id_selecionado)
            atualizar_lista()
            messagebox.showinfo("Sucesso", "Cliente deletado!")
        except:
            messagebox.showwarning("Erro", "Selecione um cliente para deletar.")

    janela = tk.Tk()
    janela.title("CRUD de Clientes - AproximaTI")
    janela.geometry("400x400")

    tk.Label(janela, text="Nome:").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Email:").pack()
    entry_email = tk.Entry(janela)
    entry_email.pack()

    tk.Label(janela, text="Senha:").pack()
    entry_senha = tk.Entry(janela, show="*")
    entry_senha.pack()

    tk.Button(janela, text="Cadastrar Cliente", command=botao_cadastrar).pack(pady=10)

    listbox = tk.Listbox(janela)
    listbox.pack(fill=tk.BOTH, expand=True)

    tk.Button(janela, text="Deletar Cliente", command=botao_deletar).pack(pady=5)

    atualizar_lista()
    janela.mainloop()
