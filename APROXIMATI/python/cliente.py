# cliente.py - Versão com banco de dados
from database import db

class Cliente:
    def __init__(self, id=None, nome=None, email=None, senha=None):
        self.id = id  
        self.nome = nome  
        self.email = email 
        self.senha = senha  

    def __repr__(self):
        return f"Cliente(id={self.id}, nome='{self.nome}', email='{self.email}', senha='{self.senha}')"

def criar_cliente(nome, email, senha):
    if not db.connection:
        db.conectar()
    
    query = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
    cursor = db.executar_query(query, (nome, email, senha))
    
    if cursor:
        cliente_id = cursor.lastrowid
        cursor.close()
        return Cliente(cliente_id, nome, email, senha)
    return None

def listar_clientes():
    if not db.connection:
        db.conectar()
    
    query = "SELECT id, nome, email, senha FROM usuarios ORDER BY id DESC"
    resultados = db.buscar_dados(query)
    
    clientes = []
    for row in resultados:
        cliente = Cliente(row[0], row[1], row[2], row[3])
        clientes.append(cliente)
    
    return clientes

def buscar_cliente_por_id(id_cliente):
    if not db.connection:
        db.conectar()
    
    query = "SELECT id, nome, email, senha FROM usuarios WHERE id = %s"
    resultados = db.buscar_dados(query, (id_cliente,))
    
    if resultados:
        row = resultados[0]
        return Cliente(row[0], row[1], row[2], row[3])
    return None

def atualizar_cliente(id_alvo, novo_nome, novo_email, nova_senha):
    if not db.connection:
        db.conectar()
    
    query = "UPDATE usuarios SET nome = %s, email = %s, senha = %s WHERE id = %s"
    cursor = db.executar_query(query, (novo_nome, novo_email, nova_senha, id_alvo))
    
    if cursor:
        linhas_afetadas = cursor.rowcount
        cursor.close()
        return linhas_afetadas > 0
    return False

def deletar_cliente(id_alvo):
    if not db.connection:
        db.conectar()
    
    query = "DELETE FROM usuarios WHERE id = %s"
    cursor = db.executar_query(query, (id_alvo,))
    
    if cursor:
        linhas_afetadas = cursor.rowcount
        cursor.close()
        return linhas_afetadas > 0
    return False