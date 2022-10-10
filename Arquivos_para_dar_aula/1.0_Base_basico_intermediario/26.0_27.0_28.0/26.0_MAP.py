from dados import produtos, pessoas, lista

# modos de percorrer uma lista
nova_lista = map(lambda x: x * 2, lista)
nova_lista = [x * 2 for x in lista]

print(lista)
print(list(nova_lista))


# modo de percorre um dicionario


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)

for p in novos_produtos:
    print(p)


def aumentar_idade(i):
    i['nova_idade'] = round(i['idade'] * 1.20)
    return i


nomes = map(lambda x: x['nome'], pessoas)

for pessoa in nomes:
    print(pessoa)

nomes = map(aumentar_idade, pessoas)

for pessoa in nomes:
    print(pessoa)
