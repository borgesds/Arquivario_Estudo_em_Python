"""
While em python
Utilizado para realizar ações enquanto
uma condição for verdadeira
"""
# loop infinito
while True:
    nome = input("Qual o seu nome? ")
    print(f'Ola {nome}')

x = 0
while x <= 25:
    print(x)
    x += 1

print('Acabou!!')


# continue
x = 0
while x <= 25:
    # retira o 10 da sequencia
    if x == 10:
        x += 1
        continue
    # não vai rodar o resto do código
    print(x)
    x += 1

print('Acabou!!')


# break
x = 0
while x <= 25:
    # vai parar quando achar
    if x == 10:
        x += 1
        break
    # não vai rodar o resto do código
    print(x)
    x += 1

print('Acabou!!')


# while dentro de while
#coluna
x = 0
while x <= 25:
    # linha
    y = 0
    while y <= 5:
        print(f'Colunda e Linhas ({x}, {y})')
        y += 1

    x += 1

print('Acabou!!')


# mini calculadora
while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador\n[+, -, * ou /]: ')


    if not num_1.isnumeric() or num_2.isnumeric():
        print('Você precisa digitar um numero.')

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - * /
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operador invalido')

    # sair
    sair = input('Deseja sair? [s]im ou [n]ão: ')
    if sair == 's':
        break

"""
While / else
contadores
acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else')

# com break (não passa por else)
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador >= 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else')

print('Isso será executado.')


"""
         Índices
         0123456789......................33
"""
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)

contador = 0

while contador < tamanho_frase:
    print(frase[contador], contador)
    contador += 1

# jogar dentro de uma variável vazia
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)

contador = 0
nova_string = ''

while contador < tamanho_frase:
    nova_string += frase[contador]
    contador += 1
    print(nova_string)


# mudar o tamanho so de uma letra
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)

contador = 0
nova_string = ''

while contador < tamanho_frase:
    letra = frase[contador]

    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra

    contador += 1

print(nova_string)

# OU trocar por input

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)

contador = 0
nova_string = ''

input_do_usuario = input('Qual letra deseja colocar maiúscula? ')

# Iteração <== Iterar (percorrer)
while contador < tamanho_frase:
    letra = frase[contador]

    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra

    contador += 1

print(nova_string)
