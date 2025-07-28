livros = [{
        "nome": "bom dia espirito santo",
        "autor": "Benny Hinn",
        "situacao": "Lido",
        "ano": 2023,
        "paginas": 237
    },
    {
        "nome": "o monge e o executivo",
        "autor": "James C. Hunter",
        "situacao": "Lido",
        "ano": 2023,
        "paginas": 144
    },
    {
        "nome": "inteligencia socioemocional",
        "autor": "Augusto Cury",
        "situacao": "Lido",
        "ano": 2023,
        "paginas": 143
    }]

for l in livros:
    l['ql'] = 1
for depois in livros:
    print(depois)