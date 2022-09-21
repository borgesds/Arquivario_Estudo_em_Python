from itertools import groupby, tee

alunos = [
    {'nome': 'Carlos', 'nota': 'A'},
    {'nome': 'Thais', 'nota': 'C'},
    {'nome': 'Felipe', 'nota': 'C'},
    {'nome': 'André', 'nota': 'B'},
    {'nome': 'Camila', 'nota': 'D'},
    {'nome': 'Valter', 'nota': 'A'},
    {'nome': 'Maria', 'nota': 'C'},
    {'nome': 'Andrey', 'nota': 'C'},
    {'nome': 'Igor', 'nota': 'B'},
    {'nome': 'Deborah', 'nota': 'A'},
    {'nome': 'Thatiane', 'nota': 'C'},
    {'nome': 'Gilson', 'nota': 'C'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')


    qtd = len(list(va2))
    print(f'\t{qtd} alunos tiraram a nota {agrupamento}')
    print()
