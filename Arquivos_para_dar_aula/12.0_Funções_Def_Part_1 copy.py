"""
Funções -def em python (parte1)
"""


def funcao(msg, nome):
    print(msg, nome)


funcao('Oi', 'Luiz')


def saudacao(msg='Ola', nome='Usuario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)


saudacao(nome='Andrea', msg='Hi')
saudacao('Oi', 'Helena')
