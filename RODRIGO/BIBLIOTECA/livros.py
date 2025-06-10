class Livros:
    def __init__(self, titulo, autor, genero, isbn):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.isbn = isbn
        self.status = "disponivel"  # Adicione este atributo