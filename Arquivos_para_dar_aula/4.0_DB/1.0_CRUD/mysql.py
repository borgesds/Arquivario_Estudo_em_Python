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
        sql = 'INSERT INTO tbl_dados_c (ade, status, valor_x, situacao_x) VALUES'\
              '(%s, %s, %s, %s)'

        valor = (81111111, 'TESTE', '5555555', 'TESTE-')

        cursor.execute(sql, valor)
        conexao.commit()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO tbl_dados_c (ade, status, valor_x, situacao_x) VALUES'\
              '(%s, %s, %s, %s)'

        dados = [
            (81111112, 'TESTE', '84555', 'TESTE-'),
            (81111113, 'TESTE', '53355', 'TESTE-'),
            (81111114, 'TESTE', '11555', 'TESTE-'),
            (81111115, 'TESTE', '955', 'TESTE-'),
                 ]

        cursor.executemany(sql, dados)
        conexao.commit()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM tbl_dados_c WHERE ade IN (%s, %s, %s)'

        dados = (81111112, 81111113, 81111114)

        cursor.execute(sql, dados)
        conexao.commit()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE tbl_dados_c SET valor_x=%s WHERE ade=%s'

        dados = (1000, 81111111)

        cursor.execute(sql, dados)
        conexao.commit()


with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute("""SELECT ade, status, situacao_x
                          FROM tbl_dados_c
                          ORDER BY ade DESC
                          LIMIT 100""")
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)
