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
                data_inicio text 
                )
                '''
            cursor.execute(sql)
            conexao.commit()

    def executar_sql(self, sql):
        try:
            with sqlite3.connect(self.nome_banco) as connection:
                cur = connection.cursor()
                cur.execute(sql)
                connection.commit()
        except Exception as e:
            print(e)

        
