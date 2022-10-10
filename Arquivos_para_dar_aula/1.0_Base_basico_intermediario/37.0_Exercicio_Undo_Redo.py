"""
Faça uma lista de tarefas com os seguintes opções:
adicionar tarefa
listar tarefas
opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
opção de refazer (a cada vez que chamarmos, refaz a última ação)
"""


def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer!!!')
        return

    # Se tiver, desfazer e add na redo_list
    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer!!!')
        return

    # Se tiver, refazer e add na todo_list
    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []  # type: list[str]
    redo_list = []  # type: list[str]

    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls: ')

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)
