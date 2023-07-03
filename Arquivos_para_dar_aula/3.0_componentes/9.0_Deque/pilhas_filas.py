from collections import deque
from time import sleep

"""
fila = deque()

fila.append('Carlinhos')
fila.append('Eduarda')
fila.append('Carla')
fila.append('Valeria')
fila.append('Camila')
fila.append('André')
fila.append('Plinio')
fila.append('Cesarino')

print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')

for nome in fila:
    print(nome)
"""

"""
fila = deque(maxlen=5)

fila.extend([1, 2, 3, 4])
fila.append(5)
fila.append(6)
fila.append(7)

print(fila)
"""

"""
fila = deque(maxlen=10)

for i in range(1000):
    fila.append(i)
    sleep(1)
    print(fila)
"""

fila = deque(maxlen=10)

fila.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
fila.insert(2, 'Luiz Otávio')
print(fila)
