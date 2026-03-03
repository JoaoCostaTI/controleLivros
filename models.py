
class Livro:
    def __init__(self, titulo, autor, genero, status, nota):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.status = status
        self.nota = nota

    def __repr__(self):
        return f'''
Titulo:   {self.titulo}
Autor(a): {self.autor}
Genero:   {self.genero}
Status:   {self.status}
Nota:     {self.nota}
'''
