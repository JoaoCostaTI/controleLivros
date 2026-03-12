import sqlite3
from models import Livro



class Database:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
    
    def criar_tabela(self):
        with sqlite3.connect(self.nome_banco) as conexao:
            cursor = conexao.cursor()
            sql = '''CREATE TABLE IF NOT EXISTS livros (
                titulo primary key, 
                autor text,
                paginas integer, 
                genero text, 
                status text,
                data_inicio text,
                data_termino text 
                )
                '''
            cursor.execute(sql)
            conexao.commit()

    def executar_sql(self, sql, value = ()):
        try:
            with sqlite3.connect(self.nome_banco) as connection:
                cur = connection.cursor()
                cur.execute(sql, value)
                connection.commit()
                return True
        except Exception as e:
            print(e)
            return False
    
    def listar_tudo(self, sql):
        try:
            with sqlite3.connect(self.nome_banco)  as connection:
                cur = connection.cursor()
                cur.execute(sql)
                livros = cur.fetchall()
                return livros
        except Exception as e:
            return e
        
    def listar_livro_por_status(self, sql, status):
        try:
            with sqlite3.connect(self.nome_banco) as connection:
                cur = connection.cursor()
                cur.execute(sql, status)
                livro_status = cur.fetchall()
                return livro_status
        except Exception as e:
            return e