"""
Desempacotamento de listas em Python
"""
lista1 = ['Luiz', 'Maria', 'Carlos']

lista2 = ['Luiz', 'Maria', 'Carlos', 1, 2, 3, 4, 5, 6, 7, 8, 9]

n1, n2, n3 = lista1
# ou (Gera outra lista como restante dos valores)
n1, n2, *outra_lista, ultimo_da_lista = lista2

print(n1, n2, n3)
print(n1, n2, outra_lista)
print(ultimo_da_lista)

lista3 = ['Luiz', 'Maria', 'Carlos', 1, 782, 3, 4, 65, 642, 73, 83, 9, 34]

# separa de uma lista os tres ultimos 
*outra_lista, n1, n2, n3 = lista3

print(outra_lista)
print(n1, n2, n3)
