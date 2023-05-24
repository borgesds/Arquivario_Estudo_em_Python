from classes import Cliente, Aluno

"""
Associação - Usa | agregação - Composição - É dono | Herança - É
"""


c1 = Cliente('Luiz', 44)
c1.falar()
c1.comprar()


a1 = Aluno('Ingred', 23)
a1.falar()
a1.estudar()

