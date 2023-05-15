import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xxxxxxxxxx",
    database="dbtestes"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE if NOT EXISTS tbl_dados_c (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nun_cpf VARCHAR(15),
    status VARCHAR(50),
    sevico VARCHAR(255),
    loja VARCHAR(10),
    tipo_x VARCHAR(10),
    valor_x VARCHAR(35),
    situacao_x VARCHAR(15),
    tipo_y VARCHAR(10),
    valor_y VARCHAR(35),
    situacao_y VARCHAR(15),
    seguro_valor VARCHAR(35),
    status_seguro VARCHAR (255)
);""")
