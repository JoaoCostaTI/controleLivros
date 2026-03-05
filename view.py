import tkinter as tk
from tkinter import ttk, messagebox
from utils import *
from models import Livro
from manager import Gerenciador
from datetime import date


gerente = Gerenciador()

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

        #Capturando Data
        hoje_obj = date.today()
        hoje_banco = str(hoje_obj)

        livro = Livro(titulo, autor, paginas, genero, status, hoje_banco, '-')

        if gerente.cadastrar_livro(livro):
            messagebox.showinfo('Sucesso!', 'Livro cadastrado com Sucesso!')
        else:
            messagebox.showerror('=(', 'Algo deu errado, livro não cadastrado')    

class MinhaEstante(ttk.Frame):
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

class Estatisticas(ttk.Frame):
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.config(borderwidth=5, relief='solid')
        self.frame_central = ttk.Frame(self)
        self.frame_central.place(relx=0.5, rely=0.5, anchor='center')
        self.card_estatisticas()
        self.card_livros_lidos()
        self.card_top_genero()


    def card_estatisticas(self):
        card = ttk.Frame(self.frame_central, borderwidth=5, relief='solid')
        card.grid(row=0, column=0, padx=5, pady=5)
        titulo = ttk.Label(card, text='Paginômetro', font=CARD_TITULO)
        titulo.pack()
        total_paginas =  ttk.Label(card, text='4500')
        total_paginas.pack()
    
    def card_livros_lidos(self):
        card = ttk.Frame(self.frame_central, borderwidth=5, relief='solid')
        card.grid(row=0, column=1, padx=5, pady=5)
        titulo = ttk.Label(card, text='Livros Lidos', font=CARD_TITULO)
        titulo.pack()
        qtd_livros = ttk.Label(card, text='12')
        qtd_livros.pack()

    def card_top_genero(self):
        card = ttk.Frame(self.frame_central, borderwidth=5, relief='solid')
        card.grid(row=0, column=2, padx=5, pady=5)
        titulo = ttk.Label(card, text='Top Gênero', font=CARD_TITULO)
        titulo.pack()
        genero = ttk.Label(card, text='Fantasia')
        genero.pack()

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
    estatisticas = Estatisticas(frame_pai)
    estatisticas.pack(fill='both', expand=True, padx=10, pady=10)

class Janela(ttk.Frame):
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master,*args, **kwargs)
        #notebook (Container com as Abas)
        notebook = ttk.Notebook(self)
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
        montar_estatisticas(frame_estatisticas)


