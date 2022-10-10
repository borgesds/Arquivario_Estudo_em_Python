from vendas import calc_precos

preco = 49.90
precos_com_aumento = calc_precos.aumento(preco, 15)
print(precos_com_aumento)

# ou

from vendas .calc_precos import aumento, reducao
from vendas.formata import preco as formata

preco = 49.90
precos_com_aumento = aumento(preco, 15, formata=True)
print(precos_com_aumento)

precos_com_reducao = reducao(preco, 15, formata=True)
print(precos_com_reducao)

print(formata.real(preco))  # busca do import
