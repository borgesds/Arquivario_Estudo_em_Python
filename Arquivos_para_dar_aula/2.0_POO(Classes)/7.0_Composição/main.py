from classes import Cliente


cliente1 = Cliente('Marcio', 48)
cliente1.insere_endereco('Sete Lagoa', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Camila Victoria', '27')
cliente2.insere_endereco('Rio Grande do Sul', 'RS')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Pablo', '55')
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()
