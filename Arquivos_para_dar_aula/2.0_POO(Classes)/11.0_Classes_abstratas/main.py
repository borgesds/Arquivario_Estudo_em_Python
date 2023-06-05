from classes.contapoupanca import ContaPoupanca
from classes.contacorrente import ContaCorrente

cp = ContaPoupanca(1111, 222, 0)
cp.depositar(10)
cp.sacar(5)

print('______________________________')

cc = ContaCorrente(agencia=1111, conta=3443, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1200)
