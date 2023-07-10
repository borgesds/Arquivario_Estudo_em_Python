import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        passwd='essaeasenha',
        db='dbtestes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()

        print('----- Conexão fechada!!! -----')


with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute("""SELECT ade, status, situacao_x
                          FROM tbl_dados_c
                          ORDER BY ade DESC
                          LIMIT 100""")
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
