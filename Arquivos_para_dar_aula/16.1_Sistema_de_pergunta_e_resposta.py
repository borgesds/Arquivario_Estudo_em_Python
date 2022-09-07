print()
print('Responda de forma clara, digite a letra da sua resposta.')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto que é 2+2?',
        'respostas': {'a': '5', 'b': '4', 'c': '3', 'd': '6'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto que é 5*2?',
        'respostas': {'a': '25', 'b': '43', 'c': '10', 'd': '16'},
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto que é 2/2?',
        'respostas': {'a': '1', 'b': '4', 'c': '0', 'd': '6'},
        'resposta_certa': 'a',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto que é 70-5?',
        'respostas': {'a': '55', 'b': '45', 'c': '35', 'd': '65'},
        'resposta_certa': 'd',
    },
}

respostas_certas = 0

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Resposta: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    print()

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('RESPOSTA CERTA!!!')
        respostas_certas += 1
    else:
        print('RESPORTA ERRADA!!!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')