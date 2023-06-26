import csv


with open('clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)
    next(dados)

    for dado in dados:
        print(dado)

with open('clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar="",
        quoting=csv.QUOTE_ALL
    )
    
    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone'],
            ]
        )
