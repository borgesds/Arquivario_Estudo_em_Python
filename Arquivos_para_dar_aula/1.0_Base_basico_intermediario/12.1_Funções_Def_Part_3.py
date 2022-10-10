"""
Funções -def em python -*args **kwargs (parte3)
"""


def func(*args):
    args = list(args)
    args[0] = 20
    print(args)


func(1, 2, 3, 4, 5)


def func2(*args):
    for v in args:
        print(v)


func2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def func3(*args):
    print(args)


lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [9, 10, 11, 12, 13, 14, 15, 16]
# desempacotamento da lista
func3(*lista, *lista2)


# **kwargs são argumentos nomeados
def func4(*args, **kwargs):
    print(args)
    print(kwargs)
    print(kwargs['nome'], kwargs['sobrenome'])


lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [9, 10, 11, 12, 13, 14, 15, 16]
# desempacotamento da lista
func4(*lista, *lista2, nome='Carlos', sobrenome='Pires')


# **kwargs são argumentos nomeados
def func5(*args, **kwargs):
    print(args)


# descobrir se foi enviado
    nome = kwargs.get('nome')
    idade = kwargs.get('idade')

    if nome is not None:
        print(nome)
    else:
        print('Nome não existe')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')


lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [9, 10, 11, 12, 13, 14, 15, 16]
# desempacotamento da lista
func5(*lista, *lista2, nome='Carlos', sobrenome='Pires')
