from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tela_Resultado(object):
    """

        Classe que contem todas as configurações da tela de resultados da ferramenta.

        Nessa classe usa-se propriedades da biblioteca PyQt5 para facilitar o
        gerenciamento das configurações e interações da tela em questão.

    """
    def setupUi(self, Tela_Resultado):
        Tela_Resultado.setObjectName("Tela_Resultado")
        Tela_Resultado.resize(922, 586)
        self.centralwidget = QtWidgets.QWidget(Tela_Resultado)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.setar_resultado = QtWidgets.QTextEdit(self.centralwidget)
        self.setar_resultado.setReadOnly(True)
        self.setar_resultado.setObjectName("setar_resultado")
        self.verticalLayout.addWidget(self.setar_resultado)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botao_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_voltar.setAutoFillBackground(False)
        self.botao_voltar.setObjectName("botao_voltar")
        self.horizontalLayout.addWidget(self.botao_voltar)
        self.bota_gerar_imagem = QtWidgets.QPushButton(self.centralwidget)
        self.bota_gerar_imagem.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bota_gerar_imagem.setObjectName("bota_gerar_imagem")
        self.horizontalLayout.addWidget(self.bota_gerar_imagem)
        self.botao_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_salvar.setObjectName("botao_salvar")
        self.horizontalLayout.addWidget(self.botao_salvar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Tela_Resultado.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Tela_Resultado)
        self.statusbar.setObjectName("statusbar")
        Tela_Resultado.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Resultado)
        QtCore.QMetaObject.connectSlotsByName(Tela_Resultado)

    def retranslateUi(self, Tela_Resultado):
        _translate = QtCore.QCoreApplication.translate
        Tela_Resultado.setWindowTitle(_translate("Tela_Resultado", "Tela de Resultados - GeMapCom"))
        self.botao_voltar.setText(_translate("Tela_Resultado", "VOLTAR"))
        self.bota_gerar_imagem.setText(_translate("Tela_Resultado", "GERAR IMAGEM"))
        self.botao_salvar.setText(_translate("Tela_Resultado", "SALVAR"))
