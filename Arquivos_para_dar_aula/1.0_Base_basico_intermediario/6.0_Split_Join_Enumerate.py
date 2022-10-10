"""
Split, Join, Enumerate em Python
Split - Dividir uma string # str
Join - Juntar uma lista # str
Enumerate - Enumerate elementos da lista # list
"""
string = "O rato roeu a roupa do rei de roma, o rato é esperto"
# criar uma lista da frase a cima e o separado e o espaço
list_1 = string.split(' ')
list_2 = string.split(',')

# quantas vezes uma palavra se repete na frase
for valor in list_1:
    print(f'A palavra {valor} apareceu {list_1.count(valor)}x na frase.')

palavra = ''
contagem = 0

for valor in list_1:
    qtd_vezes = list_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'Apalavra que apareceu mais vezes é {palavra} ({contagem}x)')

# tirar o espaço do começo e fim (strip())
# deixar a primeira letra maiúscula (captalize())
for valor in list_2:
    print(valor.strip().capitalize())

# Join
string = 'O brasil é penta, e teve o Ronaldinho Gaucho'
lista = string.split(' ')
string2 = '-'.join(lista)

print(string2)

# Enumerate
# Enumerate retorna tuplas
for indice, valor in enumerate(lista):
    print(indice, valor)

lista = [
    [0, 'Luiz'],
    [1, 'Carla'],
    [2, 'Maria'],
] 

# pegar os indices de uma lista
for v in lista:
    print(v[1])

lista2 = ['Luiz', 'Carla', 'Maria']

for indice, nome in enumerate(lista2):
    print(indice, nome)
