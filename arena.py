texto = "Alguma coisa escrita aqui para encher linguiça atoa e ver se entendi o que quero"

def limitarTexto (texto, limite):
    if len(texto) > limite:
        return texto[:limite -3] + "..."
    return texto


print(limitarTexto(texto, 28))