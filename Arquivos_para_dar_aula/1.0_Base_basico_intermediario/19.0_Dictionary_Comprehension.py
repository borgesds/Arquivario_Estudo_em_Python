"""
Dictionary Comprehension
"""

lista = [
    ('chave', 2),
    ('chave2', 'valor2'),
    ('chave3', 'valor3'),
]
d1 = {x: y for x, y in lista}
d2 = {x: y * 3 for x, y in lista}
d3 = {x.upper(): y for x, y in lista}

print(d1)
print(d2)
print(d3)

# set
d4 = {x for x in range(5)}
print(d4)

# dict
d5 = {f'chave_{x}': x ** 2 for x in range(5)}
print(d5)
