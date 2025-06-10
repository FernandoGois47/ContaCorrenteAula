# executar.py - Versão com banco de dados
import tkinter as tk
from tkinter import messagebox
from tela_cliente import tela_cliente
from tela_tecnico import tela_tecnico
from database import db

def abrir_tela_cliente():
    janela.destroy()
    tela_cliente()

def abrir_tela_tecnico():
    janela.destroy()
    tela_tecnico()

def inicializar_sistema():
    # Conecta com o banco de dados
    if db.conectar():
        messagebox.showinfo("Sucesso", "Conectado ao banco de dados!")
    else:
        messagebox.showerror("Erro", "Falha ao conectar com o banco de dados!\nVerifique se o XAMPP está rodando.")
        return False
    return True

# Inicializa o sistema
if not inicializar_sistema():
    exit()

janela = tk.Tk()
janela.title("Menu AproximaTI")
janela.geometry("300x150")

tk.Label(janela, text="Escolha o CRUD para abrir:", font=("Arial", 14)).pack(pady=10)

btn_cliente = tk.Button(janela, text="CRUD Cliente", width=20, command=abrir_tela_cliente)
btn_cliente.pack(pady=5)

btn_tecnico = tk.Button(janela, text="CRUD Técnico", width=20, command=abrir_tela_tecnico)
btn_tecnico.pack(pady=5)

# Fecha a conexão quando a janela for fechada
def on_closing():
    db.desconectar()
    janela.destroy()

janela.protocol("WM_DELETE_WINDOW", on_closing)
janela.mainloop()