"""
Formatando valores codificadores.

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de pontos flutuantes (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(Quantidade)(Tipo - s, d ou f)

> - Esquerda
< - Direita
^- centro
"""
num_1 = 1
print(f'{num_1:0>10}')

num__1 = 1
print(f'{num__1:0<10}')

num_2 = 1143
print(f'{num_2:0>10}')

num__2 = 1143
print(f'{num__2:0^10}')

num___2 = 1143
print(f'{num___2:0>10.2f}')

# Nome
nome = 'André Borges'
nome_formatado = '{n:@<20}'.format(n=nome)
print(nome_formatado)

nome = 'André Fonseca'
sobrenome = 'Borges'
nome_formatado = '{0:&^20} {1:#^20}'.format(nome, sobrenome)
print(nome_formatado)
print(nome.islower())
print(nome.isupper())
print(sobrenome.upper())
print(sobrenome.lower())
print(nome.title())
