class Servico:
    def __init__(self, id=None, titulo=None, descricao=None, data=None, status=None, orcamento=None, cliente_id=None, tecnico_id=None):
        self.id = id  
        self.titulo = titulo  
        self.descricao = descricao  
        self.data = data  
        self.status = status  
        self.orcamento = orcamento  
        self.cliente_id = cliente_id  
        self.tecnico_id = tecnico_id  

    def __repr__(self):
        return (f"Servico(id={self.id}, titulo='{self.titulo}', descricao='{self.descricao}', data='{self.data}', "
                f"status='{self.status}', orcamento={self.orcamento}, cliente_id={self.cliente_id}, tecnico_id={self.tecnico_id})")