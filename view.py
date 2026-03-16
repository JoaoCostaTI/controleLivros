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

        self.frame_buscar = ttk.Frame(self)
        self.frame_buscar.pack()

        ttk.Label(self.frame_buscar, text='Status').grid(row=0, column=0, padx=5, pady=5)
        self.combo_status = ttk.Combobox(self.frame_buscar, values=COMBO_STATUS, width=10)
        self.combo_status.grid(row=0, column=1, padx=5, pady=5)
        btn_listar = ttk.Button(self.frame_buscar, text='Listar', command= self.listar_por_status)
        btn_listar.grid(row=0, column=2, padx=5, pady=5)

        #Tabela
        self.tabela = ttk.Treeview(self, columns=COLUNAS_LIVRO, show='headings')
        self.tabela.heading('titulo', text='Titulo')
        self.tabela.heading('autor', text='Autor')
        self.tabela.heading('paginas', text='Páginas')
        self.tabela.heading('genero', text='Gênero')
        self.tabela.heading('status', text='Status')
        self.tabela.heading('data_inicio', text='Data Inicio')
        self.tabela.heading('data_termino', text='Data Término')
        self.tabela.pack(fill='both', expand=True)

        self.tabela.column('titulo', anchor='center', width=150, stretch=False)
        self.tabela.column('autor', anchor='center', width=150, stretch=False)
        self.tabela.column('paginas', anchor='center', width=150, stretch=False)
        self.tabela.column('genero', anchor='center', width=150, stretch=False)
        self.tabela.column('status', anchor='center', width=150, stretch=False)
        self.tabela.column('data_inicio', anchor='center', width=150, stretch=False)
        self.tabela.column('data_termino', anchor='center', width=150, stretch=False)

        try: 
            self.livros = gerente.listar_livros()
            if self.livros: 
                for r in self.livros:
                    titulo, autor, paginas, categoria, situacao, data_inicio, data_termino = r
                    data_inicio_usuario = converter_data_para_usuario(data_inicio)
                    data_termino_usuario = converter_data_para_usuario(data_termino)
                    self.tabela.insert('', 'end', values=(titulo, autor, paginas, categoria, situacao, data_inicio_usuario, data_termino_usuario))
        except Exception as e:
            print(e)
            messagebox.showinfo('=(', 'Nenhum livro cadastrado!')

    def listar_por_status(self):
        status = self.combo_status.get()
        self.livros = gerente.listar_livro_status(status) 

        #Limpar tabela atual
        self.tabela.delete(*self.tabela.get_children())

        for r in self.livros:
            titulo, autor, paginas, categoria, situacao, data_inicio, data_termino = r
            data_inicio_usuario = converter_data_para_usuario(data_inicio)
            data_termino_usuario = converter_data_para_usuario(data_termino)
            self.tabela.insert('', 'end', values=(titulo, autor, paginas, categoria, situacao, data_inicio_usuario, data_termino_usuario))

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

