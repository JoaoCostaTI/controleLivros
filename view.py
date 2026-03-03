import tkinter as tk
from tkinter import ttk

# --- CONFIGURAÇÕES INICIAIS ---
janela = tk.Tk()
janela.geometry("800x600")
janela.title("Controle de Leitura 📚")

# Listas para os Comboboxes
lista_categorias = ["Ficção", "Não-Ficção", "Romance", "Técnico", "Fantasia", "Outros"]
lista_status = ["Quero Ler", "Lendo", "Lido", "Relendo", "Abandonado"]

# =============================================================================
# ÁREA DE FORMULÁRIO (INPUTS)
# =============================================================================
frame_form = ttk.Frame(janela, padding=10, borderwidth=2, relief='groove')
frame_form.pack(fill='x', padx=10, pady=10)

# Título da Seção
lbl_titulo_secao = ttk.Label(frame_form, text="Cadastrar Novo Livro", font=('Arial', 12, 'bold'))
lbl_titulo_secao.pack(pady=(0, 10))

# --- LINHA 1: Título do Livro ---
lb_titulo = ttk.Label(frame_form, text="Título do Livro:")
lb_titulo.pack(anchor='w')

ent_titulo = ttk.Entry(frame_form)
ent_titulo.pack(fill='x', expand=True, pady=(0, 5))

# --- LINHA 2: Autor ---
lb_autor = ttk.Label(frame_form, text="Autor:")
lb_autor.pack(anchor='w')

ent_autor = ttk.Entry(frame_form)
ent_autor.pack(fill='x', expand=True, pady=(0, 5))

# --- LINHA 3: Categoria, Status e Nota (Lado a Lado) ---
frame_linha3 = ttk.Frame(frame_form)
frame_linha3.pack(fill='x', pady=5)

# Bloco Categoria (Esquerda)
frame_cat = ttk.Frame(frame_linha3)
frame_cat.pack(side='left', fill='x', expand=True, padx=(0, 5))
lbl_cat = ttk.Label(frame_cat, text="Gênero:")
lbl_cat.pack(anchor='w')
combo_cat = ttk.Combobox(frame_cat, values=lista_categorias, state='readonly')
combo_cat.pack(fill='x')

# Bloco Status (Meio)
frame_status = ttk.Frame(frame_linha3)
frame_status.pack(side='left', fill='x', expand=True, padx=5)
lbl_status = ttk.Label(frame_status, text="Status:")
lbl_status.pack(anchor='w')
combo_status = ttk.Combobox(frame_status, values=lista_status, state='readonly')
combo_status.pack(fill='x')

# Bloco Nota (Direita)
frame_nota = ttk.Frame(frame_linha3)
frame_nota.pack(side='left', fill='x', expand=True, padx=(5, 0))
lbl_nota = ttk.Label(frame_nota, text="Nota (0-10):")
lbl_nota.pack(anchor='w')
spin_nota = ttk.Spinbox(frame_nota, from_=0, to=10, width=5)
spin_nota.pack(fill='x')

# =============================================================================
# ÁREA DE BOTÕES
# =============================================================================
frame_botoes = ttk.Frame(janela, padding=5)
frame_botoes.pack(fill='x', padx=10)

# Funções placeholder (Para você conectar depois)
def btn_salvar_click(): 
    valores = (3,'Harry Potter', 'JK Rowling', 'Fantasia', 'Lido', 10)
    return valores
def btn_excluir_click(): print("Aqui você coloca a função DELETE do Banco")
def btn_limpar_click(): print("Aqui você limpa os campos")

btn_salvar = ttk.Button(frame_botoes, text="SALVAR LIVRO", command=btn_salvar_click)
btn_salvar.pack(side='right', padx=5)

btn_excluir = ttk.Button(frame_botoes, text="Excluir Selecionado", command=btn_excluir_click)
btn_excluir.pack(side='left', padx=5)

btn_limpar = ttk.Button(frame_botoes, text="Limpar Campos", command=btn_limpar_click)
btn_limpar.pack(side='right', padx=5)

# =============================================================================
# ÁREA DE LISTAGEM (TREEVIEW)
# =============================================================================
frame_lista = ttk.Frame(janela, padding=10)
frame_lista.pack(fill='both', expand=True, padx=10, pady=5)

lbl_lista = ttk.Label(frame_lista, text="Meus Livros Lidos:", font=('Arial', 10, 'bold'))
lbl_lista.pack(anchor='w', pady=(0, 5))

# Definição das Colunas
colunas = ('id', 'titulo', 'autor', 'genero', 'status', 'nota')
tabela = ttk.Treeview(frame_lista, columns=colunas, show='headings')

# Barra de Rolagem (Scrollbar)
scroll_y = ttk.Scrollbar(frame_lista, orient='vertical', command=tabela.yview)
tabela.configure(yscroll=scroll_y.set)

scroll_y.pack(side='right', fill='y')
tabela.pack(side='left', fill='both', expand=True)

# Cabeçalhos da Tabela
tabela.heading('id', text='ID')
tabela.heading('titulo', text='Título')
tabela.heading('autor', text='Autor')
tabela.heading('genero', text='Gênero')
tabela.heading('status', text='Status')
tabela.heading('nota', text='Nota')

# Tamanho das Colunas (O ID geralmente a gente esconde ou deixa pequeno)
tabela.column('id', width=30, minwidth=30)
tabela.column('titulo', width=200)
tabela.column('autor', width=150)
tabela.column('genero', width=100)
tabela.column('status', width=100)
tabela.column('nota', width=50, anchor='center')

# --- Exemplo de como inserir dados na tabela (Visualização apenas) ---
valores = btn_salvar_click()
tabela.insert('', 'end', values=valores)
tabela.insert('', 'end', values=(2, "Código Limpo", "Robert Martin", "Técnico", "Lendo", "-"))

janela.mainloop()