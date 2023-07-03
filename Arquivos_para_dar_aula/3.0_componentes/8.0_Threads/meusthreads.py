from time import sleep
from threading import Thread

"""
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 2)
t1.start()

t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 3', 5)
t3.start()

for i in range(20):
    print(i)
    sleep(1)
"""

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Ola mundo 1', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Ola mundo 2', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Ola mundo 3', 2))
t3.start()

for i in range(20):
    print(i)
    sleep(.5)
"""


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Ola mundo 1', 10))
t1.start()

while t1.is_alive():
    print('Esperando a thread')
    sleep(2)

print('Thread acabou')
