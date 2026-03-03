from datetime import datetime

def converter_data_para_banco(data_texto):
    """
    Recebe: '31/12/2025' ou '1/1/2025'
    Retorna: '2025-12-31' ou None (se der erro)
    """
    if not data_texto: 
        return None 
    try:
        # 1. Converte TEXTO BRASIL -> OBJETO DATA
        # O python é inteligente: ele entende "1" e "01" como a mesma coisa aqui
        data_obj = datetime.strptime(data_texto, "%d/%m/%Y")
        
        # 2. Converte OBJETO DATA -> TEXTO BANCO (ISO)
        return data_obj.strftime("%Y-%m-%d")
        
    except ValueError:
        # Se cair aqui, o usuário digitou data inválida (ex: 30/02 ou texto)
        return None
    
def converter_data_para_usuario(data):
    """
    Recebe: '2026-1-1' padrão para banco de dados
    Retorna: '1/1/2026' ou None (se der erro)
    """
    if not data:
        return None
    try:
        data_obj = datetime.strptime(data, '%Y-%m-%d')
        return data_obj.strftime('%d/%m/%Y')
    except ValueError:
        return None
    
CABECALHOS = ('HELVICA', 14, 'bold')

COMBO_GENERO = ["Biografia / Memórias",
    "Clássicos",
    "Desenvolvimento Pessoal",
    "Fantasia",
    "Ficção Científica",
    "Ficção Histórica",
    "Filosofia / Sociologia",
    "História",
    "Mistério / Suspense",
    "Religião / Espiritualidade",
    "Romance",
    "Tecnologia / Computação",
    "Terror / Horror"]

COMBO_STATUS = ['Lendo', 'Lido', 'Quero Ler']