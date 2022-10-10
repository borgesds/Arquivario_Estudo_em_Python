"""
For / Else em Python
"""
# basic
variavel = ['Luiz Carlos', 'James White', 'Maria Green']

for valor in variavel:
    if valor.startswith('J'):
        print('Começa com J', valor)
    else:
        print('Não começa com J', valor)


# usando variavel e lower
variavel = ['Luiz Carlos', 'James White', 'Maria Green']

comeca_com_j = False

for valor in variavel:
    if valor.lower().startswith('j'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe uma palavra que começa com J')
else:
    print('Não exise uma palavra que começa com J')


# continue
variavel = ['Luiz Carlos', 'James White', 'Maria Green']

for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    # vai printar todas as resposta que não tiver J
    # o print pode substituir o valor else
    print(valor)
