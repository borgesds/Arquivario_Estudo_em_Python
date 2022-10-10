from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
print(list(nova_lista))

lista_nova = [x for x in lista if x > 5]
print(list(lista_nova))

# produtos
nova_lista = filter(lambda p: p['preco'] > 35, produtos)

for produto in nova_lista:
    print(produto)


# ou


def filtrar(produto):
    if produto['preco'] >= 55:
        produto['e_caro'] = True
        return True
    else:
        return False


nova_lista = filter(filtrar, produtos)

for produto in nova_lista:
    print(produto)


# pessoas
def filtra(pessoa):
    if pessoa['idade'] < 18:
        return True
    else:
        return False


nova_lista = filter(filtra, pessoas)

for pessoa in nova_lista:
    print(pessoa)
