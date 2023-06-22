import os


caminho_procura = '/home/borges/Downloads'
termo_procura = 'train.csv'

conta = 0

for raiz, diretorio, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho:', tamanho)
            except PermissionError as e:
                print('Sem permissões, error:', e)
            except FileNotFoundError as e:
                print('Arquivo não encontrado, error:', e)
            except Exception as e:
                print('Error desconhecido, error:', e)

print()
print(f'{conta} arquivo(s) encontrado(s).')
