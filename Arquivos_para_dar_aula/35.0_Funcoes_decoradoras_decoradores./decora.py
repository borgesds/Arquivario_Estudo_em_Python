def master(funcao):
    def slave(*args, **kwargs):  # vai receber qualquer parâmetro
        print('Agora estou decorada')  # que tiver um @
        funcao(*args, **kwargs)
    return slave


@master
def fala_oi():
    print('Oi')


fala_oi()


@master
def outra_funcao(msg):
    print(msg)


outra_funcao('Ola eu sou o André')