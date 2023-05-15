from conexao import criar_conexao, fechar_conexao
import pandas as pd
import datetime


def insert_banco(
    nun_cpf,
    status,
    sevico,
    loja,
    tipo_x,
    valor_x,
    situacao_x,
    tipo_y,
    valor_y,
    situacao_y,
    seguro_valor,
    status_seguro,
):
    con = criar_conexao("localhost", "root", "xxxxxxxxxx", "dbtestes")
    cursor = con.cursor()

    sql = """INSERT INTO tbl_dados_c (
            nun_cpf, status, sevico, loja,
            tipo_x, valor_x, situacao_x, tipo_y,
            valor_y, situacao_y, seguro_valor,
            status_seguro) VALUES (%s, %s, %s, %s, %s, %s, %s,
                                   %s, %s, %s, %s,%s)
          """

    valores = (
        nun_cpf,
        status,
        sevico,
        loja,
        tipo_x,
        valor_x,
        situacao_x,
        tipo_y,
        valor_y,
        situacao_y,
        seguro_valor,
        status_seguro,
    )

    cursor.execute(sql, valores)

    cursor.close()
    con.commit()
    fechar_conexao(con)


# INITIALIZE
# Ler arquivo
df = pd.read_csv("teste_1.csv", sep=";")
df = df.fillna("")


# dados para inserção
for i, l in df.iterrows():
    insert_banco(
        l[0], l[1], l[2], l[3], l[4], l[5],
        l[6], l[7], l[8], l[9], l[10], l[11]
    )

    agora = datetime.datetime.now()

    print(
        f"""{agora.time()} =>
          Subindo para o banco de dados index = {i}

          -------------------------------------------------------
          """
    )

print("FINALIZADO!!")
