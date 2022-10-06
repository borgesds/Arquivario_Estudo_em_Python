from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        # transformar em milesegundos
        tempo = (end_time - start_time) * 1000
        print(f'Afunção {funcao.__name__} levou {tempo}ms para executar')
        return resultado
    return interna


@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)


demora()
