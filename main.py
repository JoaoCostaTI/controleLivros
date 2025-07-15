import json

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
def listarLivros():
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
        print('-' * 80)
def listarLivrosLendo():
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
        print('~' * 80)
def listarLivrosQueroLer():
    #Titulo das colunas
        print(f'{"Nº":<5}{"Nome":<30}{"Autor(a)":<20}{"Situação":<15}{"Ano":<5}{"Nº Páginas":<5}')
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
        print('~' * 80)
def listarLivrosLido():
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
        print('~' * 80)   
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
        if livro['situacao'] == 'Lendo' or livro['situacao'] == 'Lido':
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
def menu():
    tam = 40
    print('-' * tam)
    print(f'{"Sistema de Controle de Leitura".center(tam)}')
    print('-' * tam)
    print('1 - Cadastrar Livro\n2 - Listar Livro\n3 - Excluir Livro\n4 - Estatisticas\n5 - Editar Livro\n6 - Sair do Programa')
    print('-' * tam)
##############################################################################

while True:
    menu()
    op = int(input('Sua opção: '))

    if op == 1:
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
        preencherJson()

    elif op == 2:
        if len(livros) == 0:
            formatacao('Nenhum livro cadastrado! Cadastre ao menos 1 livro! ')   
        else:
            while True:
                tam = 40
                print('-' * tam)
                print('1 - Todos os Livros\n2 - Lendo\n3 - Quero Ler\n4 - Lido\n5 - Menu anterior')
                subOpcao = int(input('Sua opção: '))
                if subOpcao == 5:
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
                else:
                    print('Opção inválida! Selecione apenas dentre as disponiveis! ')
                print('-' * tam)
    elif op == 3:
            #EXCLUSÃO DE LIVROS
            listarLivros()
            while True:
                print('Qual livro deseja excluir? (Digite o número)')
                op = int(input('Livro: '))
                if op > len(livros):
                    print('Não existe esse livro! Tente novamente')
                else:
                    print(f'*' * 65)
                    print(f'Livro [{livros[op-1]['nome']}] excluído com sucesso!')
                    del livros[op - 1] 
                    print(f'*' * 65)
                    preencherJson()
                    break
    elif op == 4:
        #Estatisticas
        tam = 40
        print('~' * tam)
        print(f'{"Estatisticas de Leitura".center(tam)}')
        print('~' * tam)
        print(f'2023 = {livrosPorAno(2023)}x')
        print(f'2024 = {livrosPorAno(2024)}x')
        print(f'2025 = {livrosPorAno(2025)}x')
        print(f'Paginômetro = {paginometro()}')
        print(f'Média de Páginas = {mediaPaginas()}')
        print('~' * tam)
    elif op == 5:
        print('Ainda em produção...')
    elif op == 6:
        print('Saindo do Programa...')
        break
    else:
        formatacao('Opção inválida! Selecione uma opção do menu! ')
        

