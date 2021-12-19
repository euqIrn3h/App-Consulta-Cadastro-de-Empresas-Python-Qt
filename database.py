import sqlite3
from sqlite3.dbapi2 import Cursor

class manutencao():
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
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS Empresa(
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
        colunas=('CNPJ','NOME','LOGRADOURO','NUMERO','COMPLEMENTO','BAIRRO','MUNICIPIO','UF','CEP','TELEFONE','EMAIL')
        quantidade=("?,?,?,?,?,?,?,?,?,?,?")

        cursor= self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Empresa {colunas} VALUES({quantidade})""",fullDataSet)
            self.connection.commit()
        except:
            return "erro"

    def listar(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Empresa ORDER BY NOME")
            empresas= cursor.fetchall()
            return empresas
        except:
            return "Erro"

    def excluir(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM Empresa WHERE CNPJ == '{id}'")
            self.connection.commit()
            return "Excluida com sucesso"
        except:
            "Erro"
    
    def alterar(self,fullDataSet):
        cursor = self.connection.cursor()
        cursor.execute(f"""UPDATE Empresa set 
                CNPJ = '{fullDataSet[0]}',
                NOME = '{fullDataSet[1]}',
                LOGRADOURO = '{fullDataSet[2]}',
                NUMERO = '{fullDataSet[3]}',
                COMPLEMENTO = '{fullDataSet[4]}',
                BAIRRO = '{fullDataSet[5]}',
                MUNICIPIO = '{fullDataSet[6]}',
                UF = '{fullDataSet[7]}',
                CEP = '{fullDataSet[8]}',
                TELEFONE = '{fullDataSet[9]}',
                EMAIL = '{fullDataSet[10]}'

                WHERE CNPJ = '{fullDataSet[0]}'""")

        self.connection.commit()
        