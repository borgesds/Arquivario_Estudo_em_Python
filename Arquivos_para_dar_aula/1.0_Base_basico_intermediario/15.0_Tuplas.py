"""
Tuplas
Os argumentos que são utilizados em litas servem para tuplas
"""

t1 = (1, 2, 3, 4, 5, 'argumentos', 'Borges')

print(t1[4])
print(t1[6])
print(t1[5])


for v in t1:
    print(v)

print(t1[2:])
print(t1[:5])


# podemos criar sem ()
t1 = 1, 2, 3, 4, 5, 'argumentos', 'Borges'
t2 = 'zé', 23, -33, 'Igor'

# concatenar
t3 = t1 + t2
print(t3)

# modificar uma tupla
# tranfome primeiro em lista
t1 = list(t1)
# modfica tupla
t1[3] = 5000
# volta para tupla
t1 = tuple(t1)

print(t1)
