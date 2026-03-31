from view import *
import tkinter as tk

if __name__ == '__main__':
    raiz = tk.Tk()
    raiz.title('Skoob')
    raiz.geometry('1200x600')
    gerente_principal = Gerenciador()
    app = Janela(raiz, gerente = gerente_principal)
    app.pack(fill='both', expand=True)
    raiz.mainloop()

   