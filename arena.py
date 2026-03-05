from datetime import date
from utils import *

hoje_obj = date.today()

hoje_banco = str(hoje_obj)

hoje_usuario = converter_data_para_usuario(hoje_banco)
print(hoje_usuario)