import json
from time import sleep

livros = []

# Carregar livros do arquivo JSON ou criar lista vazia
try:
    with open('livros.json', 'r', encoding='utf-8') as arquivo:
        livros = json.load(arquivo)
except FileNotFoundError:
    livros = []

###############################################################################
#reajustes formatacao
def formatacao(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'{msg}'.center(tam))
    print('~' * tam)

def limitarTextos(texto, limite):
    if len(texto) > limite:
        return texto[:limite - 3] + '...'
    return texto

###############################################################################
#Situação dos Livros
def cabecalhos(msg = ""):
    tam = 60
    print('-' * tam)
    print(f"{msg.center(tam)}")
    print('-' * tam)
def menu():
    print('1 - Cadastrar Livro\n2 - Listar Livro\n3 - Excluir Livro\n4 - Estatisticas\n5 - Editar Livro\n6 - Sair do Programa')
def listarLivros():
    totalLivros = 0
    sleep(0.1)
    #Titulo das colunas
    print(f'{"Nº":<5}{"Nome":<30}{"Autor(a)":<20}{"Situação":<15}{"Ano":<5}{"Nº Páginas":<5}')
    print('-' * 80)
        #Listar livros com formatação limitada
    for k, livro in enumerate(livros, start=1):
        nome = limitarTextos(livro['nome'], 30)
        autor = limitarTextos(livro['autor'], 20)
        situacao = limitarTextos(livro['situacao'], 15)
        anoLeitura = livro['ano']
        nPaginas = livro["paginas"]
        print(f'{k:<5}{nome:<30}{autor:<20}{situacao:<15}{anoLeitura:<5}{nPaginas:<5}')
        totalLivros += 1
    print(f'*** Total de Livros: {totalLivros} ***')
    print('-' * 80)
def listarLivrosLendo():
    sleep(0.1)
    totalLivros = 0
    #Titulo das colunas
    print(f'{"Nº":<5}{"Nome":<30}{"Autor(a)":<20}{"Situação":<15}{"Ano":<5}{"Nº Páginas":<5}')
    print('-' * 80)
    #Listar livros com formatação limitada
    for k, livro in enumerate(livros, start=1):
        if livro['situacao'] == 'Lendo':
            nome = limitarTextos(livro['nome'], 30)
            autor = limitarTextos(livro['autor'], 20)
            situacao = limitarTextos(livro['situacao'], 15)
            anoLeitura = livro['ano']
            nPaginas = livro["paginas"]

            print(f'{k:<5}{nome:<30}{autor:<20}{situacao:<15}{anoLeitura:<5}{nPaginas:<5}')
            totalLivros += 1
    print(f'*** Total de Livros: {totalLivros} ***')
    print('~' * 80)
def listarLivrosQueroLer():
    sleep(0.1)
    totalLivros = 0
    #Titulo das colunas
    print(f'{"Nº":<5}{"Nome":<30}{"Autor(a)":<20}{"Situação":<15}{"Ano":<5}{"NºPáginas":<5}')
    print('-' * 80)
            #Listar livros com formatação limitada
    for k, livro in enumerate(livros, start=1):
        if livro['situacao'] == 'Quero Ler':
            nome = limitarTextos(livro['nome'], 30)
            autor = limitarTextos(livro['autor'], 20)
            situacao = limitarTextos(livro['situacao'], 15)
            anoLeitura = livro['ano']
            nPaginas = livro["paginas"]

            print(f'{k:<5}{nome:<30}{autor:<20}{situacao:<15}{anoLeitura:<5}{nPaginas:<5}')
            totalLivros += 1
    print(f'*** Total de Livros: {totalLivros} ***')
    print('~' * 80)
