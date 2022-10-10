"""
Funções -def em python (parte2)
"""


def funcao(var):
    return var


variavel = funcao("Valor que eu quero")

if variavel:
    print(variavel)
else:
    print("Nenhum valor")


def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


divide = divisao(8, 4)

if divide:
    print(divide)
else:
    print("Conta invalida")
