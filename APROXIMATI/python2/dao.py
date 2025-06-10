import mysql.connector
from models import Usuario, Servico, Atendimento, Avaliacao, Contato, Especializacao, Portfolio

class Database:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='aproximati'
        )
        self.cursor = self.conexao.cursor()

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()

class UsuarioDAO:
    def __init__(self):
        self.db = Database()

    def criar(self, usuario):
        sql = "INSERT INTO usuarios (nome, email, senha, tipo) VALUES (%s, %s, %s, %s)"
        self.db.cursor.execute(sql, (usuario.nome, usuario.email, usuario.senha, usuario.tipo))
        self.db.conexao.commit()
        return self.db.cursor.lastrowid

    def listar(self):
        self.db.cursor.execute("SELECT * FROM usuarios ORDER BY nome")
        return self.db.cursor.fetchall()

    def listar_por_tipo(self, tipo):
        sql = "SELECT * FROM usuarios WHERE tipo = %s ORDER BY nome"
        self.db.cursor.execute(sql, (tipo,))
        return self.db.cursor.fetchall()

    def buscar_por_id(self, id):
        sql = "SELECT * FROM usuarios WHERE id = %s"
        self.db.cursor.execute(sql, (id,))
        return self.db.cursor.fetchone()

    def atualizar(self, usuario):
        sql = "UPDATE usuarios SET nome = %s, email = %s, senha = %s, tipo = %s WHERE id = %s"
        self.db.cursor.execute(sql, (usuario.nome, usuario.email, usuario.senha, usuario.tipo, usuario.id))
        self.db.conexao.commit()

    def deletar(self, id):
        sql = "DELETE FROM usuarios WHERE id = %s"
        self.db.cursor.execute(sql, (id,))
        self.db.conexao.commit()

class ServicoDAO:
    def __init__(self):
        self.db = Database()

    def criar(self, servico):
        sql = "INSERT INTO servicos (id_tecnico, titulo, descricao, preco, categoria) VALUES (%s, %s, %s, %s, %s)"
        self.db.cursor.execute(sql, (servico.id_tecnico, servico.titulo, servico.descricao, servico.preco, servico.categoria))
        self.db.conexao.commit()
        return self.db.cursor.lastrowid

    def listar(self):
        sql = """
        SELECT s.id, s.id_tecnico, u.nome as nome_tecnico, s.titulo, s.descricao, 
               s.preco, s.categoria, s.data_publicacao
        FROM servicos s
        JOIN usuarios u ON s.id_tecnico = u.id
        ORDER BY s.data_publicacao DESC
        """
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()

    def listar_por_tecnico(self, id_tecnico):
        sql = """
        SELECT s.id, s.id_tecnico, u.nome as nome_tecnico, s.titulo, s.descricao, 
               s.preco, s.categoria, s.data_publicacao
        FROM servicos s
        JOIN usuarios u ON s.id_tecnico = u.id
        WHERE s.id_tecnico = %s
        ORDER BY s.data_publicacao DESC
        """
        self.db.cursor.execute(sql, (id_tecnico,))
        return self.db.cursor.fetchall()

    def buscar_por_id(self, id):
        sql = "SELECT * FROM servicos WHERE id = %s"
        self.db.cursor.execute(sql, (id,))
        return self.db.cursor.fetchone()

    def atualizar(self, servico):
        sql = "UPDATE servicos SET titulo = %s, descricao = %s, preco = %s, categoria = %s WHERE id = %s"
        self.db.cursor.execute(sql, (servico.titulo, servico.descricao, servico.preco, servico.categoria, servico.id))
        self.db.conexao.commit()

    def deletar(self, id):
        sql = "DELETE FROM servicos WHERE id = %s"
        self.db.cursor.execute(sql, (id,))
        self.db.conexao.commit()

class AtendimentoDAO:
    def __init__(self):
        self.db = Database()

    def criar(self, atendimento):
        sql = "INSERT INTO atendimentos (id_servico, id_tecnico, id_cliente, status) VALUES (%s, %s, %s, %s)"
        self.db.cursor.execute(sql, (atendimento.id_servico, atendimento.id_tecnico, atendimento.id_cliente, atendimento.status))
        self.db.conexao.commit()
        return self.db.cursor.lastrowid

    def listar(self):
        sql = """
        SELECT a.id, a.id_servico, s.titulo as servico_titulo, 
               a.id_tecnico, ut.nome as tecnico_nome,
               a.id_cliente, uc.nome as cliente_nome,
               a.data_solicitacao, a.status
        FROM atendimentos a
        JOIN servicos s ON a.id_servico = s.id
        JOIN usuarios ut ON a.id_tecnico = ut.id
        JOIN usuarios uc ON a.id_cliente = uc.id
        ORDER BY a.data_solicitacao DESC
        """
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()

    def listar_por_tecnico(self, id_tecnico):
        sql = """
        SELECT a.id, a.id_servico, s.titulo as servico_titulo, 
               a.id_tecnico, ut.nome as tecnico_nome,
               a.id_cliente, uc.nome as cliente_nome,
               a.data_solicitacao, a.status
        FROM atendimentos a
        JOIN servicos s ON a.id_servico = s.id
        JOIN usuarios ut ON a.id_tecnico = ut.id
        JOIN usuarios uc ON a.id_cliente = uc.id
        WHERE a.id_tecnico = %s
        ORDER BY a.data_solicitacao DESC
        """
        self.db.cursor.execute(sql, (id_tecnico,))
        return self.db.cursor.fetchall()

    def listar_por_cliente(self, id_cliente):
        sql = """
        SELECT a.id, a.id_servico, s.titulo as servico_titulo, 
               a.id_tecnico, ut.nome as tecnico_nome,
               a.id_cliente, uc.nome as cliente_nome,
               a.data_solicitacao, a.status
        FROM atendimentos a
        JOIN servicos s ON a.id_servico = s.id
        JOIN usuarios ut ON a.id_tecnico = ut.id
        JOIN usuarios uc ON a.id_cliente = uc.id
        WHERE a.id_cliente = %s
        ORDER BY a.data_solicitacao DESC
        """
        self.db.cursor.execute(sql, (id_cliente,))
        return self.db.cursor.fetchall()

    def atualizar_status(self, id, novo_status):
        sql = "UPDATE atendimentos SET status = %s WHERE id = %s"
        self.db.cursor.execute(sql, (novo_status, id))
        self.db.conexao.commit()

    def deletar(self, id):
        sql = "DELETE FROM atendimentos WHERE id = %s"
        self.db.cursor.execute(sql, (id,))
        self.db.conexao.commit()

