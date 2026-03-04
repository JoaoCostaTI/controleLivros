
class Livro:
    def __init__(self, titulo, autor,paginas, genero, status):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero
        self.status = status
        
    def __repr__(self):
        return f'''
Titulo:   {self.titulo}
Autor(a): {self.autor}
Páginas:  {self.paginas}
Genero:   {self.genero}
Status:   {self.status}
'''
