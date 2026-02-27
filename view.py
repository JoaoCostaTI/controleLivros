from manager import Gerenciador
from models import Livro
from utils import *
import tkinter as tk
from tkinter import ttk

class Janela(tk.Frame):
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Gerente que realiza operações no banco
        self.gerente = Gerenciador()

        # Notebooks
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True, padx=5, pady=5)

        # Frames
        self.frame_novo_livro = ttk.Frame(self.notebook)
        self.frame_minha_estante = ttk.Frame(self.notebook)
        self.frame_estatisticas = ttk.Frame(self.notebook)

        # Preparando as abas (NavBar)
        self.notebook.add(self.frame_novo_livro, text='Novo Livro')
        self.notebook.add(self.frame_minha_estante, text='Minha Estante')
        self.notebook.add(self.frame_estatisticas, text='Estatisticas')

        # Adicionando as abas (NavBar)
        self.novo_livro(self.frame_novo_livro)
        self.minha_estante(self.frame_minha_estante)
        self.estatisticas(self.frame_estatisticas)

    def novo_livro(self, frame_pai):
        tk.Label(frame_pai, text='Cadastro de Livros', font=CABECALHOS, background="#615E5E", foreground='#FFFFFF').pack(padx=3, pady=3)
        l = AdicionarLivros(frame_pai)
        l.pack(pady=5, padx=5)
        

    def minha_estante (self, frame_pai):
        ttk.Label(frame_pai, text='Minha Estante', font=CABECALHOS).pack(padx=3, pady=3)
    
    def estatisticas(self, frame_pai):
        ttk.Label(frame_pai, text='Estatisticas', font=CABECALHOS).pack(padx=3, pady=3)

class AdicionarLivros(tk.Frame):
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(background="#F8F9FA")
        # BTNs e Entrys
        tk.Label(self, text='Titulo', fg='#2D3436').grid(column=0, row=0, pady=5, padx=5, sticky='e',)
        self.etd_titulo = ttk.Entry(self, width=30)
        self.etd_titulo.grid(row=0, column=1, pady=5, padx=5, sticky='w')
        tk.Label(self, text='Autor', fg='#2D3436').grid(row=1, column=0, pady=5, padx=5, sticky='e',)
        self.etd_autor = ttk.Entry(self, width=30)
        self.etd_autor.grid(row=1, column=1, pady=5, padx=5, sticky='w')
        tk.Label(self, text='Páginas', fg='#2D3436').grid(row=2, column=0, padx=5, pady=5, sticky='e',)
        self.etd_paginas = ttk.Entry(self, width=10)
        self.etd_paginas.grid(row=2, column=1, pady=5, padx=5, sticky='w')
        tk.Label(self, text='Gênero', fg='#2D3436').grid(row=3, column=0, padx=5, pady=5, sticky='e',)
        self.combo_genero = ttk.Combobox(self, values=COMBO_GENERO, width=25)
        self.combo_genero.grid(row=3, column=1, pady=5, padx=5, sticky='w')
        tk.Label(self, text='Status').grid(row=4, column=0, padx=5, pady=5, sticky='e',)
        self.combo_status = ttk.Combobox(self, values=COMBO_STATUS, width=7)
        self.combo_status.grid(row=4, column=1, pady=5, padx=5, sticky='w')
        
    