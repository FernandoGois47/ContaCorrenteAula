class Portifolio:
    def __init__(self, id=None, tecnico_id=None, link: str = ""):
        self.id = id 
        self.tecnico_id = tecnico_id  
        self.link = link  

    def __repr__(self):
        return f"Portifolio(id={self.id}, tecnico_id={self.tecnico_id}, link='{self.link}')"