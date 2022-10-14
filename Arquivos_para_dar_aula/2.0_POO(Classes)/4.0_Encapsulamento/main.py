"""
public, protected, private
_ private
__ renomeia para outro atributo atrás do nome
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_clientes(1, 'Carlos')
bd.inserir_clientes(2, 'Maria')
bd.inserir_clientes(3, 'Amanda')

bd.apagar_cliente(2)
bd.lista_clientes()
