from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import *
from layout import Ui_MainWindow
from PySide6.QtGui import QIcon
import sys
from api import consulta


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

        self.lenome.setText(column[0])
        self.lelogradouro.setText(column[1])
        self.lenumero.setText(column[2])
        self.lecomplemento.setText(column[3])
        self.lebairro.setText(column[4])
        self.lemunicipio.setText(column[5])
        self.leuf.setText(column[6])                   
        self.lecep.setText(column[7].replace('.','').replace('-',''))    #replace para substituir os pontos e traços por uma string vazia para nao ter problema no sql
        self.letelefone.setText(column[8].replace('(','').replace(')','').replace('-',''))
        self.leemail.setText(column[9])






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mw()
    window.show()
    app.exec()
