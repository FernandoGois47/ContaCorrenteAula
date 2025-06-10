class Usuario:
    def __init__(self, id=None, nome="", email="", senha="", tipo="cliente", data_cadastro=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo
        self.data_cadastro = data_cadastro

class Servico:
    def __init__(self, id=None, id_tecnico=None, titulo="", descricao="", preco=0.0, categoria="", data_publicacao=None):
        self.id = id
        self.id_tecnico = id_tecnico
        self.titulo = titulo
        self.descricao = descricao
        self.preco = preco
        self.categoria = categoria
        self.data_publicacao = data_publicacao

class Atendimento:
    def __init__(self, id=None, id_servico=None, id_tecnico=None, id_cliente=None, data_solicitacao=None, status="pendente"):
        self.id = id
        self.id_servico = id_servico
        self.id_tecnico = id_tecnico
        self.id_cliente = id_cliente
        self.data_solicitacao = data_solicitacao
        self.status = status

class Avaliacao:
    def __init__(self, id=None, id_servico=None, id_cliente=None, nota=5, comentario="", data_avaliacao=None):
        self.id = id
        self.id_servico = id_servico
        self.id_cliente = id_cliente
        self.nota = nota
        self.comentario = comentario
        self.data_avaliacao = data_avaliacao

class Contato:
    def __init__(self, id=None, id_usuario=None, telefone="", cidade="", estado=""):
        self.id = id
        self.id_usuario = id_usuario
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado

class Especializacao:
    def __init__(self, id=None, nome=""):
        self.id = id
        self.nome = nome

class Portfolio:
    def __init__(self, id=None, id_tecnico=None, titulo="", descricao="", url_link="", data_envio=None):
        self.id = id
        self.id_tecnico = id_tecnico
        self.titulo = titulo
        self.descricao = descricao
        self.url_link = url_link
        self.data_envio = data_envio