"""
Um dos jeitos de chamar o modulo é:
import calculos  # Aqui vai chamar tudo que está dentro do módulo

Ex. Execução:
print(calculos.PI)

list = [2, 4]
print(calculos.multiplica(lista))

print(calculos.dobra_lista(lista))

dessa forma o código fica muito longo,
e usual quando  se tem que usar tudo que o módulo oferece.
"""
# o jeito mais certo de se fazer e chamando que precisa

from calculos import multiplica, dobra_lista, PI
from outro import falar_oi

print(multiplica([2, 3]))

print(dobra_lista([3, 4, 5, 6]))

print(PI)

falar_oi()
