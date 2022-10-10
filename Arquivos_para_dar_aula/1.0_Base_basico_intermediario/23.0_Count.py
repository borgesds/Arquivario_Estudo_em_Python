"""
Count -Itertools
"""

from itertools import count

contador = count()

lista = ['Lucas', 'Maria', 'Carlos']
lista = zip(contador, lista)
print(list(lista))

# contador sem fim
# for valor in contador:
#     print(valor)


contador2 = count(start=5,  # começa a partir de um  numero
                  step=0.5)   # conta em intervalos
for valor in contador2:
    print(round(valor, 2))

    if valor >= 10:
        break


contador3 = count(start=9,  # começa a partir de um  numero
                  step=-1)   # conta em intervalos
for valor in contador3:
    print(round(valor, 2))

    if valor >= 10 or valor <= -10:
        break
