nome = input('Qual o seu nome')

#  verdadeiro          Falso
print(nome or 'Você não digitou nada!!!')

# outro método 
a = 0
b = None
c = False
d = []
e = 22
f = 'Carlos'

variavel = a or b or c or d or e or f

print(variavel)

# para fazer essa verificação a cima você deveria fazer isso:

if a:
    variavel = a
elif b:
    variavel = b
elif c:
    variavel = c
elif d:
    variavel = d
elif e:
    variavel = e
else:
    variavel = f