class EditarLivro(ttk.Frame):
    def __init__(self, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.frame_pesquisar_livro = ttk.Frame(self, borderwidth=5, relief='solid')
        self.frame_pesquisar_livro.pack(pady=5, padx=5)
        
        ttk.Label(self.frame_pesquisar_livro, text='Pesquisar: ').grid(row=0, column=0, padx=5, pady=5)
        self.ent_nome_livro = ttk.Entry(self.frame_pesquisar_livro)
        self.ent_nome_livro.grid(row=0, column=1, padx=5, pady=5) 
        self.btn_pesquisar = ttk.Button(self.frame_pesquisar_livro, text='Pesquisar', command=lambda: self.pesquisar_livro())
        self.btn_pesquisar.grid(row=1, column=1, padx=5, pady=5)

        self.frame_editar_livro = ttk.Frame(self, borderwidth=5, relief='solid')
        self.frame_editar_livro.pack(pady=5, padx=5)

        ttk.Label(self.frame_editar_livro, text='Titulo').grid(row=0, column=0, pady=5, padx=5, sticky='e')
        self.ent_titulo = ttk.Entry(self.frame_editar_livro, width=28)
        self.ent_titulo.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        ttk.Label(self.frame_editar_livro, text='Autor').grid(row=1, column=0, pady=5, padx=5, sticky='e')
        self.ent_autor = ttk.Entry(self.frame_editar_livro, width=28)
        self.ent_autor.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        ttk.Label(self.frame_editar_livro, text='Páginas').grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.ent_paginas = ttk.Entry(self.frame_editar_livro, width=13)
        self.ent_paginas.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        ttk.Label(self.frame_editar_livro, text='Gênero').grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.combo_genero = ttk.Combobox(self.frame_editar_livro, values=COMBO_GENERO, width=25)
        self.combo_genero.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        ttk.Label(self.frame_editar_livro, text='Status').grid(row=4, column=0, padx=5, pady=5, sticky='e')
        self.combo_status = ttk.Combobox(self.frame_editar_livro, values=COMBO_STATUS, width=10)
        self.combo_status.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        #BTN's
        self.btn_salvar = ttk.Button(self.frame_editar_livro, text= 'Salvar', width=18, command=self.salvar_livro).grid(row=7, column=1, pady=5, padx=5)

    def pesquisar_livro(self):
        livro = self.ent_nome_livro.get()
        livro = gerente.pesquisar_livro_gerente(livro)
        
        if livro:
            ttk.Label(self.frame_editar_livro, text='Data Inicio').grid(row=5, column=0, padx=5, pady=5, sticky='e')
            self.ent_data_inicio = ttk.Entry(self.frame_editar_livro)
            self.ent_data_inicio.grid(row=5, column=1, padx=5, pady=5, sticky='w')

            ttk.Label(self.frame_editar_livro, text='Data Término').grid(row=6, column=0, padx=5, pady=5, sticky='e')
            self.ent_data_termino = ttk.Entry(self.frame_editar_livro)
            self.ent_data_termino.grid(row=6, column=1, padx=5, pady=5, sticky='w')


            titulo, autor, paginas, genero, status, data_inicio, data_termino = livro[0]

            data_inicio_usuario = converter_data_para_usuario(data_inicio)

            self.ent_titulo.insert(0, titulo)
            self.ent_autor.insert(0, autor)
            self.ent_paginas.insert(0, paginas)
            self.combo_genero.insert(0, genero)
            self.combo_status.insert(0, status) 
            self.ent_data_inicio.insert(0, data_inicio_usuario)
            self.ent_data_termino.insert(0, data_termino)


        else:
            messagebox.showinfo('=(', 'Livro não encontrado.')
        
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

#Funções para montagem das interfaces
def montar_add_livro(frame_pai):
    ttk.Label(frame_pai, text='Adicionar a Biblioteca', font= CABECALHOS).pack(padx=10, pady=10, anchor='center')
    add_livro = AdicionarLivro(frame_pai)
    add_livro.pack()

def montar_minha_estante(frame_pai):
    ttk.Label(frame_pai, text='Minha Estante', font=CABECALHOS).pack()
    #Listagem dos Livros
    minha_estante = MinhaEstante(frame_pai)
    minha_estante.pack()
   
def montar_estatisticas(frame_pai):
    ttk.Label(frame_pai, text='Estatisticas', font=CABECALHOS).pack()
    estatisticas = Estatisticas(frame_pai)
    estatisticas.pack(fill='both', expand=True, padx=10, pady=10)

def montar_editar_livro(frame_pai):
    ttk.Label(frame_pai, text='Editar Livro', font=CABECALHOS).pack(padx=10, pady=10, anchor='center')

    editar_livro = EditarLivro(frame_pai)
    editar_livro.pack()

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
        frame_editar_livro = ttk.Frame(notebook)

        #Adicionando a Frame na interface
        notebook.add(frame_add_livro, text='Novo Livro')
        notebook.add(frame_minha_estante, text='Minha Estante')
        notebook.add(frame_estatisticas, text='Estatísticas')
        notebook.add(frame_editar_livro, text='Editar Livro')

        #Funções para preencher as Frames
        montar_add_livro(frame_add_livro)
        montar_minha_estante(frame_minha_estante)
        montar_estatisticas(frame_estatisticas)
        montar_editar_livro(frame_editar_livro)