class AvaliacaoDAO:
    def __init__(self):
        self.db = Database()

    def criar(self, avaliacao):
        sql = "INSERT INTO avaliacoes (id_servico, id_cliente, nota, comentario) VALUES (%s, %s, %s, %s)"
        self.db.cursor.execute(sql, (avaliacao.id_servico, avaliacao.id_cliente, avaliacao.nota, avaliacao.comentario))
        self.db.conexao.commit()
        return self.db.cursor.lastrowid

    def listar_por_servico(self, id_servico):
        sql = """
        SELECT a.id, a.id_servico, s.titulo as servico_titulo,
               a.id_cliente, u.nome as cliente_nome,
               a.nota, a.comentario, a.data_avaliacao
        FROM avaliacoes a
        JOIN servicos s ON a.id_servico = s.id
        JOIN usuarios u ON a.id_cliente = u.id
        WHERE a.id_servico = %s
        ORDER BY a.data_avaliacao DESC
        """
        self.db.cursor.execute(sql, (id_servico,))
        return self.db.cursor.fetchall()

    def media_por_servico(self, id_servico):
        sql = "SELECT AVG(nota) as media FROM avaliacoes WHERE id_servico = %s"
        self.db.cursor.execute(sql, (id_servico,))
        resultado = self.db.cursor.fetchone()
        return round(resultado[0], 2) if resultado[0] else 0

class ContatoDAO:
    def __init__(self):
        self.db = Database()

    def criar(self, contato):
        sql = "INSERT INTO contatos (id_usuario, telefone, cidade, estado) VALUES (%s, %s, %s, %s)"
        self.db.cursor.execute(sql, (contato.id_usuario, contato.telefone, contato.cidade, contato.estado))
        self.db.conexao.commit()
        return self.db.cursor.lastrowid

    def buscar_por_usuario(self, id_usuario):
        sql = "SELECT * FROM contatos WHERE id_usuario = %s"
        self.db.cursor.execute(sql, (id_usuario,))
        return self.db.cursor.fetchone()

    def atualizar(self, contato):
        sql = "UPDATE contatos SET telefone = %s, cidade = %s, estado = %s WHERE id_usuario = %s"
        self.db.cursor.execute(sql, (contato.telefone, contato.cidade, contato.estado, contato.id_usuario))
        self.db.conexao.commit()

class EspecializacaoDAO:
    def __init__(self):
        self.db = Database()

    def criar(self, especializacao):
        sql = "INSERT INTO especializacoes (nome) VALUES (%s)"
        self.db.cursor.execute(sql, (especializacao.nome,))
        self.db.conexao.commit()
        return self.db.cursor.lastrowid

    def listar(self):
        sql = "SELECT * FROM especializacoes ORDER BY nome"
        self.db.cursor.execute(sql)
        return self.db.cursor.fetchall()

    def deletar(self, id):
        sql = "DELETE FROM especializacoes WHERE id = %s"
        self.db.cursor.execute(sql, (id,))
        self.db.conexao.commit()

class PortfolioDAO:
    def __init__(self):
        self.db = Database()

    def criar(self, portfolio):
        sql = "INSERT INTO portfolio (id_tecnico, titulo, descricao, url_link) VALUES (%s, %s, %s, %s)"
        self.db.cursor.execute(sql, (portfolio.id_tecnico, portfolio.titulo, portfolio.descricao, portfolio.url_link))
        self.db.conexao.commit()
        return self.db.cursor.lastrowid

    def listar_por_tecnico(self, id_tecnico):
        sql = """
        SELECT p.id, p.id_tecnico, u.nome as tecnico_nome,
               p.titulo, p.descricao, p.url_link, p.data_envio
        FROM portfolio p
        JOIN usuarios u ON p.id_tecnico = u.id
        WHERE p.id_tecnico = %s
        ORDER BY p.data_envio DESC
        """
        self.db.cursor.execute(sql, (id_tecnico,))
        return self.db.cursor.fetchall()

    def deletar(self, id):
        sql = "DELETE FROM portfolio WHERE id = %s"
        self.db.cursor.execute(sql, (id,))
        self.db.conexao.commit()