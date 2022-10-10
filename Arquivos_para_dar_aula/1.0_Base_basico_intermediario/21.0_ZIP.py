"""
Zip -  Unindo iteraveis
Zip_lonfest - Itertools
"""
from itertools import zip_longest, count


# deve esta em ordem as variaveis
indice = count()

cidade = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'outra']

estados = ['SP', 'MG', 'BA']

cidades_estados = zip(cidade, estados)

# print(dict(cidades_estados))

for valor in cidades_estados:
    print(valor)

# usando indice
cidades_estados2 = zip(
    indice,
    cidade,
    estados,
)

for indice, estado, cidade in cidades_estados2:
    print(indice, estado, cidade)


# zip_longest
# por padrão ele adiciona None quando não tem variaveis
cidade2 = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'outra']

estados2 = ['SP', 'MG', 'BA']

cidades_estados3 = zip_longest(cidade2, estados2, fillvalue='Estados')
print(list(cidades_estados3))
