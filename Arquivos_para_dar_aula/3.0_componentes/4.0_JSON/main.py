from dados import *
import json

"""
# buscando JSOn
dados_json = json.dumps(clientes_dicionario, indent=4)
print(dados_json)

# converter em JSON
dicionario = json.loads(clientes_json)

for chave, valor in dicionario.items():
    print(chave, valor)
"""

# converter e criar um arquivo  JSON
with open('clientes.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)
    
# converter emum dicionario
with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

for chave, valor in dados.items():
    print(chave, valor)
