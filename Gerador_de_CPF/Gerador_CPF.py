from random import randint

numero = str(randint(100000000, 999999999))

novo_cpf = numero
# reverso pertence a primeira e segunda etapa
reverso = 10
total = 0

# index vai retornar x linhas para calcular o total
for index in range(19):
    if index > 8:                         # Primeiro índice vai de 0 a 9,
        index -= 9                        # São os 9 primeiros digitos CPF

    total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

    reverso -= 1                          # Decrementa o contador reverso
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:                         # Se o digito for > que 9 == 0
            d = 0
        # 11 > 9 = 0
        # Digito 1 = 0
        total = 0                         # Zera o total
        novo_cpf += str(d)                # Concatena o digito no novo cpf

print(novo_cpf)
