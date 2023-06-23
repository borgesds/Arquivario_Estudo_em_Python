import os
import shutil

caminho_original = '/home/borges/Downloads/'
caminho_novo = '/home/borges/Downloads/outros/'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} ja existe.')

"""
for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.pdf' in file:
            # mover arquivos para nova pasta
            shutil.move(old_file_path, new_file_path)
            print(f'Arquivo {file} copiado com sucesso.')

"""

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.pdf' in file:
            # deleta arquivos da pasta
            os.remove(new_file_path)
            print(f'Removendo arquivo {file} com sucesso.')
