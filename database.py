import sqlite3

class Database:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    def criar_tabela_livros(self):
        with sqlite3.connect(self.nome_banco) as connection:
            cursor = connection.cursor()
            cursor.execute(
                """
                    CREATE TABLE IF NOT EXISTS livros(
                        titulo TEXT PRIMARY KEY,
                        autor TEXT,
                        total_paginas INTEGER,
                        genero TEXT,
                        status TEXT,
                        data_inicio TEXT,
                        data_termino TEXT
                    )
                """
            )
            connection.commit()

    def executar_sql(self, sql, parametros = ()):
        with sqlite3.connect(self.nome_banco) as connection:
            try:
                cursor = connection.cursor()
                cursor.execute(sql, parametros)
                connection.commit()
            except Exception as e:
                connection.rollback()
                raise e
