"""
Problema dos parâmetros mutáveis em funções.
=> Mutável: Listas, dicionários e outros
=> Imutável: Tuplas, Strings, números, True, False, None

Para ter os resultados de listas separadas dentro de uma função,
se aplica lista=None.
"""


def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_clientes_1 = ['Igor', 'Tamara']
cliente1 = lista_de_clientes(['Carlos', 'Camila', 'Deborah'], lista_clientes_1)
cliente2 = lista_de_clientes(['Zeka', 'Pablo', 'Thais'])
cliente3 = lista_de_clientes(['Otavio'])


print(cliente1)
print(cliente2)
print(cliente3)
