import sqlite3

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
        
    def pesquisa_livro_banco(self, sql, livro):
        with sqlite3.connect(self.nome_banco) as connection:
            cur = connection.cursor()
            cur.execute(sql, livro)
            livro = cur.fetchall()
            return livro
        
    def paginometro_banco(self, sql):
        with sqlite3.connect(self.nome_banco) as connection:
            cur = connection.cursor()
            cur.execute(sql)
            pag = cur.fetchone()
            paginas_lidas = pag[0]
            if paginas_lidas is None:
                paginas_lidas = 0
            return paginas_lidas
        
    def listar_qtd_livros_status_banco(self,sql, value = ()):
        try:
            with sqlite3.connect(self.nome_banco) as connection:
                cur = connection.cursor()
                cur.execute(sql, value)
                lido = cur.fetchone()
                livros_lido = lido[0]
                if livros_lido is None:
                    livros_lido = 0
                return livros_lido
        except Exception as e:
            print(e)

    def top_genero_banco(self, sql):
        try: 
            with sqlite3.connect(self.nome_banco) as connection:
                cur = connection.cursor()
                cur.execute(sql)
                genero = cur.fetchall()
                return genero
        except Exception as e:
            print(e)

    def livros_ano_banco(self, sql):
        try: 
            with sqlite3.connect(self.nome_banco) as connection:
                cur = connection.cursor()
                cur.execute(sql)
                livros = cur.fetchall()
                return livros
        except Exception as e:
            print(e)
    

