"""
Listas en Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

# #         0    1    2    3    4   5
# lista = ['A', 'b', 'c', 'd', 'e', 32]
# #      -  6    5    4    3    2    1

# print(lista[5])
# print(lista)

# lista = ['A', 'b', 'c', 'd', 'e', 32]
# lista[5] = 'Qualquer outra coisa'

# print(lista)
# print(lista[0:3])
# print(lista[1:4])
# print(lista[:3])
# print(lista[2:])
# print(lista[0])
# print(lista[-1])
# # começo:fim:saltar
# print(lista[::2])
# # inverter lista
# print(lista[::-1])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = []
l4 = l1 + l2

# # extend
# l1.extend(l2)

# append
l3.append(l1)
l3.append(l2)

# insert
l2.insert(0, 'banana')

# pop (remove o ultimo elemento)
l2.pop()

l5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# del (escolher o intervalo para remover)
del(l5[3:5])
del(l2[0])

# max
print(max(l5))

# min
print(min(l5))

# criar uma lista automatica
l6 = list(range(0, 10))
l7 = list(range(0, 100, 10))

print(l6)
print(l7)