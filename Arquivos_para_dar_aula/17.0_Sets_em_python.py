"""
Sets
add, update, clear, discard
union
"""

s1 = set()

# add
s1.add(1)
s1.add(2)
s1.add((1, 2, 3, 'Carlos'))

# discard
s1.discard(1)

# update
# update desmembra o valor, e não respeita a ordem
s1.update('python')
s1.update([1434])
s1.update([1, 2, 3, 4, 5, 6], {5, 6})
# o Sets não aceita duplicados, so aceita elementos  únicos

print(s1)

# tirar as duplicadas de uma lista
l1 = [1, 2, 1, 1, 1, 3, 2, 1, 2, 2, 'Maria', 'Camila']
l1 = set(l1)
lista = list(l1)

print(l1)

# union ou |
s2 = {0, 1, 2, 3, 4, 5}
s3 = {1, 2, 4, 6, 7, 8, 9, 10, 11, 12, 13}
st = s2 | s3

print(st)

# diference
s4 = s2 - s3
s5 = s3 - s2

print(s4)
print(s5)

# symmetric difference
s6 = s2 ^ s3

print(s6)

# tirar duplicadas de uma lista
# verificar se são iguais
l1 = ['Carlos', 'Maria', 'Camila']
l2 = ['Carlos', 'Maria', 'Camila',
      'Maria', 'Camila', 'Maria', 'Camila',
      'Camila', 'Camila', 'Camila', 'Camila']

if set(l1) == set(l2):
    print('L1 é igual L2')
else:
    print('L1 é diferente L2')
