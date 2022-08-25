"""
Operadores ternário em python
"""

logged_user = True

msg = 'Usuario logado' if logged_user else 'Usuario precisa logar'
print(msg)

# acesso por idade
idade = input('Qual sua idade:')

if not idade.isnumeric():
    print('Digite apenas numero')
else:
    idade = int(idade)
    e_maior = (idade >= 18)
    msg = 'Pode acessar' if e_maior else 'Não pode acessar'
    print(msg)
