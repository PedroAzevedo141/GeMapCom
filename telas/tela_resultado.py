from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tela_Resultado(object):
    """

    Classe que contem todas as configurações da tela de resultados da ferramenta.

    Nessa classe usa-se propriedades da biblioteca PyQt5 para facilitar o
    gerenciamento das configurações e interações da tela em questão.

    """
    def setupUi(self, Tela_Resultado):
        Tela_Resultado.setObjectName("Tela_Resultado")
        Tela_Resultado.resize(1276, 585)
        Tela_Resultado.setFixedSize(1276, 585)
        self.centralwidget = QtWidgets.QWidget(Tela_Resultado)
        self.centralwidget.setObjectName("centralwidget")
        self.setar_resultado = QtWidgets.QTextEdit(self.centralwidget)
        self.setar_resultado.setGeometry(QtCore.QRect(13, 74, 1251, 431))
        self.setar_resultado.setReadOnly(True)
        self.setar_resultado.setObjectName("setar_resultado")
        self.botao_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_voltar.setGeometry(QtCore.QRect(10, 10, 99, 27))
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("images/voltar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.botao_voltar.setIcon(icon)
        self.botao_voltar.setObjectName("botao_voltar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 1276, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.botao_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_salvar.setGeometry(QtCore.QRect(1160, 520, 99, 27))
        self.botao_salvar.setObjectName("botao_salvar")
        self.bota_gerar_imagem = QtWidgets.QPushButton(self.centralwidget)
        self.bota_gerar_imagem.setGeometry(QtCore.QRect(1030, 520, 121, 27))
        self.bota_gerar_imagem.setObjectName("bota_gerar_imagem")
        Tela_Resultado.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_Resultado)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1276, 25))
        self.menubar.setObjectName("menubar")
        Tela_Resultado.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tela_Resultado)
        self.statusbar.setObjectName("statusbar")
        Tela_Resultado.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Resultado)
        QtCore.QMetaObject.connectSlotsByName(Tela_Resultado)

    def retranslateUi(self, Tela_Resultado):
        _translate = QtCore.QCoreApplication.translate
        Tela_Resultado.setWindowTitle(_translate("Tela_Resultado", "Tela de Resultado"))
        self.botao_voltar.setText(_translate("Tela_Resultado", "VOLTAR"))
        self.botao_salvar.setText(_translate("Tela_Resultado", "SALVAR"))
        self.bota_gerar_imagem.setText(_translate("Tela_Resultado", "GERAR IMAGEM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Resultado = QtWidgets.QMainWindow()
    ui = Ui_Tela_Resultado()
    ui.setupUi(Tela_Resultado)
    Tela_Resultado.show()
    sys.exit(app.exec_())
