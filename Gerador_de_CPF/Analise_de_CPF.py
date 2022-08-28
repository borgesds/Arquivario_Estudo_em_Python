"""
CPF = 168.995.350-09
------------------------------------------------
Primeira Etapa             Segunda Etapa
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""
# loop
while True:
    cpf = input('Digite um cpf: ')
    # cpf = '16899535009'
    # Elimina os dois últimos digitos do CPF
    novo_cpf = cpf[:-2]
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

    if cpf == novo_cpf:
        print('Válido')
    else:
        print('Inválido')
