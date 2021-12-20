from typing import Text
from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import *
from layout import Ui_MainWindow
from PySide6.QtGui import QIcon
import sys
from api import consulta
from database import database
import pandas as pd
import sqlite3 as sq


class mw(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mw,self).__init__()
        self.setupUi(self)
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        #Toogle button

        self.pbtoogle.clicked.connect(self.leftMenu)

        #Botoes do menu
        self.pbhome.clicked.connect(lambda: self.Pages.setCurrentWidget(self.Home))
        self.pbcadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.Cadastrar))
        self.pbcontatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.Contatos))
        self.pbsobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.Sobre))

        #Dados da empresa preenchido automaticamente
        self.lecnpj.editingFinished.connect(self.consultaApi)

        #Cadastrar a empresa no nosso banco de dados
        self.pbenviar.clicked.connect(self.cadastrarEmpresa)
        
        #Preenchendo a tabela com as empresas cadastradas
        self.listarEmpresa()

        #Alterando as empresas no Bd com alterações na tabela
        self.pbalterar.clicked.connect(self.alterarEmpresa)

        #Gerando o relatorio em excel.
        self.pbgerarexcel.clicked.connect(self.gerarExcel1)

        #Excluir empresa do BD
        self.pbexcluir.clicked.connect(self.excluirEmpresa)

    def leftMenu(self):
        x = self.LContainer.width()

        if x == 9:
            nx = 200
        else:
            nx = 9

        self.animation = QtCore.QPropertyAnimation(self.LContainer,b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(x)
        self.animation.setEndValue(nx)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def consultaApi(self):
        column = consulta(self.lecnpj.text().replace('/','').replace('.','').replace('-','').replace(" ",''))

        if column=='erro':
            pass
        else:
            self.lenome.setText(column[0].replace('-','').replace('/',''))
            self.lelogradouro.setText(column[1])
            self.lenumero.setText(column[2])
            self.lecomplemento.setText(column[3])
            self.lebairro.setText(column[4])
            self.lemunicipio.setText(column[5])
            self.leuf.setText(column[6])                   
            self.lecep.setText(column[7].replace('.','').replace('-',''))    #replace para substituir os pontos e traços por uma string vazia para nao ter problema no sql
            self.letelefone.setText(column[8].replace('(','').replace(')','').replace('-','').replace('/',''))
            self.leemail.setText(column[9])

    def cadastrarEmpresa(self):
        db = database()
        db.connect()

        fullDataSet = (
            self.lecnpj.text(),
            self.lenome.text(),
            self.lelogradouro.text(),
            self.lenumero.text(),
            self.lecomplemento.text(),
            self.lebairro.text(),
            self.lemunicipio.text(),            
            self.leuf.text(),                   
            self.lecep.text(),    
            self.letelefone.text(),
            self.leemail.text(),
        )

        #Cadastrar no banco de dados
        resposta = db.cadastrar(fullDataSet)

        if resposta=='erro':
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText("Empresa nao foi cadastrada!")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Cadastrado")
            msg.setText("Empresa cadastrada com SUCESSO!")
            msg.exec()
            db.close()

    def listarEmpresa(self):
        db = database()
        db.connect()   
        resultado = db.listar()

        self.tbl0.clearContents()
        self.tbl0.setRowCount((len(resultado)))

        for linha, t in enumerate(resultado):
            for coluna, d in enumerate(t):
                self.tbl0.setItem(linha,coluna,QTableWidgetItem(str(d)))

        db.close()

    def alterarEmpresa(self):
        dados =[]
        dadosnovos=[]

        for linha in range(self.tbl0.rowCount()):
            for coluna in range(self.tbl0.columnCount()):
                dados.append(self.tbl0.item(linha,coluna,).text())
            dadosnovos.append(dados)
            dados=[]

        db = database()
        db.connect()

        try:    
            for empresa in dadosnovos:
                db.alterar(tuple(empresa))
            msg = QMessageBox()
            msg.setWindowTitle("Cadastro alterado")
            msg.setText("Cadastro alterado com sucesso")
            msg.exec()

        except:
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText("Cadastro não foi alterado")
            msg.exec()

        db.close()

    def gerarExcel(self):           #Gera a planilha a partir do QTableWidget
                     
        x = []
        dados = []

        for linha in range(self.tbl0.rowCount()):
            for coluna in range(self.tbl0.columnCount()):
                x.append(self.tbl0.item(linha,coluna).text())
            dados.append(x)
            x=[]
        colunas = ['CNPJ','NOME','LOGRADOURO','NÚMERO','COMPLEMENTO','BAIRRO',
        'CIDADE','UF','CEP','TELEFONE','EMAIL']

        empresas = pd.DataFrame(dados,columns= colunas)
        empresas.to_excel("Empresas.xlsx", sheet_name='Empresas',index=False)

        msg = QMessageBox()
        msg.setWindowTitle("Relatório gerado")
        msg.setText("Relatório gerado com SUCESSO")
        msg.exec()
                             
    def gerarExcel1(self):          #Gera a planilha a partir do banco de dados

        bd = sq.connect("system.db")
        empresas = pd.read_sql_query("SELECT * FROM Empresa",bd)
        empresas.to_excel("EmpresasBd.xlsx", sheet_name='EmpresasBd',index=False)
        msg = QMessageBox()
        msg.setWindowTitle("Relatório gerado")
        msg.setText("Relatório gerado com SUCESSO")
        msg.exec()
            
    def excluirEmpresa(self):
        tbl = self.tbl0

        msg = QMessageBox()
        msg.setWindowTitle("Excluir essa Empresa ?")
        msg.setText("Você deseja mesmo EXCLUIR ?")
        msg.addButton("Excluir",msg.ButtonRole(True))
        msg.addButton("Não Excluir",msg.ButtonRole(False))
        msg.exec()
        if msg.clickedButton().text() == 'Excluir':
            msg = QMessageBox()                     #resetando a instancianda classe para nao ter o trabalho de apagar os botoes.
            try:
                db = database()
                db.connect()
                db.excluir(tbl.item(tbl.row(tbl.currentItem()),0).text()) 
                # tbl.item(tbl.row(tbl.currentItem()),0).text()Retorna o cnpj da empresa. Ele busca, na linha selecionada e coluna 0, o item que é lido pelo metodo item e devolvido poelo metodo text.
                msg.setWindowTitle("Excluido")
                msg.setText("Excluido com SUCESSO!")
                msg.exec()
            except:
                msg.setWindowTitle("Não Excluido")
                msg.setText("Selecione um campo para excluir")
                msg.exec()



if __name__ == "__main__":
    db = database()
    db.connect()
    db.ctable()
    db.close()

    app = QApplication(sys.argv)
    window = mw()
    window.show()
    app.exec()
