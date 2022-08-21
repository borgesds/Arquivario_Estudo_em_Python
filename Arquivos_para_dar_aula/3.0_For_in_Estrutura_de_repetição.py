"""
For in em Python
Iterando strings com for
Função range(start=0, stop, stp=1)
"""
for n in range(20, 10, -1):
    print(n)

for n in range(0, 30, 3):
    print(n)

for n in range(100):
    if n % 8 == 0:
        print(n)

# buscar letras
texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()

    elif letra == 'h':
        nova_string += letra.upper()

    else:
        nova_string += letra

print(nova_string)

# buscar letras
# continue -> pula para o proximo laço
# break -> termina o laço
texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()

    elif letra == 'h':
        nova_string += letra.upper()
        break

    else:
        nova_string += letra

print(nova_string)
