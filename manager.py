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

    def paginometro_gerente(self):
        try:
            sql = "SELECT sum(paginas) FROM livros WHERE status = 'Lido'"
            pag = self.db.paginometro_banco(sql)
            return pag
        except Exception as e:
            print(e)

    def listar_qtd_livros_status(self, status):
        try:
            sql = "SELECT COUNT(*) FROM livros WHERE status = ?"
            lido = self.db.listar_qtd_livros_status_banco(sql, (status,))
            return lido
        except Exception as e:
            print(e)

    def top_genero_gerente(self):
        try: 
            sql = '''
                SELECT genero, COUNT(genero) AS quantidade
                FROM livros
                GROUP BY genero
                ORDER BY quantidade DESC
                LIMIT 5
            '''
            genero = self.db.top_genero_banco(sql)
            return genero
        except Exception as e:
            print(e)

    def livros_ano_gerente(self):
        try: 
            sql = '''
                SELECT strftime('%Y', data_termino) AS ano, COUNT(titulo) AS quantidade
                FROM livros
                WHERE status = 'Lido' and data_termino != '-'
                GROUP BY ano
                ORDER BY quantidade DESC
                LIMIT 3
            '''
            livros_ano = self.db.livros_ano_banco(sql)
            return livros_ano
        except Exception as e:
            raise e

