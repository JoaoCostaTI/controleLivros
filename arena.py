livros = [
    {
        "nome": "Bom dia Espirito Santo",
        "autor": "Benny Hinn",
        "situacao": "Lido",
        "ano": 2023,
        "paginas": 237
    },
    {
        "nome": "O Monge e o executivo",
        "autor": "James C. Hunter",
        "situacao": "Lido",
        "ano": 2023,
        "paginas": 144
    },
    {
        "nome": "Inteligência Socioemocional",
        "autor": "Augusto Cury",
        "situacao": "Lido",
        "ano": 2023,
        "paginas": 143
    },
    {
        "nome": "Manual de Persuasão do FBI",
        "autor": "Jack Schafer",
        "situacao": "Lido",
        "ano": 2023,
        "paginas": 256
    }
]


while True:
    pesquisa = input('Qual livro editar? ')
    encontrado = True
    parada = False

    for k, livro in enumerate(livros):
        
        if pesquisa in livro['nome']:

            encontrado = False

            print(f'Livro encontrado! {livro["nome"]}')
            while True:
                print('Qual campo alterar? ')
                op = int(input('1 - Situação (Quero Ler, Lendo, Lido)\n2 - Ano da leitura >>> '))
                if op > 2:
                    print('Opção inválida! Escolha apenas a opções acima! ')
                elif op == 1:
                    while True:
                        situacao = int(input('1 - Quero Ler\n2 - Lendo\n3 - Lido >>> '))
                        if situacao > 3:
                            print('Opção inválida! Selecione apenas as opções acima!')
                        elif situacao == 1:
                            livros[k]['situacao'] = 'Quero Ler'
                            print('Alterado com sucesso!')
                            parada = True
                            
                        elif situacao == 2:
                            livros[k]['situacao'] = 'Lendo'
                            print('Alterado com sucesso!')
                            parada = True
                            
                        elif situacao == 3:
                            livros[k]['situacao'] = 'Lido'
                            print('Alterado com sucesso!')
                            parada = True
                        else:
                            break
                elif op == 2:
                    novoAno = int(input('Qual o novo ano? '))
                    livros[k]['ano'] =  novoAno
                    print('Alterado com sucesso!')
                    parada = True
                else:
                    break
    if parada:
        break
    if encontrado:
        print('Livro não encontrado! ')
    

           