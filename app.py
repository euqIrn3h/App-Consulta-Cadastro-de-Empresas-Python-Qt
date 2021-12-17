from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import *
from layout import Ui_MainWindow
from PySide6.QtGui import QIcon
import sys


class mw(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mw,self).__init__()
        self.setupUi(self)
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

        #Toogle button

        self.pbtoogle.clicked.connect(self.LeftMenu)

        #Botoes do menu
        self.pbhome.clicked.connect(lambda: self.Pages.setCurrentWidget(self.Home))
        self.pbcadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.Cadastrar))
        self.pbcontatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.Contatos))
        self.pbsobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.Sobre))

    def LeftMenu(self):
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mw()
    window.show()
    app.exec()
