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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mw()
    window.show()
    app.exec()
