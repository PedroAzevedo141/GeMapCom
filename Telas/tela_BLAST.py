from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_tela_BLAST(object):
    """

    Classe que contem todas as configurações da tela inicial do BLAST.

    Nessa classe usa-se propriedades da biblioteca PyQt5 para facilitar o
    gerenciamento das configurações e interações da tela em questão.

    """
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 586)
        MainWindow.setFixedSize(922, 586)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 821, 479))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setLineWidth(3)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 3)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 2, 0, 1, 2)
        self.ButtonQuery = QtWidgets.QPushButton(self.frame_2)
        self.ButtonQuery.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonQuery.setObjectName("ButtonQuery")
        self.gridLayout_4.addWidget(self.ButtonQuery, 0, 1, 2, 1)
        self.ButtonSubject = QtWidgets.QPushButton(self.frame_2)
        self.ButtonSubject.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonSubject.setObjectName("ButtonSubject")
        self.gridLayout_4.addWidget(self.ButtonSubject, 4, 1, 2, 1)
        self.NomeArquivoSUBJECT = QtWidgets.QLineEdit(self.frame_2)
        self.NomeArquivoSUBJECT.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.NomeArquivoSUBJECT.setReadOnly(True)
        self.NomeArquivoSUBJECT.setObjectName("NomeArquivoSUBJECT")
        self.gridLayout_4.addWidget(self.NomeArquivoSUBJECT, 4, 0, 1, 1)
        self.CabecalhoArquivoSUBJECT = QtWidgets.QLineEdit(self.frame_2)
        self.CabecalhoArquivoSUBJECT.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.CabecalhoArquivoSUBJECT.setReadOnly(True)
        self.CabecalhoArquivoSUBJECT.setObjectName("CabecalhoArquivoSUBJECT")
        self.gridLayout_4.addWidget(self.CabecalhoArquivoSUBJECT, 5, 0, 1, 1)
        self.NomeArquivoQUERY = QtWidgets.QLineEdit(self.frame_2)
        self.NomeArquivoQUERY.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.NomeArquivoQUERY.setReadOnly(True)
        self.NomeArquivoQUERY.setObjectName("NomeArquivoQUERY")
        self.gridLayout_4.addWidget(self.NomeArquivoQUERY, 0, 0, 1, 1)
        self.CabecalhoArquivoQUERY = QtWidgets.QLineEdit(self.frame_2)
        self.CabecalhoArquivoQUERY.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.CabecalhoArquivoQUERY.setReadOnly(True)
        self.CabecalhoArquivoQUERY.setObjectName("CabecalhoArquivoQUERY")
        self.gridLayout_4.addWidget(self.CabecalhoArquivoQUERY, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 3)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.SalvarComo = QtWidgets.QLabel(self.frame_3)
        self.SalvarComo.setObjectName("SalvarComo")
        self.gridLayout_5.addWidget(self.SalvarComo, 0, 1, 1, 1)
        self.ASN1 = QtWidgets.QRadioButton(self.frame_3)
        self.ASN1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ASN1.setObjectName("ASN1")
        self.gridLayout_5.addWidget(self.ASN1, 3, 3, 1, 1)
        self.BLAST_Format = QtWidgets.QRadioButton(self.frame_3)
        self.BLAST_Format.setObjectName("BLAST_Format")
        self.gridLayout_5.addWidget(self.BLAST_Format, 4, 3, 1, 1)
        self.Comma = QtWidgets.QRadioButton(self.frame_3)
        self.Comma.setObjectName("Comma")
        self.gridLayout_5.addWidget(self.Comma, 4, 2, 1, 1)
        self.FLATIdentities = QtWidgets.QRadioButton(self.frame_3)
        self.FLATIdentities.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FLATIdentities.setObjectName("FLATIdentities")
        self.gridLayout_5.addWidget(self.FLATIdentities, 1, 2, 1, 1)
        self.FLATnoIdentities = QtWidgets.QRadioButton(self.frame_3)
        self.FLATnoIdentities.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FLATnoIdentities.setObjectName("FLATnoIdentities")
        self.gridLayout_5.addWidget(self.FLATnoIdentities, 2, 2, 1, 1)
        self.NoIdentities = QtWidgets.QRadioButton(self.frame_3)
        self.NoIdentities.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NoIdentities.setObjectName("NoIdentities")
        self.gridLayout_5.addWidget(self.NoIdentities, 3, 1, 1, 1)
        self.ShowingIdentities = QtWidgets.QRadioButton(self.frame_3)
        self.ShowingIdentities.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ShowingIdentities.setObjectName("ShowingIdentities")
        self.gridLayout_5.addWidget(self.ShowingIdentities, 2, 1, 1, 1)
        self.TextoBinary = QtWidgets.QRadioButton(self.frame_3)
        self.TextoBinary.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TextoBinary.setObjectName("TextoBinary")
        self.gridLayout_5.addWidget(self.TextoBinary, 4, 1, 1, 1)
        self.Tabular_Co = QtWidgets.QRadioButton(self.frame_3)
        self.Tabular_Co.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Tabular_Co.setObjectName("Tabular_Co")
        self.gridLayout_5.addWidget(self.Tabular_Co, 2, 3, 1, 1)
        self.XML = QtWidgets.QRadioButton(self.frame_3)
        self.XML.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.XML.setObjectName("XML")
        self.gridLayout_5.addWidget(self.XML, 3, 2, 1, 1)
        self.Pairwise = QtWidgets.QRadioButton(self.frame_3)
        self.Pairwise.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Pairwise.setObjectName("Pairwise")
        self.gridLayout_5.addWidget(self.Pairwise, 1, 3, 1, 1)
        self.Tabular = QtWidgets.QRadioButton(self.frame_3)
        self.Tabular.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Tabular.setChecked(True)
        self.Tabular.setObjectName("Tabular")
        self.gridLayout_5.addWidget(self.Tabular, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 3, 1, 1, 2)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.GAP = QtWidgets.QLabel(self.frame)
        self.GAP.setObjectName("GAP")
        self.verticalLayout_2.addWidget(self.GAP)
        self.MATCH = QtWidgets.QLabel(self.frame)
        self.MATCH.setObjectName("MATCH")
        self.verticalLayout_2.addWidget(self.MATCH)
        self.MISMATCH = QtWidgets.QLabel(self.frame)
        self.MISMATCH.setObjectName("MISMATCH")
        self.verticalLayout_2.addWidget(self.MISMATCH)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LineGAP = QtWidgets.QLineEdit(self.frame)
        self.LineGAP.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LineGAP.setAlignment(QtCore.Qt.AlignCenter)
        self.LineGAP.setText("2")
        self.LineGAP.setClearButtonEnabled(True)
        self.LineGAP.setObjectName("LineGAP")
        self.verticalLayout.addWidget(self.LineGAP)
        self.LineMATCH = QtWidgets.QLineEdit(self.frame)
        self.LineMATCH.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LineMATCH.setAlignment(QtCore.Qt.AlignCenter)
        self.LineMATCH.setText("2")
        self.LineMATCH.setClearButtonEnabled(True)
        self.LineMATCH.setObjectName("LineMATCH")
        self.verticalLayout.addWidget(self.LineMATCH)
        self.LineMISMATCH = QtWidgets.QLineEdit(self.frame)
        self.LineMISMATCH.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LineMISMATCH.setAlignment(QtCore.Qt.AlignCenter)
        self.LineMISMATCH.setText("-3")
        self.LineMISMATCH.setClearButtonEnabled(True)
        self.LineMISMATCH.setObjectName("LineMISMATCH")
        self.verticalLayout.addWidget(self.LineMISMATCH)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.Parametros = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Parametros.sizePolicy().hasHeightForWidth())
        self.Parametros.setSizePolicy(sizePolicy)
        self.Parametros.setObjectName("Parametros")
        self.gridLayout_3.addWidget(self.Parametros, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)
        self.Voltar_Prin = QtWidgets.QPushButton(self.centralwidget)
        self.Voltar_Prin.setObjectName("Voltar_Prin")
        self.gridLayout.addWidget(self.Voltar_Prin, 1, 0, 1, 1)
        self.Alinhar = QtWidgets.QPushButton(self.centralwidget)
        self.Alinhar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Alinhar.setObjectName("Alinhar")
        self.gridLayout.addWidget(self.Alinhar, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Query = None
        self.Subject = None

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.ButtonQuery.clicked.connect(self.primeiroArquivo)
        self.ButtonSubject.clicked.connect(self.segundoArquivo)

    def ChecagemCheckBox(self):
        '''

            Função que faz a checagem dos checkBox da pagina. Tem como funcionalidade
            indicar ao programa qual tipo de arquivo final o usuario deseja.

        '''
        if (self.Tabular.isChecked()):
            self.Estilo = " -outfmt 6"
        elif (self.Pairwise.isChecked()):
            self.Estilo = " -outfmt 0"
        elif (self.ShowingIdentities.isChecked()):
            self.Estilo = " -outfmt 1"
        elif (self.NoIdentities.isChecked()):
            self.Estilo = " -outfmt 2"
        elif (self.FLATIdentities.isChecked()):
            self.Estilo = " -outfmt 3"
        elif (self.FLATnoIdentities.isChecked()):
            self.Estilo = " -outfmt 4"
        elif (self.XML.isChecked()):
            self.Estilo = " -outfmt 5"
        elif (self.Tabular_Co.isChecked()):
            self.Estilo = " -outfmt 7"
        elif (self.ASN1.isChecked()):
            self.Estilo = " -outfmt 8"
        elif (self.TextoBinary.isChecked()):
            self.Estilo = " -outfmt 9"
        elif (self.Comma.isChecked()):
            self.Estilo = " -outfmt 10"
        elif (self.BLAST_Format.isChecked()):
            self.Estilo = " -outfmt 11"
        else:
            self.Estilo = " "


    def primeiroArquivo(self):
        '''

            A função tem como funcionalidade:
                -> Inserir, na variavel "self.Query", o caminho no qual o Arquivo 01
                está na maquina do usuario.
                -> E adicionar na tela inicial do BLAST o nome do arquivo e o nome do
                genoma inserido.

        '''
        Filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "SELECIONE O ARQUIVO QUERY", "", "Arquivo de Fasta (*.fasta *.fa)")
        if Filename:
            Name = []
            self.Query = Filename
            Name = Filename.split("/")
            self.NomeArquivoQUERY.setText(Name[-1])
            self.CabecalhoArquivoQUERY.setText(self.primeiraLinha(Filename))

    def segundoArquivo(self):
        '''

            A função tem como funcionalidade:
                -> Inserir, na variavel "self.Subject", o caminho no qual o Arquivo 02
                está na maquina do usuario.
                -> E adicionar na tela inicial do BLAST o nome do arquivo e o nome do
                genoma inserido.

        '''
        Filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "SELECIONE O ARQUIVO SUBJECT", "", "Arquivo de Fasta (*.fasta *.fa)")
        if Filename:
            Name = []
            self.Subject = Filename
            Name = Filename.split("/")
            self.NomeArquivoSUBJECT.setText(Name[-1])
            self.CabecalhoArquivoSUBJECT.setText(self.primeiraLinha(Filename))

    def primeiraLinha(self, Arquivo):
        '''

            Tem como funcionalidade retornar o nome do genoma prescrito no arquivo
            inserido pelo usuario.
                Obs. O nome do genoma fica na primeira linha do mapeamento.

            Parametro:
                    Arquivo (str): Uma string que contém o endereço do arquivo.

            Retorno:
                    lines (str): Uma string com o nome do genoma mapeado no arquivo.

        '''
        f = open(Arquivo, 'r')
        lines = f.readlines(1)
        lines = lines.pop(0)
        f.close()
        return lines

    def func_Paramentros(self):
        '''

            Tem como funcionalidade, guardar os valores atribuidos para o GAP,
            MATCH e MISMATCH.

        '''
        self.penalty = (" -penalty " + self.LineMISMATCH.text())
        self.reward = (" -reward "+ self.LineMATCH.text())

    def Alinhamento(self):
        '''

            Função principal do BLAST. Nela está todas as informações inseridas
            pelo usuario.
            O resumo desta função está na função "os.system" que faz o sistema
            rodar o BLASTN usando comandos do terminal para rodar o que o usuario informou.
            Também contém diversas condições para que não exista falta de informações.

            Retorno:
                    (Bool): O retorno booleano serve para notificar o erro para o software
                    e assim não dar continuidade.

            --> Função usada no GeMapCom.py

        '''
        if (self.Query != None and len(self.Query) > 0) and (self.Subject != None and len(self.Subject) > 0):       #Caso não tenha os dois arquivos inseridos, o software não ira alinhar os mapeamentos.
            self.func_Paramentros()
            self.ChecagemCheckBox()
            os.system("blastn -query " + self.Query + " -subject " + self.Subject + self.Estilo + self.penalty + self.reward + " -out ResultAlin.out")
            QtWidgets.QMessageBox.about(None, "Alinhamento", "Sucesso: Alinhado com SUCESSO!!")
            if (self.Estilo == " -outfmt 9"):                                                                       #Quando o tipo de saida for binario, não irá para a tela de resultados, pois não tem metodos de visualizações ainda. O programa só ira alinhar e disponibilizar o arquivo.
                QtWidgets.QMessageBox.about(None, "Alinhamento", "Sem Opção de Visualização: Arquivo Binario")
                return None
            return True
        else:
            QtWidgets.QMessageBox.about(None, "Alinhamento", "Error: Arquivo não INSERIDO!!")
            return None

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BLAST - Basic Local Alignment Search Tool"))
        self.label_3.setText(_translate("MainWindow", "BLAST"))
        self.ButtonQuery.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.ButtonQuery.setText(_translate("MainWindow", "Selecione o Query"))
        self.ButtonSubject.setText(_translate("MainWindow", "Selecione o(s) Subject"))
        self.BLAST_Format.setText(_translate("MainWindow", "BLAST archive format (ASN.1)"))
        self.FLATIdentities.setText(_translate("MainWindow", "Flat - Showing Identities"))
        self.Comma.setText(_translate("MainWindow", "Comma-separated Values"))
        self.Tabular.setText(_translate("MainWindow", "Tabular"))
        self.Pairwise.setText(_translate("MainWindow", "Pairwise"))
        self.ShowingIdentities.setText(_translate("MainWindow", "Showing Identities"))
        self.NoIdentities.setText(_translate("MainWindow", "No Identities"))
        self.TextoBinary.setText(_translate("MainWindow", "Texto Binary ASN.1"))
        self.XML.setText(_translate("MainWindow", "Saida XML"))
        self.Tabular_Co.setText(_translate("MainWindow", "Tabular - Comentado"))
        self.ASN1.setText(_translate("MainWindow", "Texto ASN.1"))
        self.FLATnoIdentities.setText(_translate("MainWindow", "Flat - No Identities"))
        self.SalvarComo.setText(_translate("MainWindow", "Salvar como..."))
        self.GAP.setText(_translate("MainWindow", "GAP:"))
        self.MATCH.setText(_translate("MainWindow", "MATCH:"))
        self.MISMATCH.setText(_translate("MainWindow", "MISMATCH:"))
        self.Parametros.setText(_translate("MainWindow", "Parâmetros:"))
        self.Voltar_Prin.setText(_translate("MainWindow", "Voltar"))
        self.Alinhar.setText(_translate("MainWindow", "Alinhar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_tela_BLAST()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