def listarLivrosLido():
    sleep(0.1)
    totalLivros = 0
    #Titulo das colunas
    print(f'{"Nº":<5}{"Nome":<30}{"Autor(a)":<20}{"Situação":<15}{"Ano":<5}{"Nº Páginas":<5}')
    print('-' * 80)
    #Listar livros com formatação limitada
    for k, livro in enumerate(livros, start=1):
        if livro['situacao'] == 'Lido':
            nome = limitarTextos(livro['nome'], 30)
            autor = limitarTextos(livro['autor'], 20)
            situacao = limitarTextos(livro['situacao'], 15)
            anoLeitura = livro['ano']
            nPaginas = livro["paginas"]

            print(f'{k:<5}{nome:<30}{autor:<20}{situacao:<15}{anoLeitura:<5}{nPaginas:<5}')
            totalLivros += 1
    print(f'*** Total de Livros: {totalLivros} ***')
    print('~' * 80)   
def listarLivrosAbandonados():
    sleep(0.1)
    totalLivros = 0
    #Titulo das colunas
    print(f'{"Nº":<5}{"Nome":<30}{"Autor(a)":<20}{"Situação":<15}{"Ano":<5}{"Nº Páginas":<5}')
    print('-' * 80)
    #Listar livros com formatação limitada
    for k, livro in enumerate(livros, start=1):
        if livro['situacao'] == 'Abandonado':
            nome = limitarTextos(livro['nome'], 30)
            autor = limitarTextos(livro['autor'], 20)
            situacao = limitarTextos(livro['situacao'], 15)
            anoLeitura = livro['ano']
            nPaginas = livro["paginas"]

            print(f'{k:<5}{nome:<30}{autor:<20}{situacao:<15}{anoLeitura:<5}{nPaginas:<5}')
            totalLivros += 1
    print(f'*** Total de Livros: {totalLivros} ***')
    #Passagem da quantidade de livros abandonados 
def contarLivrosAbandonados(totalLivros = 0):
    #Listar livros com formatação limitada
    totalLivros = 0
    for livro in livros:
        if livro['situacao'] == 'Abandonado':
            totalLivros += 1
    return totalLivros
def livrosPorAno(anoReferencia):
    #Listar livros com formatação limitada
    qtdLivros = 0
    for k, livro in enumerate(livros, start=1):
        if livro['ano'] == anoReferencia and livro['situacao'] == 'Lido':
            qtdLivros += 1
    return qtdLivros
def preencherJson():
     with open('livros.json', 'w', encoding='utf-8') as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)
def paginometro():
    qtdPaginas = 0
    for livro in livros:
        if livro['situacao'] == 'Lido':
            qtdPaginas += livro['paginas']
    return qtdPaginas
def mediaPaginas():
    qtdPaginas = 0
    qtdLivros = 0
    for livro in livros:
        if livro['situacao'] == 'Lendo' or livro['situacao'] == 'Lido':
            qtdLivros += 1
            qtdPaginas += livro['paginas']
    return int(qtdPaginas / qtdLivros)
def editarLivro():
    tam = 40
    print('-' * tam)
    pesquisarLivro = str(input('Qual livro editar? '))
    naoEncontrado = True
    print('-' * tam)
    for k, v in enumerate(livros):
        #Pesquisando o livro na lista
        if pesquisarLivro in v['nome']:
            naoEncontrado = False
            tam = 40
            print(f'livro encontrado = {v["nome"]} | {v["situacao"]} | {v["ano"]} | {v["paginas"]}')
            print('-' * tam)
            op = int(input('1 - Editar situação\n2 - Editar Ano\n3 - Nº de páginas >>> '))
            #Alterar situação 
            if op == 1:
                v['situacao'] = str(input('Nova situação: [Quero Ler] [Lido] [Lendo][Abandonado]: '))
                print('-' * tam)
                print(f'Alterado com sucesso para {v["situacao"]}')
            #Alterar ano de leitura
            elif op == 2:
                print('-' * tam)
                v['ano'] = int(input('Novo ano: '))
                print(f'Alterado com sucesso para {v["ano"]}')
            elif op == 3:
                v['paginas'] = int(input('Nº de páginas: '))
                print(f'Alterado com sucesso para {v["paginas"]}')
            # Caso nenhuma opção der certo
            else:
                print('-' * tam)
                print('Opção inválida, nada foi alterado.')
                break
            
    if naoEncontrado:
        print('-' * tam)
        print('Livro não encontrado! ')
    
    print('-' * tam)

