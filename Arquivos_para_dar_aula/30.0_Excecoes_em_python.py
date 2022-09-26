def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print(error)
        return False

print(divide(2, 0))

print()


def divide2(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print('Log', error)
        raise  # cria uma exceção


try:
    print(divide2(2, 0))
except ZeroDivisionError as error:
    print(error)

print()

# criar a propria exceção


def divide3(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0.")
    return n1 / n2


try:
    print(divide3(3, 0))
except ValueError as error:
    print('Você esta tentando dividir oir zero.')
    print('Log ', error)
