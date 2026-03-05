from view import *
import tkinter as tk

if __name__ == '__main__':
    raiz = tk.Tk()
    raiz.title('Skoob')
    raiz.geometry('500x400')
    app = Janela(raiz)
    app.pack(fill='both', expand=True)
    
    raiz.mainloop()