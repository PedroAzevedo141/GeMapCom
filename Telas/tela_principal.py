from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_Principal(object):
    """

      Classe que contem todas as configurações da tela inicial da ferramenta.

      Nessa classe usa-se propriedades da biblioteca PyQt5 para facilitar o
      gerenciamento das configurações e interações da tela em questão.

      """
    def setupUi(self, Tela_Principal):
        Tela_Principal.setObjectName("Tela_Principal")
        Tela_Principal.setWindowModality(QtCore.Qt.NonModal)
        Tela_Principal.resize(922, 586)
        Tela_Principal.setAutoFillBackground(False)
        Tela_Principal.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        Tela_Principal.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Tela_Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_sair.setObjectName("botao_sair")
        self.gridLayout.addWidget(self.botao_sair, 6, 0, 1, 1)
        self.botao_tela_converter = QtWidgets.QPushButton(self.centralwidget)
        self.botao_tela_converter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_tela_converter.setObjectName("botao_tela_converter")
        self.gridLayout.addWidget(self.botao_tela_converter, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.botao_tela_comparacao = QtWidgets.QPushButton(self.centralwidget)
        self.botao_tela_comparacao.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_tela_comparacao.setObjectName("botao_tela_comparacao")
        self.gridLayout.addWidget(self.botao_tela_comparacao, 0, 0, 1, 1)
        self.botao_tela_outras = QtWidgets.QPushButton(self.centralwidget)
        self.botao_tela_outras.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_tela_outras.setObjectName("botao_tela_outras")
        self.gridLayout.addWidget(self.botao_tela_outras, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(4)
        self.label.setMidLineWidth(0)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        Tela_Principal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Tela_Principal)
        self.statusbar.setObjectName("statusbar")
        Tela_Principal.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(Tela_Principal)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 922, 22))
        self.menuBar.setObjectName("menuBar")
        Tela_Principal.setMenuBar(self.menuBar)

        self.retranslateUi(Tela_Principal)
        QtCore.QMetaObject.connectSlotsByName(Tela_Principal)

    def retranslateUi(self, Tela_Principal):
        _translate = QtCore.QCoreApplication.translate
        Tela_Principal.setWindowTitle(_translate("Tela_Principal", "Tela Inicial - GeMapCom"))
        self.botao_sair.setText(_translate("Tela_Principal", "SAIR"))
        self.botao_tela_converter.setText(_translate("Tela_Principal", "CONVERTER SEQUENCIA"))
        self.botao_tela_comparacao.setText(_translate("Tela_Principal", "COMPARAR SEQUENCIAS"))
        self.botao_tela_outras.setText(_translate("Tela_Principal", "OUTRAS FERRAMENTAS"))
        self.label.setText(_translate("Tela_Principal", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">GeMapCom</span></p></body></html>"))
