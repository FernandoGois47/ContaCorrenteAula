class Avaliacao:
    def __init__(self, id=None, nota: int = 0, comentario: str = "", cliente_id=None, tecnico_id=None):
        self.id = id  
        self.nota = nota  
        self.comentario = comentario 
        self.cliente_id = cliente_id 
        self.tecnico_id = tecnico_id 

    def __repr__(self):
        return (f"Avaliacao(id={self.id}, nota={self.nota}, comentario='{self.comentario}', "
                f"cliente_id={self.cliente_id}, tecnico_id={self.tecnico_id})")