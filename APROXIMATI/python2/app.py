import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime
import sqlite3
import os

class AproximaTI:
    def __init__(self):
        self.init_database()
        self.show_main_menu()

    def init_database(self):
        """Criar tabelas básicas se não existirem"""
        self.conn = sqlite3.connect('aproximati.db')
        cursor = self.conn.cursor()
        
        # # Tabela de clientes
        # cursor.execute('''
        #     CREATE TABLE IF NOT EXISTS clientes (
        #         id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         nome TEXT NOT NULL,
        #         email TEXT UNIQUE NOT NULL,
        #         telefone TEXT,
        #         endereco TEXT,
        #         data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        #     )
        # ''')
        
        # # Tabela de técnicos
        # cursor.execute('''
        #     CREATE TABLE IF NOT EXISTS tecnicos (
        #         id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         nome TEXT NOT NULL,
        #         email TEXT UNIQUE NOT NULL,
        #         telefone TEXT,
        #         especialidade TEXT,
        #         experiencia TEXT,
        #         preco_hora REAL,
        #         portfolio TEXT,
        #         data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        #     )
        # ''')
        
        # # Tabela de avaliações
        # cursor.execute('''
        #     CREATE TABLE IF NOT EXISTS avaliacoes (
        #         id INTEGER PRIMARY KEY AUTOINCREMENT,
        #         id_cliente INTEGER,
        #         id_tecnico INTEGER,
        #         nota INTEGER CHECK (nota >= 1 AND nota <= 5),
        #         comentario TEXT,
        #         data_avaliacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        #         FOREIGN KEY (id_cliente) REFERENCES clientes (id),
        #         FOREIGN KEY (id_tecnico) REFERENCES tecnicos (id)
        #     )
        # ''')
        
        self.conn.commit()

    def show_main_menu(self):
        """Tela principal com opções de cadastro"""
        self.main_window = tk.Tk()
        self.main_window.title("AproximaTI - Sistema de Conectividade")
        self.main_window.geometry("500x400")
        self.main_window.configure(bg='#2c3e50')
        
        # Centralizar janela
        self.main_window.eval('tk::PlaceWindow . center')
        
        # Título
        title_label = tk.Label(self.main_window, text="🔧 AproximaTI", 
                              font=('Arial', 24, 'bold'), fg='white', bg='#2c3e50')
        title_label.pack(pady=30)
        
        subtitle_label = tk.Label(self.main_window, text="Conectando Clientes e Técnicos de TI", 
                                 font=('Arial', 12), fg='#ecf0f1', bg='#2c3e50')
        subtitle_label.pack(pady=10)
        
        # Frame para botões
        buttons_frame = tk.Frame(self.main_window, bg='#2c3e50')
        buttons_frame.pack(expand=True)
        
        # Botão Cadastro Cliente
        btn_cliente = tk.Button(buttons_frame, text="👤 Sou Cliente\n(Buscar Técnicos)", 
                               command=self.open_cliente_window, 
                               font=('Arial', 14, 'bold'), 
                               bg='#3498db', fg='white', 
                               width=20, height=3,
                               cursor='hand2')
        btn_cliente.pack(pady=15)
        
        # Botão Cadastro Técnico
        btn_tecnico = tk.Button(buttons_frame, text="🛠️ Sou Técnico\n(Oferecer Serviços)", 
                               command=self.open_tecnico_window, 
                               font=('Arial', 14, 'bold'), 
                               bg='#27ae60', fg='white', 
                               width=20, height=3,
                               cursor='hand2')
        btn_tecnico.pack(pady=15)
        
        # Rodapé
        footer_label = tk.Label(self.main_window, text="Escolha sua opção para começar", 
                               font=('Arial', 10), fg='#bdc3c7', bg='#2c3e50')
        footer_label.pack(side='bottom', pady=20)
        
        self.main_window.mainloop()

    def open_cliente_window(self):
        """Abrir janela específica para clientes"""
        ClienteWindow(self)

    def open_tecnico_window(self):
        """Abrir janela específica para técnicos"""
        TecnicoWindow(self)

