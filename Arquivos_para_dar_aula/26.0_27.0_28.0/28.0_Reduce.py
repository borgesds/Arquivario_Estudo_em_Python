from dados import produtos, pessoas, lista
from functools import reduce

# acumulador
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
                    # ac = acumulador
                        # i = item a item
                            # i + ac = soma do acumulado e item
                    # lista = onde contem os itens
                    # 0 = O começo acumulado
print(soma_lista)


# produtos total
soma_preco = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_preco)
# media
print(f'Media de preços = {soma_preco / len(produtos)}')

# idade
soma_de_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_de_idades)
print(f'Media de idades = {soma_de_idades / len(pessoas)}')
