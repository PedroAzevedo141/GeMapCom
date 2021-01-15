from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.centralwidget = QtWidgets.QWidget(Page_02)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 900, 476))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Saida = QtWidgets.QLabel(self.frame)
        self.Saida.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Saida.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Saida.setText("")
        self.Saida.setObjectName("Saida")
        self.gridLayout_3.addWidget(self.Saida, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.Voltar = QtWidgets.QPushButton(self.centralwidget)
        self.Voltar.setObjectName("Voltar")
        self.gridLayout.addWidget(self.Voltar, 1, 0, 1, 1)
        self.Finalizar = QtWidgets.QPushButton(self.centralwidget)
        self.Finalizar.setObjectName("Finalizar")
        self.gridLayout.addWidget(self.Finalizar, 2, 0, 1, 1)
        Page_02.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Page_02)
        self.statusbar.setObjectName("statusbar")
        Page_02.setStatusBar(self.statusbar)

        self.retranslateUi(Page_02)
        QtCore.QMetaObject.connectSlotsByName(Page_02)

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
        _translate = QtCore.QCoreApplication.translate
        Page_02.setWindowTitle(_translate("Page_02", "BLAST - Tela de Resultados"))
        self.Voltar.setText(_translate("Page_02", "Voltar"))
        self.Finalizar.setText(_translate("Page_02", "Finalizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Page_02 = QtWidgets.QMainWindow()
    ui = Ui_tela_Resultado_BLAST()
    ui.setupUi(Page_02)
    Page_02.show()
    sys.exit(app.exec_())
