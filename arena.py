from datetime import date
from utils import *

hoje = date.today()

hoje_formatado_usuario = converter_data_para_usuario(str(hoje))
hoje_formatado_banco = converter_data_para_banco(str(hoje))

print(hoje_formatado_usuario)
print(hoje_formatado_banco)

