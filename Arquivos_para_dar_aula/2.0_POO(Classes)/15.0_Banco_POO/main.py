from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Carlos', 56)
cliente2 = Cliente('Kamilla', 25)
cliente3 = Cliente('Ryan', 22)

conta1 = ContaPoupanca(1111, 25254548, 0)
conta2 = ContaCorrente(2222, 25556698, 0)
conta3 = ContaPoupanca(1212, 25020699, 0)

cliente1.inser_conta(conta1)
cliente2.inser_conta(conta2)
cliente3.inser_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado')

print('\n')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(80)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado')
