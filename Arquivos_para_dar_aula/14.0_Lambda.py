"""
Lambda
"""

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


a = lambda x, y: x + y


print(a(2, 2))


x = lambda a : a + 10
print(x(5))


def myfunc(n):
  return lambda a : a * n


mydoubler = myfunc(2)

print(mydoubler(11))



lista = [
    ['P1', 13],
    ['P2', 4],
    ['P3', 25],
    ['P4', 1],
    ['P5', 73],
]
print(sorted(lista))

# ordem crescente
print(sorted(lista, key=lambda x: x[1]))

# ordem decrescente
print(sorted(lista, key=lambda x: x[1], reverse=True))
