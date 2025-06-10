from database import db

class Tecnico:
    def __init__(self, id=None, nome=None, email=None, senha=None, cidade=None, especialidade=None):
        self.id = id 
        self.nome = nome  
        self.email = email 
        self.senha = senha  
        self.cidade = cidade  
        self.especialidade = especialidade 

    def __repr__(self):
        return (f"Tecnico(id={self.id}, nome='{self.nome}', email='{self.email}', senha='{self.senha}', "
                f"cidade='{self.cidade}', especialidade='{self.especialidade}')")

def criar_tecnico(nome, email, senha, cidade, especialidade):
    if not db.connection:
        db.conectar()
    
    query = "INSERT INTO tecnico_especializacao (nome, email, senha, cidade, especialidade) VALUES (%s, %s, %s, %s, %s)"
    cursor = db.executar_query(query, (nome, email, senha, cidade, especialidade))
    
    if cursor:
        tecnico_id = cursor.lastrowid
        cursor.close()
        return Tecnico(tecnico_id, nome, email, senha, cidade, especialidade)
    return None

def listar_tecnicos():
    if not db.connection:
        db.conectar()
    
    query = "SELECT id, nome, email, senha, cidade, especialidade FROM tecnico_especializacao ORDER BY id DESC"
    resultados = db.buscar_dados(query)
    
    tecnicos = []
    for row in resultados:
        tecnico = Tecnico(row[0], row[1], row[2], row[3], row[4], row[5])
        tecnicos.append(tecnico)
    
    return tecnicos

def buscar_tecnico_por_id(id_tecnico):
    if not db.connection:
        db.conectar()
    
    query = "SELECT id, nome, email, senha, cidade, especialidade FROM tecnico_especializacao WHERE id = %s"
    resultados = db.buscar_dados(query, (id_tecnico,))
    
    if resultados:
        row = resultados[0]
        return Tecnico(row[0], row[1], row[2], row[3], row[4], row[5])
    return None

def atualizar_tecnico(id_alvo, novo_nome, novo_email, nova_senha, nova_cidade, nova_especialidade):
    if not db.connection:
        db.conectar()
    
    query = "UPDATE tecnico_especializacao SET nome = %s, email = %s, senha = %s, cidade = %s, especialidade = %s WHERE id = %s"
    cursor = db.executar_query(query, (novo_nome, novo_email, nova_senha, nova_cidade, nova_especialidade, id_alvo))
    
    if cursor:
        linhas_afetadas = cursor.rowcount
        cursor.close()
        return linhas_afetadas > 0
    return False

def deletar_tecnico(id_alvo):
    if not db.connection:
        db.conectar()
    
    query = "DELETE FROM tecnico_especializacao WHERE id = %s"
    cursor = db.executar_query(query, (id_alvo,))
    
    if cursor:
        linhas_afetadas = cursor.rowcount
        cursor.close()
        return linhas_afetadas > 0
    return False