# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'layout.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
from icones import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(614, 407)
        MainWindow.setStyleSheet(u"*{\n"
"background-color:rgb(0,0,0);\n"
"color:rgb(255,255,255);\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"background-color:rgb(150,150,150);\n"
"color:rgb(0,0,0);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0)\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0);\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LContainer = QFrame(self.centralwidget)
        self.LContainer.setObjectName(u"LContainer")
        self.LContainer.setMinimumSize(QSize(0, 0))
        self.LContainer.setMaximumSize(QSize(9, 16777215))
        self.LContainer.setFrameShape(QFrame.StyledPanel)
        self.LContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.LContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border: 1px;\n"
"border-style:solid;\n"
"border-color: white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"border: none")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.LContainer)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(120, 0))
        self.frame_2.setStyleSheet(u"border: 1px;\n"
"border-style:solid;\n"
"border-color: white;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"border:none;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 100, 258))
        self.page.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pbhome = QPushButton(self.page)
        self.pbhome.setObjectName(u"pbhome")

        self.verticalLayout_4.addWidget(self.pbhome)

        self.pbcadastrar = QPushButton(self.page)
        self.pbcadastrar.setObjectName(u"pbcadastrar")

        self.verticalLayout_4.addWidget(self.pbcadastrar)

        self.pbcontatos = QPushButton(self.page)
        self.pbcontatos.setObjectName(u"pbcontatos")

        self.verticalLayout_4.addWidget(self.pbcontatos)

        self.pbsobre = QPushButton(self.page)
        self.pbsobre.setObjectName(u"pbsobre")

        self.verticalLayout_4.addWidget(self.pbsobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Menu")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 100, 258))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.toolBox.addItem(self.page_2, u"Info")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.LContainer)

        self.MainContainer = QFrame(self.centralwidget)
        self.MainContainer.setObjectName(u"MainContainer")
        self.MainContainer.setMinimumSize(QSize(440, 0))
        self.MainContainer.setFrameShape(QFrame.StyledPanel)
        self.MainContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.MainContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TopFrame = QFrame(self.MainContainer)
        self.TopFrame.setObjectName(u"TopFrame")
        self.TopFrame.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(150,150,150);\n"
"color:rgb(0,0,0)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0)\n"
"}")
        self.TopFrame.setFrameShape(QFrame.StyledPanel)
        self.TopFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.TopFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pbtoogle = QPushButton(self.TopFrame)
        self.pbtoogle.setObjectName(u"pbtoogle")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbtoogle.sizePolicy().hasHeightForWidth())
        self.pbtoogle.setSizePolicy(sizePolicy)
        self.pbtoogle.setMinimumSize(QSize(30, 40))
        self.pbtoogle.setMaximumSize(QSize(30, 16777215))
        self.pbtoogle.setStyleSheet(u"background-image: url(:/icon/toogle.png);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color:white;\n"
"hover{\n"
"background-color:rgb(255,255,255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.pbtoogle, 0, Qt.AlignLeft)

        self.label = QLabel(self.TopFrame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(400, 0))
        self.label.setMaximumSize(QSize(400, 16777215))
        self.label.setFont(font)
        self.label.setStyleSheet(u"border:none")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.TopFrame)

        self.MainFrame = QFrame(self.MainContainer)
        self.MainFrame.setObjectName(u"MainFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MainFrame.sizePolicy().hasHeightForWidth())
        self.MainFrame.setSizePolicy(sizePolicy1)
        self.MainFrame.setMinimumSize(QSize(410, 0))
        self.MainFrame.setStyleSheet(u"border: 1px;\n"
"border-style:solid;\n"
"border-color: white;")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Pages = QStackedWidget(self.MainFrame)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"border:none")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.verticalLayout_8 = QVBoxLayout(self.Home)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.logo = QLabel(self.Home)
        self.logo.setObjectName(u"logo")

        self.verticalLayout_8.addWidget(self.logo)

        self.Pages.addWidget(self.Home)
        self.Cadastrar = QWidget()
        self.Cadastrar.setObjectName(u"Cadastrar")
        self.verticalLayout_9 = QVBoxLayout(self.Cadastrar)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidget = QTabWidget(self.Cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(370, 0))
        self.tabWidget.setStyleSheet(u"color:rgb(0,0,0);\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_12 = QVBoxLayout(self.tab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(211, 211, 211);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_5)


        self.verticalLayout_12.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pbgerarexcel = QPushButton(self.frame_4)
        self.pbgerarexcel.setObjectName(u"pbgerarexcel")

        self.verticalLayout_10.addWidget(self.pbgerarexcel)

        self.pbalterar = QPushButton(self.frame_4)
        self.pbalterar.setObjectName(u"pbalterar")

        self.verticalLayout_10.addWidget(self.pbalterar)

        self.pbexcluir = QPushButton(self.frame_4)
        self.pbexcluir.setObjectName(u"pbexcluir")

        self.verticalLayout_10.addWidget(self.pbexcluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_4)


        self.verticalLayout_12.addWidget(self.frame_5)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 4)

        self.lineEdit = QLineEdit(self.tab_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.tab_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 4)

        self.lineEdit_4 = QLineEdit(self.tab_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 3, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.tab_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 3, 1, 1, 2)

        self.lineEdit_6 = QLineEdit(self.tab_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 3, 3, 1, 1)

        self.lineEdit_7 = QLineEdit(self.tab_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 4, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.tab_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 4, 1, 1, 2)

        self.lineEdit_9 = QLineEdit(self.tab_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 4, 3, 1, 1)

        self.lineEdit_10 = QLineEdit(self.tab_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout.addWidget(self.lineEdit_10, 5, 0, 1, 2)

        self.lineEdit_11 = QLineEdit(self.tab_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout.addWidget(self.lineEdit_11, 5, 2, 1, 2)

        self.lineEdit_2 = QLineEdit(self.tab_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 3)

        self.pbenviar = QPushButton(self.tab_2)
        self.pbenviar.setObjectName(u"pbenviar")

        self.gridLayout.addWidget(self.pbenviar, 6, 1, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.Pages.addWidget(self.Cadastrar)
        self.Contatos = QWidget()
        self.Contatos.setObjectName(u"Contatos")
        self.verticalLayout_13 = QVBoxLayout(self.Contatos)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.Contatos)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.label_7)

        self.label_8 = QLabel(self.Contatos)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.label_8)

        self.label_9 = QLabel(self.Contatos)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.label_9)

        self.Pages.addWidget(self.Contatos)
        self.Sobre = QWidget()
        self.Sobre.setObjectName(u"Sobre")
        self.verticalLayout_7 = QVBoxLayout(self.Sobre)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(self.Sobre)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)

        self.Pages.addWidget(self.Sobre)

        self.verticalLayout_6.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.MainFrame)

        self.FooterFrame = QFrame(self.MainContainer)
        self.FooterFrame.setObjectName(u"FooterFrame")
        self.FooterFrame.setFont(font)
        self.FooterFrame.setFrameShape(QFrame.StyledPanel)
        self.FooterFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.FooterFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.FooterFrame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.FooterFrame)


        self.horizontalLayout.addWidget(self.MainContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cadastro-Consulta", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"scc", None))
        self.pbhome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pbcadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.pbcontatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.pbsobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Versao : 1.0.0\n"
"Autor : HenrIque", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Info", None))
        self.pbtoogle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"SISTEMA DE CADASTRO E CONSULTA", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icon/icon.png\"/></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Empresas", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.pbgerarexcel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.pbalterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.pbexcluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Empresa", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MUNIC\u00cdPIO", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME EMPRESARIAL", None))
        self.pbenviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icon/telefone.png\"/>Telefone</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icon/instagram.png\"/> Instagram</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icon/email.png\"/>Email</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Essa \u00e9 uma aplica\u00e7\u00e3o teste para fins de aprendizado.", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"(C) Henrique - 2021", None))
    # retranslateUi

