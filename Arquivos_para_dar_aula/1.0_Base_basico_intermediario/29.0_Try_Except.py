try:
    a = 0
    try:
        a = 1 / 0
    except:
        print('Erro')
except NameError as erro:
    print(erro)
except (IndexError, KeyError) as erro:
    print(erro)
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    print('Seu código foi executado com sucesso!')
    print(a)
finally:
    print('Finalmente')
