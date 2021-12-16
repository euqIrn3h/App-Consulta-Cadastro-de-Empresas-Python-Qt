import PyQt5.QtWidgets as qt
from PyQt5 import uic



app = qt.QApplication([])
ui = uic.loadUi("layout.ui")


ui.show()
app.exec()