class ClienteWindow:
    def __init__(self, main_app):
        self.main_app = main_app
        self.conn = main_app.conn
        self.setup_window()

    def setup_window(self):
        self.window = tk.Toplevel()
        self.window.title("AproximaTI - Área do Cliente")
        self.window.geometry("800x600")
        self.window.configure(bg='#f8f9fa')
        
        # Título
        title_frame = tk.Frame(self.window, bg='#3498db', height=60)
        title_frame.pack(fill='x')
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="👤 Área do Cliente", 
                              font=('Arial', 18, 'bold'), fg='white', bg='#3498db')
        title_label.pack(expand=True)

        # Notebook para abas
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Criar abas
        self.create_cadastro_tab()
        self.create_busca_tab()
        self.create_avaliacao_tab()

    def create_cadastro_tab(self):
        """Aba para cadastro do cliente"""
        cadastro_frame = ttk.Frame(self.notebook)
        self.notebook.add(cadastro_frame, text="📝 Meu Cadastro")

        # Formulário
        form_frame = tk.LabelFrame(cadastro_frame, text="Cadastro do Cliente", 
                                  font=('Arial', 12, 'bold'), bg='#f8f9fa')
        form_frame.pack(fill='x', padx=20, pady=20)

        # Campos
        tk.Label(form_frame, text="Nome Completo:", bg='#f8f9fa').grid(row=0, column=0, sticky='w', padx=10, pady=10)
        self.entry_nome = tk.Entry(form_frame, width=40, font=('Arial', 11))
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Email:", bg='#f8f9fa').grid(row=1, column=0, sticky='w', padx=10, pady=10)
        self.entry_email = tk.Entry(form_frame, width=40, font=('Arial', 11))
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Telefone:", bg='#f8f9fa').grid(row=2, column=0, sticky='w', padx=10, pady=10)
        self.entry_telefone = tk.Entry(form_frame, width=40, font=('Arial', 11))
        self.entry_telefone.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Endereço:", bg='#f8f9fa').grid(row=3, column=0, sticky='w', padx=10, pady=10)
        self.entry_endereco = tk.Entry(form_frame, width=40, font=('Arial', 11))
        self.entry_endereco.grid(row=3, column=1, padx=10, pady=10)

        # Botões
        buttons_frame = tk.Frame(form_frame, bg='#f8f9fa')
        buttons_frame.grid(row=4, column=0, columnspan=2, pady=20)

        tk.Button(buttons_frame, text="Cadastrar", command=self.cadastrar_cliente, 
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold'), 
                 width=15).pack(side='left', padx=10)
        
        tk.Button(buttons_frame, text="Limpar", command=self.limpar_campos, 
                 bg='#95a5a6', fg='white', font=('Arial', 11, 'bold'), 
                 width=15).pack(side='left', padx=10)

    def create_busca_tab(self):
        """Aba para buscar técnicos"""
        busca_frame = ttk.Frame(self.notebook)
        self.notebook.add(busca_frame, text="🔍 Buscar Técnicos")

        # Filtros
        filter_frame = tk.LabelFrame(busca_frame, text="Filtros de Busca", 
                                   font=('Arial', 12, 'bold'))
        filter_frame.pack(fill='x', padx=20, pady=10)

        tk.Label(filter_frame, text="Especialidade:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
        self.combo_especialidade = ttk.Combobox(filter_frame, width=30, values=[
            'Todas', 'Desenvolvimento Web', 'Suporte Técnico', 'Redes', 
            'Banco de Dados', 'Segurança', 'Hardware', 'Mobile'
        ])
        self.combo_especialidade.grid(row=0, column=1, padx=10, pady=10)
        self.combo_especialidade.set('Todas')

        tk.Label(filter_frame, text="Preço máximo/hora:").grid(row=0, column=2, sticky='w', padx=10, pady=10)
        self.entry_preco_max = tk.Entry(filter_frame, width=15)
        self.entry_preco_max.grid(row=0, column=3, padx=10, pady=10)

        tk.Button(filter_frame, text="🔍 Buscar Técnicos", command=self.buscar_tecnicos, 
                 bg='#27ae60', fg='white', font=('Arial', 11, 'bold')).grid(row=1, column=0, columnspan=4, pady=15)

        # Resultados
        result_frame = tk.LabelFrame(busca_frame, text="Técnicos Disponíveis", 
                                   font=('Arial', 12, 'bold'))
        result_frame.pack(fill='both', expand=True, padx=20, pady=10)

        self.text_tecnicos = scrolledtext.ScrolledText(result_frame, height=20, font=('Arial', 10))
        self.text_tecnicos.pack(fill='both', expand=True, padx=10, pady=10)

    def create_avaliacao_tab(self):
        """Aba para avaliar técnicos"""
        avaliacao_frame = ttk.Frame(self.notebook)
        self.notebook.add(avaliacao_frame, text="⭐ Avaliar Técnico")

        # Formulário de avaliação
        form_frame = tk.LabelFrame(avaliacao_frame, text="Avaliar Atendimento", 
                                  font=('Arial', 12, 'bold'))
        form_frame.pack(fill='x', padx=20, pady=20)

        tk.Label(form_frame, text="Seu ID Cliente:").grid(row=0, column=0, sticky='w', padx=10, pady=10)
        self.entry_id_cliente = tk.Entry(form_frame, width=20)
        self.entry_id_cliente.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="ID do Técnico:").grid(row=0, column=2, sticky='w', padx=10, pady=10)
        self.entry_id_tecnico_aval = tk.Entry(form_frame, width=20)
        self.entry_id_tecnico_aval.grid(row=0, column=3, padx=10, pady=10)

        tk.Label(form_frame, text="Nota (1-5):").grid(row=1, column=0, sticky='w', padx=10, pady=10)
        self.combo_nota = ttk.Combobox(form_frame, width=17, values=['1', '2', '3', '4', '5'])
        self.combo_nota.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Comentário:").grid(row=2, column=0, sticky='nw', padx=10, pady=10)
        self.text_comentario = tk.Text(form_frame, width=50, height=4)
        self.text_comentario.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

        tk.Button(form_frame, text="⭐ Enviar Avaliação", command=self.avaliar_tecnico, 
                 bg='#f39c12', fg='white', font=('Arial', 11, 'bold')).grid(row=3, column=0, columnspan=4, pady=15)

        # Histórico de avaliações
        hist_frame = tk.LabelFrame(avaliacao_frame, text="Minhas Avaliações", 
                                 font=('Arial', 12, 'bold'))
        hist_frame.pack(fill='both', expand=True, padx=20, pady=10)

        self.text_avaliacoes = scrolledtext.ScrolledText(hist_frame, height=10, font=('Arial', 10))
        self.text_avaliacoes.pack(fill='both', expand=True, padx=10, pady=10)

    def cadastrar_cliente(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        telefone = self.entry_telefone.get().strip()
        endereco = self.entry_endereco.get().strip()

        if not nome or not email:
            messagebox.showwarning("Atenção", "Preencha pelo menos nome e email!")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO clientes (nome, email, telefone, endereco) VALUES (?, ?, ?, ?)", 
                          (nome, email, telefone, endereco))
            self.conn.commit()
            
            # Pegar o ID do cliente cadastrado
            cliente_id = cursor.lastrowid
            
            messagebox.showinfo("Sucesso!", f"Cliente cadastrado com sucesso!\nSeu ID é: {cliente_id}")
            self.limpar_campos()
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "Email já existe!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {str(e)}")

    def buscar_tecnicos(self):
        especialidade = self.combo_especialidade.get()
        preco_max = self.entry_preco_max.get().strip()

        try:
            cursor = self.conn.cursor()
            query = "SELECT * FROM tecnicos WHERE 1=1"
            params = []

            if especialidade != 'Todas':
                query += " AND especialidade LIKE ?"
                params.append(f"%{especialidade}%")

            if preco_max:
                query += " AND preco_hora <= ?"
                params.append(float(preco_max))

            query += " ORDER BY nome"
            cursor.execute(query, params)
            tecnicos = cursor.fetchall()

            self.text_tecnicos.delete("1.0", tk.END)
            
            if not tecnicos:
                self.text_tecnicos.insert(tk.END, "Nenhum técnico encontrado com os filtros especificados.")
                return

            self.text_tecnicos.insert(tk.END, "TÉCNICOS ENCONTRADOS:\n")
            self.text_tecnicos.insert(tk.END, "=" * 80 + "\n\n")

            for tecnico in tecnicos:
                # Buscar média de avaliações
                cursor.execute("SELECT AVG(nota), COUNT(*) FROM avaliacoes WHERE id_tecnico = ?", (tecnico[0],))
                aval_data = cursor.fetchone()
                media_nota = aval_data[0] if aval_data[0] else 0
                num_avaliacoes = aval_data[1]

                self.text_tecnicos.insert(tk.END, f"ID: {tecnico[0]}\n")
                self.text_tecnicos.insert(tk.END, f"Nome: {tecnico[1]}\n")
                self.text_tecnicos.insert(tk.END, f"Email: {tecnico[2]}\n")
                self.text_tecnicos.insert(tk.END, f"Telefone: {tecnico[3] or 'Não informado'}\n")
                self.text_tecnicos.insert(tk.END, f"Especialidade: {tecnico[4] or 'Não informado'}\n")
                self.text_tecnicos.insert(tk.END, f"Preço/hora: R$ {tecnico[6]:.2f}" if tecnico[6] else "Preço: A negociar\n")
                self.text_tecnicos.insert(tk.END, f"Avaliação: {media_nota:.1f}/5 ({num_avaliacoes} avaliações)\n")
                if tecnico[7]:  # Portfolio
                    self.text_tecnicos.insert(tk.END, f"Portfolio: {tecnico[7][:100]}...\n")
                self.text_tecnicos.insert(tk.END, "-" * 80 + "\n\n")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar técnicos: {str(e)}")

    def avaliar_tecnico(self):
        id_cliente = self.entry_id_cliente.get().strip()
        id_tecnico = self.entry_id_tecnico_aval.get().strip()
        nota = self.combo_nota.get()
        comentario = self.text_comentario.get("1.0", tk.END).strip()

        if not id_cliente or not id_tecnico or not nota:
            messagebox.showwarning("Atenção", "Preencha ID do cliente, ID do técnico e nota!")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO avaliacoes (id_cliente, id_tecnico, nota, comentario) VALUES (?, ?, ?, ?)", 
                          (int(id_cliente), int(id_tecnico), int(nota), comentario))
            self.conn.commit()
            messagebox.showinfo("Sucesso!", "Avaliação enviada com sucesso!")
            
            # Limpar campos
            self.entry_id_cliente.delete(0, tk.END)
            self.entry_id_tecnico_aval.delete(0, tk.END)
            self.combo_nota.set('')
            self.text_comentario.delete("1.0", tk.END)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao avaliar: {str(e)}")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_endereco.delete(0, tk.END)

