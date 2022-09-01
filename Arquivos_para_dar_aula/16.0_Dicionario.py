"""
Dicionário
"""

# chave: valor
d1 = {'chave1': 'valor da chave'}

d1['nova_chave'] = 'valor da nova chave'

print(d1['chave1'])

# outro modo
d2 = dict(chave='valor da chave', chave1='valor da chave')
d2['nova_chave'] = 'valor da nova chave'

print(d2['chave1'])

# suportável
dx = {                   # <====
    'str': 'valor',
    123: 'outro valor',
    (1, 2, 3, 4): 'tupla'
}


dx['naoexiste'] = 'agora existe'

if 'naoexiste' in dx:
    print(dx['naoexiste'])

else:
    print('Não existe essa chave')


# posso usar esse modo, e é mais recomendado
dx['naoexisteoutro'] = 'agora existe'

if dx.get('naoexisteoutro') is not None:
    print(dx.get('naoexisteoutro'))
else:
    print('Não existe essa chave')

print(dx)


# update
dx['str'] = 'André Borges'

if dx.get('str') is not None:
    print(dx.get('str'))
else:
    print('Não existe essa chave')


# ou
dz = {                    # <====
    'chave1': 'valor',
    'chave2': 'outro valor',
    'chave3': 'tupla'
}


# retornar so chaves
for k in dz:
    print(k)

# retornar valores
for v in dz.values():
    print(v)

# retornar chave valor
for cv in dz.items():
    print(cv)
    print(cv[0], cv[1])

    # ou
for cv1, cv2 in dz.items():
    print(cv1, cv2)


