from pessoas import Pessoa

p1 = Pessoa('Carlos', 31)
p2 = Pessoa('Adriely', 19)

p1.falar('POO')
p2.falar('Novelas')
p2.comer('Maçã')
p2.falar('filmes')
p1.falar('Banco de dados')

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
