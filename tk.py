import tkinter as tk
from tkinter import messagebox


# Função para abrir nova janela
def abrir_janela_opcao(opcao):
    nova_janela = tk.Toplevel(janela)  # Cria nova janela filha
    nova_janela.title(f"Opção: {opcao}")
    nova_janela.geometry("300x200")  # Tamanho da janela
    
    tk.Label(nova_janela, text=f"{opcao}").pack(pady=20)
    
    # Exemplo de botão na nova janela
    tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy).pack(pady=10)

# Janela principal
janela = tk.Tk()
janela.title("SKOOB")
janela.geometry("300x250")

# Lista de opções
opcoes = ["Cadastrar Livro", "Listar Livro", "Estatisticas", "Editar Livro", "Sair do Programa"]

tk.Label(janela, text="Sistema de Controle de Livros").pack(pady=10)

for opcao in opcoes:
    tk.Button(janela, text=opcao, width=25,
              command=lambda o=opcao: abrir_janela_opcao(o)).pack(pady=5)

janela.mainloop()
