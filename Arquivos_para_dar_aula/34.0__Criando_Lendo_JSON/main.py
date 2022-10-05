import json


d1 = {
    'pessoa 1': {
        'nome': 'Luiz',
        'idade': 25,
    },
    'pessoa 2': {
        'nome': 'Carlos',
        'idade': 38,
    },
}

# converter o dicionario para JSON
d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:  # criar um arquivo json
    file.write(d1_json)  # escrever o arquivo json