##############################################################################


while True:
    try:
        cabecalhos('Sistema de Controle de Leitura')
        menu()
        op = int(input('Sua opção: '))

        if op == 1:
            cabecalhos('Cadastro de livros')
            #cadastrar os livros:
            dados = {}
            dados['nome'] = input('Nome do livro: ')
            dados['autor'] = input('Nome Autor(a): ')
            while True:
                print('---Situação---\n1 - [Quero Ler]\n2 - [Lendo]\n3 - [Lido]')
                situacao = int(input('Sua opção: '))
                if situacao <= 0 or situacao > 3:
                    print('Erro! Selecione apenas as situações acima! ')
                elif situacao == 1:
                    dados['situacao'] = "Quero Ler"
                    break
                elif situacao == 2:
                    dados['situacao'] = "Lendo"
                    break
                elif situacao == 3:
                    dados['situacao'] = "Lido"
                    break

            dados['ano'] =  int(input('Ano de leitura: '))
            dados['paginas'] = int(input('Páginas: '))
            livros.append(dados)
            try:
                preencherJson()
                print('Livro cadastrado com sucesso. ')
            except ValueError:
                print('Algo deu errado, não foi possível cadastrar o livro.')
        elif op == 2:
            if len(livros) == 0:
                cabecalhos('ATENÇÃO!!')
                print('Nenhum livro cadastrado!\nCadastre ao menos 1 livro!')   
            else:
                while True:
                    try:
                        cabecalhos('Listagem de Livros')
                        print('1 - Todos os Livros\n2 - Lendo\n3 - Quero Ler\n4 - Lido\n5 - Abandonados\n6 - Menu anterior')
                        subOpcao = int(input('Sua opção: '))
                        if subOpcao == 6:
                            print('Voltando ao menu anterior...')
                            break
                        elif subOpcao == 1:
                            listarLivros()
                        elif subOpcao == 2:
                            listarLivrosLendo()
                        elif subOpcao == 3:
                            listarLivrosQueroLer()
                        elif subOpcao == 4:
                            listarLivrosLido()
                        elif subOpcao == 5:
                            listarLivrosAbandonados()
                        else:
                            print('Opção inválida! Selecione apenas dentre as disponiveis! ')
                    except ValueError:
                        print('⚠ Por favor, escolha uma opção válida (1 a 5). Somente números são aceitos.')
                        continue                
        elif op == 3:
                #EXCLUSÃO DE LIVROS
                cabecalhos('Excluir Livros')
                listarLivros()
                while True:
                    try:
                        print('Qual livro deseja excluir? (0 Volta para menu anterior)')
                        op = int(input('Livro: '))
                        if op == 0:
                            print('Voltando ao menu anterior...')
                            break
                        if op < 0 or op > len(livros):
                            print('Não existe esse livro! Tente novamente')
                        else:
                            print(f'*' * 65)
                            print(f'Livro [{livros[op-1]["nome"]}] excluído com sucesso!')
                            del livros[op - 1] 
                            print(f'*' * 65)
                            preencherJson()
                            break
                    except ValueError:
                        print('⚠ Por favor, escolha um livro válido da lista acima!. ')
        elif op == 4:
            #Estatisticas
            
            cabecalhos(f'Estatisticas de Leitura')
            sleep(0.3)
            
            sleep(0.1)
            print(f'2023 = {livrosPorAno(2023)}x')
            print(f'2024 = {livrosPorAno(2024)}x')
            print(f'2025 = {livrosPorAno(2025)}x')
            print(f'Abandonados = {contarLivrosAbandonados()}x')
            print(f'Paginômetro = {paginometro()}')
            print(f'Média de Páginas = {mediaPaginas()}')
            
            sleep(0.1)
        elif op == 5:
            editarLivro()
            preencherJson()
        elif op == 6:
            sleep(0.1)
            print('Saindo do Programa...')
            sleep(0.3)
            break
        else:
            formatacao('Opção inválida! Selecione uma opção do menu! ')   
    except ValueError:
        print('Erro! Selecione dentre as opções disponíveis! ')