class TecnicoWindow:
    def __init__(self, main_app):
        self.main_app = main_app
        self.conn = main_app.conn
        self.setup_window()

    def setup_window(self):
        self.window = tk.Toplevel()
        self.window.title("AproximaTI - Área do Técnico")
        self.window.geometry("800x600")
        self.window.configure(bg='#f8f9fa')
        
        # Título
        title_frame = tk.Frame(self.window, bg='#27ae60', height=60)
        title_frame.pack(fill='x')
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="🛠️ Área do Técnico", 
                              font=('Arial', 18, 'bold'), fg='white', bg='#27ae60')
        title_label.pack(expand=True)

        # Notebook para abas
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Criar abas
        self.create_cadastro_tab()
        self.create_portfolio_tab()
        self.create_avaliacoes_tab()

    def create_cadastro_tab(self):
        """Aba para cadastro do técnico"""
        cadastro_frame = ttk.Frame(self.notebook)
        self.notebook.add(cadastro_frame, text="📝 Meu Cadastro")

        # Formulário
        form_frame = tk.LabelFrame(cadastro_frame, text="Cadastro do Técnico", 
                                  font=('Arial', 12, 'bold'), bg='#f8f9fa')
        form_frame.pack(fill='x', padx=20, pady=20)

        # Campos
        tk.Label(form_frame, text="Nome Completo:", bg='#f8f9fa').grid(row=0, column=0, sticky='w', padx=10, pady=10)
        self.entry_nome = tk.Entry(form_frame, width=40, font=('Arial', 11))
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Email:", bg='#f8f9fa').grid(row=1, column=0, sticky='w', padx=10, pady=10)
        self.entry_email = tk.Entry(form_frame, width=40, font=('Arial', 11))
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Telefone:", bg='#f8f9fa').grid(row=2, column=0, sticky='w', padx=10, pady=10)
        self.entry_telefone = tk.Entry(form_frame, width=40, font=('Arial', 11))
        self.entry_telefone.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Especialidade:", bg='#f8f9fa').grid(row=3, column=0, sticky='w', padx=10, pady=10)
        self.combo_especialidade = ttk.Combobox(form_frame, width=37, values=[
            'Desenvolvimento Web', 'Suporte Técnico', 'Redes', 
            'Banco de Dados', 'Segurança', 'Hardware', 'Mobile'
        ])
        self.combo_especialidade.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Preço por Hora (R$):", bg='#f8f9fa').grid(row=4, column=0, sticky='w', padx=10, pady=10)
        self.entry_preco = tk.Entry(form_frame, width=40, font=('Arial', 11))
        self.entry_preco.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(form_frame, text="Experiência:", bg='#f8f9fa').grid(row=5, column=0, sticky='nw', padx=10, pady=10)
        self.text_experiencia = tk.Text(form_frame, width=40, height=3, font=('Arial', 11))
        self.text_experiencia.grid(row=5, column=1, padx=10, pady=10)

        # Botões
        buttons_frame = tk.Frame(form_frame, bg='#f8f9fa')
        buttons_frame.grid(row=6, column=0, columnspan=2, pady=20)

        tk.Button(buttons_frame, text="Cadastrar", command=self.cadastrar_tecnico, 
                 bg='#27ae60', fg='white', font=('Arial', 11, 'bold'), 
                 width=15).pack(side='left', padx=10)
        
        tk.Button(buttons_frame, text="Limpar", command=self.limpar_campos, 
                 bg='#95a5a6', fg='white', font=('Arial', 11, 'bold'), 
                 width=15).pack(side='left', padx=10)

    def create_portfolio_tab(self):
        """Aba para gerenciar portfólio"""
        portfolio_frame = ttk.Frame(self.notebook)
        self.notebook.add(portfolio_frame, text="💼 Meu Portfólio")

        # Formulário do portfólio
        form_frame = tk.LabelFrame(portfolio_frame, text="Descrição do Portfólio", 
                                  font=('Arial', 12, 'bold'))
        form_frame.pack(fill='both', expand=True, padx=20, pady=20)

        tk.Label(form_frame, text="ID do Técnico:").pack(anchor='w', padx=10, pady=(10,0))
        self.entry_id_tecnico = tk.Entry(form_frame, width=20, font=('Arial', 11))
        self.entry_id_tecnico.pack(anchor='w', padx=10, pady=(0,10))

        tk.Label(form_frame, text="Descrição do Portfólio:").pack(anchor='w', padx=10)
        self.text_portfolio = scrolledtext.ScrolledText(form_frame, height=15, font=('Arial', 11))
        self.text_portfolio.pack(fill='both', expand=True, padx=10, pady=10)

        # Botões
        buttons_frame = tk.Frame(form_frame)
        buttons_frame.pack(pady=10)

        tk.Button(buttons_frame, text="💾 Salvar Portfólio", command=self.salvar_portfolio, 
                 bg='#3498db', fg='white', font=('Arial', 11, 'bold')).pack(side='left', padx=10)
        
        tk.Button(buttons_frame, text="📂 Carregar Portfólio", command=self.carregar_portfolio, 
                 bg='#9b59b6', fg='white', font=('Arial', 11, 'bold')).pack(side='left', padx=10)

    def create_avaliacoes_tab(self):
        """Aba para ver avaliações recebidas"""
        avaliacoes_frame = ttk.Frame(self.notebook)
        self.notebook.add(avaliacoes_frame, text="⭐ Minhas Avaliações")

        # Campo para ID do técnico
        id_frame = tk.Frame(avaliacoes_frame)
        id_frame.pack(fill='x', padx=20, pady=10)

        tk.Label(id_frame, text="Meu ID:").pack(side='left')
        self.entry_id_tecnico_aval = tk.Entry(id_frame, width=15)
        self.entry_id_tecnico_aval.pack(side='left', padx=10)

        tk.Button(id_frame, text="📊 Ver Minhas Avaliações", command=self.ver_avaliacoes, 
                 bg='#f39c12', fg='white', font=('Arial', 11, 'bold')).pack(side='left', padx=10)

        # Área de resultados
        result_frame = tk.LabelFrame(avaliacoes_frame, text="Avaliações Recebidas", 
                                   font=('Arial', 12, 'bold'))
        result_frame.pack(fill='both', expand=True, padx=20, pady=10)

        self.text_minhas_avaliacoes = scrolledtext.ScrolledText(result_frame, height=20, font=('Arial', 10))
        self.text_minhas_avaliacoes.pack(fill='both', expand=True, padx=10, pady=10)

    def cadastrar_tecnico(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()
        telefone = self.entry_telefone.get().strip()
        especialidade = self.combo_especialidade.get()
        preco = self.entry_preco.get().strip()
        experiencia = self.text_experiencia.get("1.0", tk.END).strip()

        if not nome or not email:
            messagebox.showwarning("Atenção", "Preencha pelo menos nome e email!")
            return

        try:
            preco_val = float(preco) if preco else None
            cursor = self.conn.cursor()
            cursor.execute("""INSERT INTO tecnicos (nome, email, telefone, especialidade, experiencia, preco_hora) 
                             VALUES (?, ?, ?, ?, ?, ?)""", 
                          (nome, email, telefone, especialidade, experiencia, preco_val))
            self.conn.commit()
            
            # Pegar o ID do técnico cadastrado
            tecnico_id = cursor.lastrowid
            
            messagebox.showinfo("Sucesso!", f"Técnico cadastrado com sucesso!\nSeu ID é: {tecnico_id}")
            self.limpar_campos()
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "Email já existe!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {str(e)}")

    def salvar_portfolio(self):
        id_tecnico = self.entry_id_tecnico.get().strip()
        portfolio = self.text_portfolio.get("1.0", tk.END).strip()

        if not id_tecnico or not portfolio:
            messagebox.showwarning("Atenção", "Preencha o ID do técnico e a descrição do portfólio!")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE tecnicos SET portfolio = ? WHERE id = ?", (portfolio, int(id_tecnico)))
            if cursor.rowcount > 0:
                self.conn.commit()
                messagebox.showinfo("Sucesso!", "Portfólio salvo com sucesso!")
            else:
                messagebox.showwarning("Atenção", "Técnico não encontrado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar portfólio: {str(e)}")

    def carregar_portfolio(self):
        id_tecnico = self.entry_id_tecnico.get().strip()

        if not id_tecnico:
            messagebox.showwarning("Atenção", "Preencha o ID do técnico!")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT portfolio FROM tecnicos WHERE id = ?", (int(id_tecnico),))
            result = cursor.fetchone()
            
            if result:
                portfolio = result[0] if result[0] else ""
                self.text_portfolio.delete("1.0", tk.END)
                self.text_portfolio.insert("1.0", portfolio)
                messagebox.showinfo("Sucesso!", "Portfólio carregado!")
            else:
                messagebox.showwarning("Atenção", "Técnico não encontrado!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar portfólio: {str(e)}")

    def ver_avaliacoes(self):
        id_tecnico = self.entry_id_tecnico_aval.get().strip()

        if not id_tecnico:
            messagebox.showwarning("Atenção", "Preencha seu ID!")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT a.nota, a.comentario, a.data_avaliacao, c.nome 
                FROM avaliacoes a 
                JOIN clientes c ON a.id_cliente = c.id 
                WHERE a.id_tecnico = ? 
                ORDER BY a.data_avaliacao DESC
            """, (int(id_tecnico),))
            avaliacoes = cursor.fetchall()

            self.text_minhas_avaliacoes.delete("1.0", tk.END)

            if not avaliacoes:
                self.text_minhas_avaliacoes.insert(tk.END, "Você ainda não possui avaliações.")
                return

            # Calcular estatísticas
            cursor.execute("SELECT AVG(nota), COUNT(*) FROM avaliacoes WHERE id_tecnico = ?", (int(id_tecnico),))
            stats = cursor.fetchone()
            media_nota = stats[0] if stats[0] else 0
            total_avaliacoes = stats[1]

            self.text_minhas_avaliacoes.insert(tk.END, "MINHAS AVALIAÇÕES\n")
            self.text_minhas_avaliacoes.insert(tk.END, "=" * 60 + "\n\n")
            self.text_minhas_avaliacoes.insert(tk.END, f"Média Geral: {media_nota:.1f}/5 estrelas\n")
            self.text_minhas_avaliacoes.insert(tk.END, f"Total de Avaliações: {total_avaliacoes}\n\n")
            self.text_minhas_avaliacoes.insert(tk.END, "-" * 60 + "\n\n")

            for avaliacao in avaliacoes:
                nota, comentario, data, cliente_nome = avaliacao
                estrelas = "⭐" * int(nota) + "☆" * (5 - int(nota))
                
                self.text_minhas_avaliacoes.insert(tk.END, f"Cliente: {cliente_nome}\n")
                self.text_minhas_avaliacoes.insert(tk.END, f"Nota: {estrelas} ({nota}/5)\n")
                self.text_minhas_avaliacoes.insert(tk.END, f"Data: {data}\n")
                if comentario:
                    self.text_minhas_avaliacoes.insert(tk.END, f"Comentário: {comentario}\n")
                self.text_minhas_avaliacoes.insert(tk.END, "-" * 40 + "\n\n")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar avaliações: {str(e)}")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.combo_especialidade.set('')
        self.entry_preco.delete(0, tk.END)
        self.text_experiencia.delete("1.0", tk.END)


def main():
    app = AproximaTI()

if __name__ == "__main__":
    main()