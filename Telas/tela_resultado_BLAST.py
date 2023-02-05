from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
class Ui_tela_Resultado_BLAST(object):
    """

    Classe que contem todas as configurações da tela de resultados do BLAST.

    Nessa classe usa-se propriedades da biblioteca PyQt5 para facilitar o
    gerenciamento das configurações e interações da tela em questão.

    """
    def setupUi(self, Page_02):
        Page_02.setObjectName("Page_02")
        Page_02.resize(922, 586)
        Page_02.setDocumentMode(True)
        self.centralwidget = QWidget(Page_02)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QFrame.StyledPanel)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 900, 476))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Saida = QTextEdit(self.frame)
        self.Saida.setReadOnly(True)
        font = QFont("Consolas", 9)
        self.Saida.setFont(font)
        self.Saida.setObjectName("Saida")
        self.gridLayout_3.addWidget(self.Saida, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.Voltar = QPushButton(self.centralwidget)
        self.Voltar.setObjectName("Voltar")
        self.gridLayout.addWidget(self.Voltar, 1, 0, 1, 1)
        self.Finalizar = QPushButton(self.centralwidget)
        self.Finalizar.setObjectName("Finalizar")
        self.gridLayout.addWidget(self.Finalizar, 2, 0, 1, 1)
        Page_02.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Page_02)
        self.statusbar.setObjectName("statusbar")
        Page_02.setStatusBar(self.statusbar)

        self.retranslateUi(Page_02)
        QMetaObject.connectSlotsByName(Page_02)

    def resultadoFiltragem(self):
        """

            Função que abre e lê o arquivo "Filtragem.out" e ilustra o mesmo na
            tela.

        """
        Result = 'Filtragem.out'
        f = open(Result, 'r')
        file_text = f.read()
        self.Saida.setText(file_text)
        f.close()

    def resultadoAlinhamento(self):
        """

            Função que abre e lê o arquivo "ResultAlin.out" e ilustra o mesmo na
            tela.

        """
        Result = 'ResultAlin.out'
        f = open(Result, 'r')
        file_text = f.read()
        self.Saida.setText(file_text)
        f.close()

    def retranslateUi(self, Page_02):
        _translate = QCoreApplication.translate
        Page_02.setWindowTitle(_translate("Page_02", "MainWindow"))
        self.Voltar.setText(_translate("Page_02", "Voltar"))
        self.Finalizar.setText(_translate("Page_02", "Finalizar"))
