from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_Tela_Resultado(object):
    """

        Classe que contem todas as configurações da tela de resultados da ferramenta.

        Nessa classe usa-se propriedades da biblioteca PyQt5 para facilitar o
        gerenciamento das configurações e interações da tela em questão.

    """
    def setupUi(self, Tela_Resultado):
        Tela_Resultado.setObjectName("Tela_Resultado")
        Tela_Resultado.resize(1000, 600)
        self.centralwidget = QWidget(Tela_Resultado)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.setar_resultado = QTextEdit(self.centralwidget)
        self.setar_resultado.setReadOnly(True)
        self.setar_resultado.setObjectName("setar_resultado")
        self.verticalLayout.addWidget(self.setar_resultado)
        self.line = QFrame(self.centralwidget)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.botao_voltar = QPushButton(self.centralwidget)
        self.botao_voltar.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_voltar.setAutoFillBackground(False)
        self.botao_voltar.setObjectName("botao_voltar")
        self.horizontalLayout.addWidget(self.botao_voltar)
        self.bota_gerar_imagem = QPushButton(self.centralwidget)
        self.bota_gerar_imagem.setCursor(QCursor(Qt.PointingHandCursor))
        self.bota_gerar_imagem.setObjectName("bota_gerar_imagem")
        self.horizontalLayout.addWidget(self.bota_gerar_imagem)
        self.botao_salvar = QPushButton(self.centralwidget)
        self.botao_salvar.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao_salvar.setObjectName("botao_salvar")
        self.horizontalLayout.addWidget(self.botao_salvar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Tela_Resultado.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Tela_Resultado)
        self.statusbar.setObjectName("statusbar")
        Tela_Resultado.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Resultado)
        QMetaObject.connectSlotsByName(Tela_Resultado)

    def retranslateUi(self, Tela_Resultado):
        _translate = QCoreApplication.translate
        Tela_Resultado.setWindowTitle(_translate("Tela_Resultado", "Tela de Resultados - GeMapCom"))
        self.botao_voltar.setText(_translate("Tela_Resultado", "VOLTAR"))
        self.bota_gerar_imagem.setText(_translate("Tela_Resultado", "GERAR IMAGEM"))
        self.botao_salvar.setText(_translate("Tela_Resultado", "SALVAR"))
