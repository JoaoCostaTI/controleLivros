import tkinter as tk
from tkinter import ttk
from utils import *
from models import Livro

class AdicionarLivro(ttk.Frame):
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        ttk.Label(self, text='Titulo').grid(row=0, column=0, pady=5, padx=5, sticky='e')
        self.ent_titulo = ttk.Entry(self, width=28)
        self.ent_titulo.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        ttk.Label(self, text='Autor').grid(row=1, column=0, pady=5, padx=5, sticky='e')
        self.ent_autor = ttk.Entry(self, width=28)
        self.ent_autor.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        ttk.Label(self, text='Páginas').grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.ent_paginas = ttk.Entry(self, width=13)
        self.ent_paginas.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        ttk.Label(self, text='Gênero').grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.combo_genero = ttk.Combobox(self, values=COMBO_GENERO, width=25)
        self.combo_genero.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        ttk.Label(self, text='Status').grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.combo_status = ttk.Combobox(self, values=COMBO_STATUS, width=10)
        self.combo_status.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        #BTN's
        self.btn_salvar = ttk.Button(self, text= 'Salvar', width=18, command=self.salvar_livro).grid(row=5, column=1, pady=5, padx=5)
        
    def salvar_livro(self):
        titulo = self.ent_titulo.get()
        autor = self.ent_autor.get()
        paginas = self.ent_paginas.get()
        genero = self.combo_genero.get()
        status = self.combo_status.get()

        livro = Livro(titulo, autor, paginas, genero, status)

        print(livro)

class MinhaEstante(ttk.Frame):
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        

#Funções para montagem das interfaces
def montar_add_livro(frame_pai):
    ttk.Label(frame_pai, text='Adicionar a Biblioteca', font= CABECALHOS).pack(padx=10, pady=10, anchor='center')
    add_livro = AdicionarLivro(frame_pai)
    add_livro.pack()

def montar_minha_estante(frame_pai):
    ttk.Label(frame_pai, text='Minha Estante', font=CABECALHOS).pack()
    minha_estante = MinhaEstante(frame_pai)
    minha_estante.pack()

def montar_estatisticas(frame_pai):
    ttk.Label(frame_pai, text='Estatisticas', font=CABECALHOS).pack()


raiz = tk.Tk()
raiz.geometry('700x500')

#notebook (Container com as Abas)
notebook = ttk.Notebook(raiz)
notebook.pack(fill='both', expand=True, padx=5, pady=5)

#Frames com as páginas
frame_add_livro = ttk.Frame(notebook)
frame_minha_estante = ttk.Frame(notebook)
frame_estatisticas = ttk.Frame(notebook)

#Adicionando a Frame na interface
notebook.add(frame_add_livro, text='Novo Livro')
notebook.add(frame_minha_estante, text='Minha Estante')
notebook.add(frame_estatisticas, text='Estatísticas')

#Funções para preencher as Frames
montar_add_livro(frame_add_livro)
montar_minha_estante(frame_minha_estante)
mon

raiz.mainloop()