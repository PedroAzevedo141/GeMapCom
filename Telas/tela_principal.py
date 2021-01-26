from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tela_Principal(object):
    """

    Classe que contem todas as configurações da tela inicial da ferramenta.

    Nessa classe usa-se propriedades da biblioteca PyQt5 para facilitar o
    gerenciamento das configurações e interações da tela em questão.

    """
    def setupUi(self, Tela_Principal):
        Tela_Principal.setObjectName("Tela_Principal")
        Tela_Principal.resize(1276, 585)
        Tela_Principal.setFixedSize(1276, 585)
        self.centralwidget = QtWidgets.QWidget(Tela_Principal)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 10, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 1276, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.botao_tela_comparacao = QtWidgets.QPushButton(self.centralwidget)
        self.botao_tela_comparacao.setGeometry(QtCore.QRect(550, 90, 191, 91))
        self.botao_tela_comparacao.setObjectName("botao_tela_comparacao")
        self.botao_tela_converter = QtWidgets.QPushButton(self.centralwidget)
        self.botao_tela_converter.setGeometry(QtCore.QRect(550, 200, 191, 91))
        self.botao_tela_converter.setObjectName("botao_tela_converter")
        self.botao_tela_outras = QtWidgets.QPushButton(self.centralwidget)
        self.botao_tela_outras.setGeometry(QtCore.QRect(550, 310, 191, 91))
        self.botao_tela_outras.setObjectName("botao_tela_outras")
        self.botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sair.setGeometry(QtCore.QRect(550, 420, 191, 91))
        self.botao_sair.setObjectName("botao_sair")
        Tela_Principal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_Principal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1276, 25))
        self.menubar.setObjectName("menubar")
        Tela_Principal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tela_Principal)
        self.statusbar.setObjectName("statusbar")
        Tela_Principal.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Principal)
        QtCore.QMetaObject.connectSlotsByName(Tela_Principal)

    def retranslateUi(self, Tela_Principal):
        _translate = QtCore.QCoreApplication.translate
        Tela_Principal.setWindowTitle(_translate("Tela_Principal", "Tela Inicial"))
        self.label.setText(_translate("Tela_Principal", "GeMapCom"))
        self.botao_tela_comparacao.setText(_translate("Tela_Principal", "COMPARAR SEQUÊNCIAS"))
        self.botao_tela_converter.setText(_translate("Tela_Principal", "CONVERTER SEQUÊNCIAS"))
        self.botao_tela_outras.setText(_translate("Tela_Principal", "OUTRAS FERRAMENTAS"))
        self.botao_sair.setText(_translate("Tela_Principal", "SAIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Principal = QtWidgets.QMainWindow()
    ui = Ui_Tela_Principal()
    ui.setupUi(Tela_Principal)
    Tela_Principal.show()
    sys.exit(app.exec_())
