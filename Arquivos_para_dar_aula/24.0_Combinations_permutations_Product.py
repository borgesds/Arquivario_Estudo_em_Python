"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Maria', 'Carlos', 'Rose', 'Igor']

# a ordem não importa
for grupo in combinations(pessoas, 2):  # 2 é a quantidade que deve te no grupo
    print(grupo)

print()

# a ordem importa
for grupo in permutations(pessoas, 2):
    print(grupo)

print()

# ter todas as combinações posssiveis
for grupo in product(pessoas, repeat=2):
    print(grupo)
