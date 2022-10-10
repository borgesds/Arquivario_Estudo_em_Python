"""
Considerando duas listas de inteiros ou float (lista A e lista B)
Some as valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o
tamanho da menor.

Ex:
lista_a = [1,2,3,4,5,6,7,8]
lista_b = [1,2,3,4]

==> resultado
lista_soma = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7, 8]
lista_b = [1, 2, 3, 4]

# modo 1
lista_soma = []

for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])

print(lista_soma)


# modo 2
lista_soma2 = []

for i, _ in enumerate(lista_b):
    lista_soma2.append(lista_a[i] + lista_b[i])

print(lista_soma2)


# modo 2
# modomais pythonico de resolver esse problema
lista_soma3 = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma3)
