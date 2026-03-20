import sqlite3
from database import Database
from models import Livro

class Gerenciador:
    def __init__(self):
        self.db = Database('skoob.db')

    def cadastrar_livro(self, livro_obj):
        titulo = livro_obj.titulo
        autor = livro_obj.autor
        total_paginas = livro_obj.paginas
        genero = livro_obj.genero
        status = livro_obj.status
        data_inicio = livro_obj.data_inicio
        data_termino = livro_obj.data_termino

        sql = 'INSERT INTO livros VALUES(?,?,?,?,?,?,?)'

        try:
            if self.db.executar_sql(sql, (titulo, autor, total_paginas, genero, status, data_inicio, data_termino)):
                return True
        except Exception as e:
            print(e)
            return False
        
    def atualizar_livro(self, livro_obj):
        titulo = livro_obj.titulo
        autor = livro_obj.autor
        total_paginas = livro_obj.paginas
        genero = livro_obj.genero
        status = livro_obj.status
        data_inicio = livro_obj.data_inicio
        data_termino = livro_obj.data_termino

        sql = 'UPDATE livros SET autor = ?, paginas = ?, genero = ?, status = ?, data_inicio = ?, data_termino = ?  WHERE titulo = ?'

        try:
            self.db.executar_sql(sql, (autor, total_paginas, genero, status, data_inicio, data_termino, titulo))
            return True
        except Exception as e:
            print(e)

    def listar_livros(self):
        '''
            Função para listar TODOS os livros
        '''
        try:
            sql = 'SELECT * FROM livros'
            livros = self.db.listar_tudo(sql)
            return livros
        except Exception as e:
            print(e)
            return False
    def criar_tabela_livros(self):
        self.db.criar_tabela()


    def listar_livro_status(self, status):
        '''
            Função para listar um status especifico.
            Utilizar a variável status
        '''
        sql = 'SELECT * FROM livros WHERE status = ?'
        livros = self.db.listar_livro_por_status(sql, (status,))
        return livros
    

    def pesquisar_livro_gerente(self, livro):
        try:
            sql = 'SELECT * FROM livros WHERE titulo = ?'
            livro_banco = self.db.pesquisa_livro_banco(sql, (livro,))
            return livro_banco
        except Exception as e:
            print(e)

    def excluir_livro(self, livro):
        try:
            sql = 'DELETE FROM livros WHERE  titulo = ?'
            self.db.executar_sql(sql, (livro,))
            return
        except Exception as e:
            print(e)



