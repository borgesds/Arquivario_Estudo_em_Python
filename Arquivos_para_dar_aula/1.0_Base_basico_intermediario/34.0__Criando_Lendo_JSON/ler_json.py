import json


with open('abc.json', 'r') as file:
    d1_json = file.read()  # lendo o arquivo json
    print(d1_json)
    d1_json = json.loads(d1_json)  # tranformando em dicionario
    print(d1_json)

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
