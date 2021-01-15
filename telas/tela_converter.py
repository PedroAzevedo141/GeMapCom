from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tela_Converter(object):
    """

    Classe que contem todas as configurações da tela de converter da ferramenta.

    Nessa classe usa-se propriedades da biblioteca PyQt5 para facilitar o
    gerenciamento das configurações e interações da tela em questão.

    """
    def setupUi(self, Tela_Converter):
        Tela_Converter.setObjectName("Tela_Converter")
        Tela_Converter.resize(812, 585)
        Tela_Converter.setFixedSize(812, 585)
        self.centralwidget = QtWidgets.QWidget(Tela_Converter)
        self.centralwidget.setObjectName("centralwidget")
        self.botao_voltar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_voltar.setGeometry(QtCore.QRect(10, 10, 99, 27))
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap("images/voltar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.botao_voltar.setIcon(icon)
        self.botao_voltar.setObjectName("botao_voltar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 821, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(180, 70, 151, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 151, 17))
        self.label.setObjectName("label")
        self.botao_abrir_arquivo = QtWidgets.QPushButton(self.centralwidget)
        self.botao_abrir_arquivo.setGeometry(QtCore.QRect(10, 500, 118, 27))
        self.botao_abrir_arquivo.setObjectName("botao_abrir_arquivo")
        self.botao_converter = QtWidgets.QPushButton(self.centralwidget)
        self.botao_converter.setGeometry(QtCore.QRect(700, 500, 97, 27))
        self.botao_converter.setObjectName("botao_converter")
        self.setar_sequencia = QtWidgets.QTextEdit(self.centralwidget)
        self.setar_sequencia.setGeometry(QtCore.QRect(15, 110, 781, 371))
        self.setar_sequencia.setReadOnly(True)
        self.setar_sequencia.setObjectName("setar_sequencia")
        Tela_Converter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tela_Converter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 25))
        self.menubar.setObjectName("menubar")
        Tela_Converter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tela_Converter)
        self.statusbar.setObjectName("statusbar")
        Tela_Converter.setStatusBar(self.statusbar)

        self.retranslateUi(Tela_Converter)
        QtCore.QMetaObject.connectSlotsByName(Tela_Converter)

    def retranslateUi(self, Tela_Converter):
        _translate = QtCore.QCoreApplication.translate
        Tela_Converter.setWindowTitle(_translate("Tela_Converter", "Tela de Converter"))
        self.botao_voltar.setText(_translate("Tela_Converter", "VOLTAR"))
        self.comboBox.setItemText(0, _translate("Tela_Converter", "GENBANK - FASTA"))
        self.comboBox.setItemText(1, _translate("Tela_Converter", "FASTQ - FASTA"))
        self.label.setText(_translate("Tela_Converter", "TIPO DE CONVERSÃO: "))
        self.botao_abrir_arquivo.setText(_translate("Tela_Converter", "ABRIR ARQUIVO"))
        self.botao_converter.setText(_translate("Tela_Converter", "CONVERTER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Converter = QtWidgets.QMainWindow()
    ui = Ui_Tela_Converter()
    ui.setupUi(Tela_Converter)
    Tela_Converter.show()
    sys.exit(app.exec_())
