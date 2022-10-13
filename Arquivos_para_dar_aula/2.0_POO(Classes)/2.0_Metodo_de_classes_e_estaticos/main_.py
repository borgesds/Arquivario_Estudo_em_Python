from random import randint


class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método de instância
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Método da classe
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # Método estáticos
    # Ele não usa a classe cls e nem a instância self
    @staticmethod
    def gerar_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa('Carlos', 34)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gerar_id())
print(p1.gerar_id())
