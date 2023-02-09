import os

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 821, 479))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setFrameShadow(QFrame.Sunken)
        self.label_3.setLineWidth(3)
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 3)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line = QFrame(self.frame_2)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 2, 0, 1, 2)
        self.ButtonQuery = QPushButton(self.frame_2)
        self.ButtonQuery.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonQuery.setObjectName("ButtonQuery")
        self.gridLayout_4.addWidget(self.ButtonQuery, 0, 1, 2, 1)
        self.ButtonSubject = QPushButton(self.frame_2)
        self.ButtonSubject.setCursor(QCursor(Qt.PointingHandCursor))
        self.ButtonSubject.setObjectName("ButtonSubject")
        self.gridLayout_4.addWidget(self.ButtonSubject, 4, 1, 2, 1)
        self.NomeArquivoSUBJECT = QLineEdit(self.frame_2)
        self.NomeArquivoSUBJECT.setCursor(QCursor(Qt.ArrowCursor))
        self.NomeArquivoSUBJECT.setReadOnly(True)
        self.NomeArquivoSUBJECT.setObjectName("NomeArquivoSUBJECT")
        self.gridLayout_4.addWidget(self.NomeArquivoSUBJECT, 4, 0, 1, 1)
        self.CabecalhoArquivoSUBJECT = QLineEdit(self.frame_2)
        self.CabecalhoArquivoSUBJECT.setCursor(QCursor(Qt.ArrowCursor))
        self.CabecalhoArquivoSUBJECT.setReadOnly(True)
        self.CabecalhoArquivoSUBJECT.setObjectName("CabecalhoArquivoSUBJECT")
        self.gridLayout_4.addWidget(self.CabecalhoArquivoSUBJECT, 5, 0, 1, 1)
        self.NomeArquivoQUERY = QLineEdit(self.frame_2)
        self.NomeArquivoQUERY.setCursor(QCursor(Qt.ArrowCursor))
        self.NomeArquivoQUERY.setReadOnly(True)
        self.NomeArquivoQUERY.setObjectName("NomeArquivoQUERY")
        self.gridLayout_4.addWidget(self.NomeArquivoQUERY, 0, 0, 1, 1)
        self.CabecalhoArquivoQUERY = QLineEdit(self.frame_2)
        self.CabecalhoArquivoQUERY.setCursor(QCursor(Qt.ArrowCursor))
        self.CabecalhoArquivoQUERY.setReadOnly(True)
        self.CabecalhoArquivoQUERY.setObjectName("CabecalhoArquivoQUERY")
        self.gridLayout_4.addWidget(self.CabecalhoArquivoQUERY, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 3)
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.SalvarComo = QLabel(self.frame_3)
        self.SalvarComo.setObjectName("SalvarComo")
        self.gridLayout_5.addWidget(self.SalvarComo, 0, 1, 1, 1)
        self.ASN1 = QRadioButton(self.frame_3)
        self.ASN1.setCursor(QCursor(Qt.PointingHandCursor))
        self.ASN1.setObjectName("ASN1")
        self.gridLayout_5.addWidget(self.ASN1, 3, 3, 1, 1)
        self.BLAST_Format = QRadioButton(self.frame_3)
        self.BLAST_Format.setObjectName("BLAST_Format")
        self.gridLayout_5.addWidget(self.BLAST_Format, 4, 3, 1, 1)
        self.Comma = QRadioButton(self.frame_3)
        self.Comma.setObjectName("Comma")
        self.gridLayout_5.addWidget(self.Comma, 4, 2, 1, 1)
        self.FLATIdentities = QRadioButton(self.frame_3)
        self.FLATIdentities.setCursor(QCursor(Qt.PointingHandCursor))
        self.FLATIdentities.setObjectName("FLATIdentities")
        self.gridLayout_5.addWidget(self.FLATIdentities, 1, 2, 1, 1)
        self.FLATnoIdentities = QRadioButton(self.frame_3)
        self.FLATnoIdentities.setCursor(QCursor(Qt.PointingHandCursor))
        self.FLATnoIdentities.setObjectName("FLATnoIdentities")
        self.gridLayout_5.addWidget(self.FLATnoIdentities, 2, 2, 1, 1)
        self.NoIdentities = QRadioButton(self.frame_3)
        self.NoIdentities.setCursor(QCursor(Qt.PointingHandCursor))
        self.NoIdentities.setObjectName("NoIdentities")
        self.gridLayout_5.addWidget(self.NoIdentities, 3, 1, 1, 1)
        self.ShowingIdentities = QRadioButton(self.frame_3)
        self.ShowingIdentities.setCursor(QCursor(Qt.PointingHandCursor))
        self.ShowingIdentities.setObjectName("ShowingIdentities")
        self.gridLayout_5.addWidget(self.ShowingIdentities, 2, 1, 1, 1)
        self.TextoBinary = QRadioButton(self.frame_3)
        self.TextoBinary.setCursor(QCursor(Qt.PointingHandCursor))
        self.TextoBinary.setObjectName("TextoBinary")
        self.gridLayout_5.addWidget(self.TextoBinary, 4, 1, 1, 1)
        self.Tabular_Co = QRadioButton(self.frame_3)
        self.Tabular_Co.setCursor(QCursor(Qt.PointingHandCursor))
        self.Tabular_Co.setObjectName("Tabular_Co")
        self.gridLayout_5.addWidget(self.Tabular_Co, 2, 3, 1, 1)
        self.XML = QRadioButton(self.frame_3)
        self.XML.setCursor(QCursor(Qt.PointingHandCursor))
        self.XML.setObjectName("XML")
        self.gridLayout_5.addWidget(self.XML, 3, 2, 1, 1)
        self.Pairwise = QRadioButton(self.frame_3)
        self.Pairwise.setCursor(QCursor(Qt.PointingHandCursor))
        self.Pairwise.setObjectName("Pairwise")
        self.gridLayout_5.addWidget(self.Pairwise, 1, 3, 1, 1)
        self.Tabular = QRadioButton(self.frame_3)
        self.Tabular.setCursor(QCursor(Qt.PointingHandCursor))
        self.Tabular.setChecked(True)
        self.Tabular.setObjectName("Tabular")
        self.gridLayout_5.addWidget(self.Tabular, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_3, 3, 1, 1, 2)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.GAP = QLabel(self.frame)
        self.GAP.setObjectName("GAP")
        self.verticalLayout_2.addWidget(self.GAP)
        self.MATCH = QLabel(self.frame)
        self.MATCH.setObjectName("MATCH")
        self.verticalLayout_2.addWidget(self.MATCH)
        self.MISMATCH = QLabel(self.frame)
        self.MISMATCH.setObjectName("MISMATCH")
        self.verticalLayout_2.addWidget(self.MISMATCH)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LineGAP = QLineEdit(self.frame)
        self.LineGAP.setLayoutDirection(Qt.LeftToRight)
        self.LineGAP.setAlignment(Qt.AlignCenter)
        self.LineGAP.setText("2")
        self.LineGAP.setClearButtonEnabled(True)
        self.LineGAP.setObjectName("LineGAP")
        self.verticalLayout.addWidget(self.LineGAP)
        self.LineMATCH = QLineEdit(self.frame)
        self.LineMATCH.setLayoutDirection(Qt.LeftToRight)
        self.LineMATCH.setAlignment(Qt.AlignCenter)
        self.LineMATCH.setText("2")
        self.LineMATCH.setClearButtonEnabled(True)
        self.LineMATCH.setObjectName("LineMATCH")
        self.verticalLayout.addWidget(self.LineMATCH)
        self.LineMISMATCH = QLineEdit(self.frame)
        self.LineMISMATCH.setLayoutDirection(Qt.LeftToRight)
        self.LineMISMATCH.setAlignment(Qt.AlignCenter)
        self.LineMISMATCH.setText("-3")
        self.LineMISMATCH.setClearButtonEnabled(True)
        self.LineMISMATCH.setObjectName("LineMISMATCH")
        self.verticalLayout.addWidget(self.LineMISMATCH)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.Parametros = QLabel(self.frame)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.Parametros.sizePolicy().hasHeightForWidth())
        self.Parametros.setSizePolicy(sizePolicy)
        self.Parametros.setObjectName("Parametros")
        self.gridLayout_3.addWidget(self.Parametros, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 3, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)
        self.Voltar_Prin = QPushButton(self.centralwidget)
        self.Voltar_Prin.setObjectName("Voltar_Prin")
        self.gridLayout.addWidget(self.Voltar_Prin, 1, 0, 1, 1)
        self.Alinhar = QPushButton(self.centralwidget)
        self.Alinhar.setCursor(QCursor(Qt.PointingHandCursor))
        self.Alinhar.setObjectName("Alinhar")
        self.gridLayout.addWidget(self.Alinhar, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.Query = None
        self.Subject = None

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

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
        Filename, _ = QFileDialog.getOpenFileName(None, "SELECIONE O ARQUIVO QUERY", "", "Arquivo de Fasta (*.fasta *.fa)")
        # Filename = "/home/pedroazevedo141/repositories/GeMapCom/Primeiro_Uso/seq1.fasta"
        # Filename = "/home/pedroazevedo141/repositories/GeMapCom/Primeiro_Uso/Yersinia-BLAST.fasta"
        if Filename:
            Name = []
            self.Query = Filename
            Name = Filename.split("/")
            self.NomeArquivoQUERY.setText(Name[-1])
            self.CabecalhoArquivoQUERY.setText(
                self.primeiraLinha(Filename)[1:])

    def segundoArquivo(self):
        '''

            A função tem como funcionalidade:
                -> Inserir, na variavel "self.Subject", o caminho no qual o Arquivo 02
                está na maquina do usuario.
                -> E adicionar na tela inicial do BLAST o nome do arquivo e o nome do
                genoma inserido.

        '''
        Filename, _ = QFileDialog.getOpenFileName(None, "SELECIONE O ARQUIVO SUBJECT", "", "Arquivo de Fasta (*.fasta *.fa)")
        # Filename = "/home/pedroazevedo141/repositories/GeMapCom/Primeiro_Uso/seq2.fasta"
        # Filename = "/home/pedroazevedo141/repositories/GeMapCom/Primeiro_Uso/Xanthomonas-BLAST.fasta"
        if Filename:
            Name = []
            self.Subject = Filename
            Name = Filename.split("/")
            self.NomeArquivoSUBJECT.setText(Name[-1])
            self.CabecalhoArquivoSUBJECT.setText(
                self.primeiraLinha(Filename)[1:])

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
        self.penalty = (" -penalty " + self.LineMISMATCH.text()
                        ) if len(self.LineMISMATCH.text()) > 0 else " -penalty -3"
        self.reward = (" -reward " + self.LineMATCH.text()
                       ) if len(self.LineMATCH.text()) > 0 else " -reward 2"

    def fileEmpty(self):
        with open('ResultAlin.out', 'r') as file:
            file.seek(0, os.SEEK_END)
            isempty = file.tell() == 0
            file.seek(0)    # rebobinar o arquivo
        return isempty

    def Alinhamento(self, type):
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
        if type == "blastn":
            # Caso não tenha os dois arquivos inseridos, o software não ira alinhar os mapeamentos.
            if (self.Query != None and len(self.Query) > 0) and (self.Subject != None and len(self.Subject) > 0):
                self.func_Paramentros()
                self.ChecagemCheckBox()
                exit_result = os.system(type + " -query " + self.Query + " -subject " +
                                        self.Subject + self.Estilo + self.penalty + self.reward + " -out ResultAlin.out")
                if exit_result == 0:
                    if (self.fileEmpty()):
                        QMessageBox.about(
                            None, "Alinhamento", "Error: Sem resultado, verifique os parametros!!")
                        return None
                    else:
                        QMessageBox.about(None, "Alinhamento",
                                          "Sucesso: Alinhado com SUCESSO!!")
                        # Quando o tipo de saida for binario, não irá para a tela de resultados, pois não tem metodos de visualizações ainda. O programa só ira alinhar e disponibilizar o arquivo.
                        if (self.Estilo == " -outfmt 9"):
                            QMessageBox.about(
                                None, "Alinhamento", "Sem Opção de Visualização: Arquivo Binario")
                            return None
                        return True
                elif exit_result == 1:
                    QMessageBox.about(None, "Resultado do Alinhamento",
                                      "Error: Error in query sequence(s) or BLAST options!!")
                elif exit_result == 2:
                    QMessageBox.about(
                        None, "Resultado do Alinhamento", "Error: Error in BLAST database!!")
                elif exit_result == 3:
                    QMessageBox.about(
                        None, "Resultado do Alinhamento", "Error: Error in BLAST engine!!")
                elif exit_result == 4:
                    QMessageBox.about(
                        None, "Resultado do Alinhamento", "Error: Out of memory!!")
                elif exit_result == 5:
                    QMessageBox.about(None, "Resultado do Alinhamento",
                                      "Error: Network error connecting to NCBI to fetch sequence data!!")
                elif exit_result == 6:
                    QMessageBox.about(
                        None, "Resultado do Alinhamento", "Error: Error creating output files!!")
                else:
                    QMessageBox.about(
                        None, "Resultado do Alinhamento", "Error: Unknown error!!")
            else:
                QMessageBox.about(None, "Alinhamento",
                                  "Error: Arquivo não INSERIDO!!")
                return None
        else:
            # Caso não tenha os dois arquivos inseridos, o software não ira alinhar os mapeamentos.
            if (self.Query != None and len(self.Query) > 0) and (self.Subject != None and len(self.Subject) > 0):
                exit_result = os.system(
                    type + " -query " + self.Query + " -subject " + self.Subject + " -out ResultAlin.out")
                if exit_result == 0:
                    QMessageBox.about(None, "Alinhamento",
                                      "Sucesso: Alinhado com SUCESSO!!")
                    return True
                elif exit_result == 1:
                    QMessageBox.about(None, "Resultado do Alinhamento",
                                      "Error: Error in query sequence(s) or BLAST options!!")
                elif exit_result == 2:
                    QMessageBox.about(
                        None, "Resultado do Alinhamento", "Error: Error in BLAST database!!")
                elif exit_result == 3:
                    QMessageBox.about(
                        None, "Resultado do Alinhamento", "Error: Error in BLAST engine!!")
                elif exit_result == 4:
                    QMessageBox.about(
                        None, "Resultado do Alinhamento", "Error: Out of memory!!")
                elif exit_result == 5:
                    QMessageBox.about(None, "Resultado do Alinhamento",
                                      "Error: Network error connecting to NCBI to fetch sequence data!!")
                elif exit_result == 6:
                    QMessageBox.about(
                        None, "Resultado do Alinhamento", "Error: Error creating output files!!")
                else:
                    QMessageBox.about(
                        None, "Resultado do Alinhamento", "Error: Unknown error!!")
            else:
                QMessageBox.about(None, "Alinhamento",
                                  "Error: Arquivo não INSERIDO!!")
                return None

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "BLAST - Basic Local Alignment Search Tool"))
        self.label_3.setText(_translate("MainWindow", "BLAST"))
        self.ButtonQuery.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.ButtonQuery.setText(_translate("MainWindow", "Selecione o Query"))
        self.ButtonSubject.setText(_translate(
            "MainWindow", "Selecione o(s) Subject"))
        self.BLAST_Format.setText(_translate(
            "MainWindow", "BLAST archive format (ASN.1)"))
        self.FLATIdentities.setText(_translate(
            "MainWindow", "Flat - Showing Identities"))
        self.Comma.setText(_translate("MainWindow", "Comma-separated Values"))
        self.Tabular.setText(_translate("MainWindow", "Tabular"))
        self.Pairwise.setText(_translate("MainWindow", "Pairwise"))
        self.ShowingIdentities.setText(
            _translate("MainWindow", "Showing Identities"))
        self.NoIdentities.setText(_translate("MainWindow", "No Identities"))
        self.TextoBinary.setText(_translate(
            "MainWindow", "Texto Binary ASN.1"))
        self.XML.setText(_translate("MainWindow", "Saida XML"))
        self.Tabular_Co.setText(_translate(
            "MainWindow", "Tabular - Comentado"))
        self.ASN1.setText(_translate("MainWindow", "Texto ASN.1"))
        self.FLATnoIdentities.setText(_translate(
            "MainWindow", "Flat - No Identities"))
        self.SalvarComo.setText(_translate("MainWindow", "Salvar como..."))
        self.GAP.setText(_translate("MainWindow", "GAP:"))
        self.MATCH.setText(_translate("MainWindow", "MATCH:"))
        self.MISMATCH.setText(_translate("MainWindow", "MISMATCH:"))
        self.Parametros.setText(_translate("MainWindow", "Parâmetros:"))
        self.Voltar_Prin.setText(_translate("MainWindow", "Voltar"))
        self.Alinhar.setText(_translate("MainWindow", "Alinhar"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_tela_BLAST()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
