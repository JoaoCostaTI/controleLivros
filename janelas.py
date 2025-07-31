import tkinter as tk
from tkinter import messagebox, simpledialog

# Lista para armazenar os alimentos
alimentos = []

# Função para atualizar a lista na interface
def atualizar_lista():
    lista.delete(0, tk.END)
    for alimento in alimentos:
        lista.insert(tk.END, f"{alimento['nome']} - {alimento['calorias']} kcal")

# Função para adicionar novo alimento
def adicionar():
    nome = entrada_nome.get().strip()
    calorias = entrada_calorias.get().strip()
    
    if nome == "" or calorias == "":
        messagebox.showwarning("Erro", "Preencha todos os campos.")
        return

    try:
        calorias = int(calorias)
    except ValueError:
        messagebox.showwarning("Erro", "Calorias devem ser um número.")
        return

    alimentos.append({"nome": nome, "calorias": calorias})
    entrada_nome.delete(0, tk.END)
    entrada_calorias.delete(0, tk.END)
    atualizar_lista()

# Função para editar alimento
def editar():
    selecao = lista.curselection()
    if not selecao:
        messagebox.showinfo("Aviso", "Selecione um alimento para editar.")
        return

    index = selecao[0]
    alimento = alimentos[index]

    novo_nome = simpledialog.askstring("Editar Nome", "Novo nome:", initialvalue=alimento["nome"])
    if novo_nome is None:
        return
    novo_calorias = simpledialog.askstring("Editar Calorias", "Novas calorias:", initialvalue=alimento["calorias"])
    if novo_calorias is None:
        return

    try:
        novo_calorias = int(novo_calorias)
    except ValueError:
        messagebox.showwarning("Erro", "Calorias inválidas.")
        return

    alimentos[index] = {"nome": novo_nome, "calorias": novo_calorias}
    atualizar_lista()

# Função para excluir alimento
def excluir():
    selecao = lista.curselection()
    if not selecao:
        messagebox.showinfo("Aviso", "Selecione um alimento para excluir.")
        return

    index = selecao[0]
    confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir?")
    if confirmacao:
        alimentos.pop(index)
        atualizar_lista()

# Criando a janela principal
janela = tk.Tk()
janela.title("Sistema de cadastro de Livros")

# Entradas
tk.Label(janela, text="Nome do alimento:").grid(row=0, column=0)
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1)

tk.Label(janela, text="Calorias:").grid(row=1, column=0)
entrada_calorias = tk.Entry(janela)
entrada_calorias.grid(row=1, column=1)

# Botões
tk.Button(janela, text="Adicionar", command=adicionar).grid(row=2, column=0, pady=5)
tk.Button(janela, text="Editar", command=editar).grid(row=2, column=1, pady=5)
tk.Button(janela, text="Excluir", command=excluir).grid(row=2, column=2, pady=5)

# Lista
lista = tk.Listbox(janela, width=100)
lista.grid(row=3, column=0, columnspan=3, pady=10)

# Rodar a aplicação
janela.mainloop()
