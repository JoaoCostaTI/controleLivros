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
        
livraria_costa = BancoDeDados('olamundo.db')
livraria_costa.criar_tabela()
# Lista com os dados dos 10 livros
dados_para_teste = [
    ('O Senhor dos Anéis', 'J.R.R. Tolkien', 'Fantasia', 'Lido', 10),
    ('1984', 'George Orwell', 'Ficção', 'Lido', 9),
    ('Dom Casmurro', 'Machado de Assis', 'Clássico', 'Relendo', 10),
    ('Código Limpo', 'Robert C. Martin', 'Técnico', 'Lendo', 8),
    ('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 'Infantil', 'Lido', 10),
    ('Duna', 'Frank Herbert', 'Ficção Científica', 'Quero Ler', 0),
    ('Sapiens', 'Yuval Noah Harari', 'Não-Ficção', 'Abandonado', 5),
    ('Entendendo Algoritmos', 'Aditya Bhargava', 'Técnico', 'Quero Ler', 0),
    ('A Revolução dos Bichos', 'George Orwell', 'Sátira', 'Lido', 8),
    ('O Hobbit', 'J.R.R. Tolkien', 'Fantasia', 'Lido', 9)
]

# Loop para criar os objetos e inserir no banco
print("Iniciando inserção em massa...")

for i in dados_para_teste:
    # Desempacota a tupla direto nos argumentos da classe Livro
    # i[0] = Título, i[1] = Autor, etc.
    novo_livro = Livro(i[0], i[1], i[2], i[3], i[4])
    livraria_costa.inserir_livro(novo_livro)

print("Todos os 10 livros foram inseridos!")
livros = livraria_costa.listar_todos_livros()
print(livros)
