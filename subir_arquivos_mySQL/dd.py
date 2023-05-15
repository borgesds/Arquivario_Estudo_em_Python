# buscar do arquivo conexao o criar_conexao e fechar_conexao
from conexao import criar_conexao, fechar_conexao
import pandas as pd


def insert_banco(nome, cpf, status_atendimento):
    con = criar_conexao("localhost", "root", "xxxxxxxxxxxxxx", "dbtestes")
    cursor = con.cursor()

    sql = """INSERT INTO tbl_teste (
            nome, cpf, status_atendimento) VALUES (%s, %s, %s)"""
    valores = nome, cpf, status_atendimento

    cursor.execute(sql, valores)

    cursor.close()
    con.commit()
    fechar_conexao(con)


# INITIALIZE
# Ler arquivo
df = pd.read_csv('teste_2.csv', sep=";")


# dados para inserção
for i, l in df.iterrows():
    nome, cpf, status_atendimento = (l[0], l[1], l[2])
    insert_banco(nome, cpf, status_atendimento)
    print(nome, cpf, status_atendimento)









