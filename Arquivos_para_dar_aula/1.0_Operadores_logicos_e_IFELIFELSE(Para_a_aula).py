# Login no sistema
usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

qtd_caracteres = len(usuario)

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está conectado ao sistema')

else:
    print('Senha ou usuário inválidos')

# Analisando a senha
if qtd_caracteres < 8:
    print('Para uma a melhor proteção tenha uma senha'
          ' com 8 ou mais caracteres')

else:
    print('Bom Trabalho!!!')
