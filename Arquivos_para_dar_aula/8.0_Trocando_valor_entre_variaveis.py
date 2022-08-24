"""
Trocando valores entre variáveis
"""
# o jeito mais comuns entre linguagens de programação:
from re import X


x = 10
# =>Luiz

y = 'Luiz'
# =>10

z = x
x = y
y = z

print(f'x={x} e y={y}')

# no python
x = 10
# =>Luiz

y = 'Luiz'
# =>10

x, y = y, x

print(f'x={x} e y={y}')

x = 10
y = 'Luiz'
s = 'Igor'

x, y, s = y, s, x

print(f'x={x} e y={y} e s={s}')