from manager import Gerenciador
from models import Livro
from utils import *

gerente = Gerenciador()

data_inicio = '31/12/2025'
data_convertida_banco = converter_data_para_banco(data_inicio)

l = Livro('Harry Potter', 'J.K.K. Rowling', 700, 'Fantasia', 'Lendo', data_convertida_banco, '-')

gerente.criar_tabela()

gerente.cadastrar_livro(l)