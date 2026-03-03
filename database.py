import sqlite3
from models import Livro

class BancoDeDados:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco
    
    def criar_tabela(self):
        with sqlite3.connect(self.nome_banco) as conexao:
            cursor = conexao.cursor()
            sql = 'CREATE TABLE IF NOT EXISTS livros (id integer primary key autoincrement, titulo text, autor text, genero text, status text, nota int)'
            cursor.execute(sql)
            conexao.commit()

    def inserir_livro(self, livro):
        dados_livro = (
            livro.titulo,
            livro.autor,
            livro.genero,
            livro.status,
            livro.nota
        )
        with sqlite3.connect(self.nome_banco) as conexao:
            cursor = conexao.cursor()
            sql = "INSERT INTO livros (titulo, autor, genero, status, nota) values (?,?,?,?,?)"
            cursor.execute(sql, dados_livro)
            conexao.commit()
    
    def listar_todos_livros(self):
        with sqlite3.connect(self.nome_banco) as conexao:
            cursor = conexao.cursor()
            sql = 'SELECT * FROM livros'
            cursor.execute(sql)
            todos_livros = cursor.fetchall()
            
            return todos_livros
        
