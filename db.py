import sqlite3
from sqlite3.dbapi2 import Cursor

class db():
    def __init__(self, name='system.db') -> None:
        self.name = name
        
    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close(self):
        try:
            self.connection.close()
        except:
            print("Nao foi possivel desconectar")
    def ctable(self):
        cursor = self.connection.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXIST empresa(
                CNPJ TEXT,
                NOME TEXT,
                LOGRADOURO TEXT,
                NUMERO TEXT,
                COMPLEMENTO TEXT,
                BAIRRO TEXT,
                MUNICIPIO TEXT,
                UF TEXT,
                CEP TEXT,
                TELEFONE TEXT,
                EMAIL TEXT,

                PRIMARY KEY(CNPJ)            );"""
        )

    def cadastrar(self,fullDataSet):
        colunas=('CNPJ','NOME','LOGRADOURO','BAIRRO','NUMERO','COMPLEMENTO','MUNICIPIO','UF','CEP','TELEFONE','EMAIL')
        quantidade=("?,?,?,?,?,?,?,?,?,?,?")

        cursor= self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Empresas {colunas} VALUES({quantidade})""",fullDataSet)
            return "OK"
        except:
            return "Erro"

    def tabela(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Empresas ORDER BY NOME")
            empresas= cursor.fetchall()
            return empresas
        except:
            return "Erro"

    def excluir(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Empresas WHERE CNPJ == '{id}'")
            self.connection.commit()
            return "Excluida com sucesso"
        except:
            "Erro"
    
    def alterar(self,fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Empresas set 
                CNPJ = '{fullDataSet[0]}',
                NOME = '{fullDataSet[1]}',
                LOGRADOURO = '{fullDataSet[2]}',
                NUMERO = '{fullDataSet[3]}',
                COMPLEMENTO = '{fullDataSet[4]}',
                BAIRRO = {fullDataSet[5]}
                MUNICIPIO = '{fullDataSet[6]}',
                UF = '{fullDataSet[7]}',
                CEP = '{fullDataSet[8]}',
                TELEFONE = '{fullDataSet[9]}',
                EMAIL = '{fullDataSet[10]}',
                WHERE CNPJ = '{fullDataSet[0]}'""")

        self.connection.commit()
        