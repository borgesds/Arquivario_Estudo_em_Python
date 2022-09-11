"""
Exercicio List Comprehension
"""

string = '012345678901234567890123456789012345678901234567890123456789'
n = 10

# separar em lotes de 10
lista = [string[i:i+n] for i in range(0, len(string), n)]
# colocar um . por bloco
retorno = '.'.join(lista)

print(lista)
print(retorno)
