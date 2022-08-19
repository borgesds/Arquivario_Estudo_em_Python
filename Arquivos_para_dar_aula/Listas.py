"""
Listas en Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

#         0    1    2    3    4   5
lista = ['A', 'b', 'c', 'd', 'e', 32]
#      -  6    5    4    3    2    1

print(lista[5])
print(lista)

lista = ['A', 'b', 'c', 'd', 'e', 32]
lista[5] = 'Qualquer outra coisa'

print(lista)
print(lista[0:3])
print(lista[1:4])
print(lista[:3])
print(lista[2:])
print(lista[0])
print(lista[-1])
# começo:fim:saltar
print(lista[::2])
# inverter lista
print(lista[::-1])

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

l8 = [0, 'String', True, -33.5]

for elem in l8:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')

# Advinha a palavra
secreto = 'cavalo'
digitadas = []
chances = 4

while True:
    # chances
    if chances <= 0:
        print('Você perdeu!!!')
        break

    # games
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhhh isso não vale, digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhhuull, a letra "{letra}" esta na palavra secreta.')
    else:
        print(f'AFFzzz: a letra "{letra}" Não existe na palavra secreta.')
        digitadas.pop()

    # mostra letras acertadas
    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'VOCÊ GANHOU!!! A palavra secreta era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim, tente mais uma vez: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances')
    print()
