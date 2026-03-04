import sqlite3
from database import Database

class Gerenciador:
    def __init__(self):
        self.db = Database('skoob.db')

    def cadastrar_livro(self, livro_obj):
        titulo = livro_obj.titulo
        autor = livro_obj.autor
        total_paginas = livro_obj.total_paginas
        genero = livro_obj.genero
        status = livro_obj.status
        data_inicio = livro_obj.data_inicio
        data_termino = livro_obj.data_termino

        sql = 'INSERT INTO livros VALUES(?,?,?,?,?,?,?)'

        try:
            self.db.executar_sql(sql, (titulo, autor, total_paginas, genero, status, data_inicio, data_termino))
            return True
        except Exception as e:
            print(e)
            return False
        
    def criar_tabela_livros(self):
        self.db.criar_tabela()

