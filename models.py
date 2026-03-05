
class Livro:
    def __init__(self, titulo, autor,paginas, genero, status, data_inicio, data_termino):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero
        self.status = status
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        
    def __repr__(self):
        return f'''
Titulo:   {self.titulo}
Autor(a): {self.autor}
Páginas:  {self.paginas}
Genero:   {self.genero}
Status:   {self.status}
'''
