import os

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from src.blast.qDialogAlinhamento import EmployeeDlg

class funcBlast():
    
    def initScreens(self, homeScreen) -> None:
        self.Query = None
        self.Subject = None
        self.homeScreen = homeScreen
        self.screenBlast = homeScreen.tela_blast_1
        self.QtStack = homeScreen.QtStack
        self.screenBlast.ButtonQuery.clicked.connect(self.primeiroArquivo)
        self.screenBlast.ButtonSubject.clicked.connect(self.segundoArquivo)
        self.screenBlast.Alinhar.clicked.connect(self.alingCheck)
        
    def alingCheck(self):
        if self.Query != None:
            if self.Subject != None:
                self.launchPopup()
            else:
                QMessageBox.about(None, "BLAST",
                                  "Informe o Subject para prosseguir com o alinhamento.")
        else:
            QMessageBox.about(None, "BLAST",
                              "Informe o Query para prosseguir com o alinhamento.")
        
    def ChecagemCheckBox(self):
        '''

            Função que faz a checagem dos checkBox da pagina. Tem como funcionalidade
            indicar ao programa qual tipo de arquivo final o usuario deseja.

        '''
        if (self.screenBlast.Tabular.isChecked()):
            self.Estilo = " -outfmt 6"
        elif (self.screenBlast.Pairwise.isChecked()):
            self.Estilo = " -outfmt 0"
        elif (self.screenBlast.ShowingIdentities.isChecked()):
            self.Estilo = " -outfmt 1"
        elif (self.screenBlast.NoIdentities.isChecked()):
            self.Estilo = " -outfmt 2"
        elif (self.screenBlast.FLATIdentities.isChecked()):
            self.Estilo = " -outfmt 3"
        elif (self.screenBlast.FLATnoIdentities.isChecked()):
            self.Estilo = " -outfmt 4"
        elif (self.screenBlast.XML.isChecked()):
            self.Estilo = " -outfmt 5"
        elif (self.screenBlast.Tabular_Co.isChecked()):
            self.Estilo = " -outfmt 7"
        elif (self.screenBlast.ASN1.isChecked()):
            self.Estilo = " -outfmt 8"
        elif (self.screenBlast.TextoBinary.isChecked()):
            self.Estilo = " -outfmt 9"
        elif (self.screenBlast.Comma.isChecked()):
            self.Estilo = " -outfmt 10"
        elif (self.screenBlast.BLAST_Format.isChecked()):
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
        # Filename, _ = QFileDialog.getOpenFileName(None, "SELECIONE O ARQUIVO QUERY", "", "Arquivo de Fasta (*.fasta *.fa)")
        # Filename = "/home/pedroazevedo141/repositories/GeMapCom/Primeiro_Uso/seq1.fasta"
        Filename = "/home/pedroazevedo141/repositories/GeMapCom/Primeiro_Uso/Yersinia-BLAST.fasta"
        if Filename:
            Name = []
            self.Query = Filename
            Name = Filename.split("/")
            self.screenBlast.NomeArquivoQUERY.setText(Name[-1])
            self.screenBlast.CabecalhoArquivoQUERY.setText(
                self.primeiraLinha(Filename)[1:])

    def segundoArquivo(self):
        '''

            A função tem como funcionalidade:
                -> Inserir, na variavel "self.Subject", o caminho no qual o Arquivo 02
                está na maquina do usuario.
                -> E adicionar na tela inicial do BLAST o nome do arquivo e o nome do
                genoma inserido.

        '''
        # Filename, _ = QFileDialog.getOpenFileName(None, "SELECIONE O ARQUIVO SUBJECT", "", "Arquivo de Fasta (*.fasta *.fa)")
        # Filename = "/home/pedroazevedo141/repositories/GeMapCom/Primeiro_Uso/seq2.fasta"
        Filename = "/home/pedroazevedo141/repositories/GeMapCom/Primeiro_Uso/Xanthomonas-BLAST.fasta"
        if Filename:
            Name = []
            self.Subject = Filename
            Name = Filename.split("/")
            self.screenBlast.NomeArquivoSUBJECT.setText(Name[-1])
            self.screenBlast.CabecalhoArquivoSUBJECT.setText(
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
        self.penalty = (" -penalty " + self.screenBlast.LineMISMATCH.text()
                        ) if len(self.screenBlast.LineMISMATCH.text()) > 0 else " -penalty -3"
        self.reward = (" -reward " + self.screenBlast.LineMATCH.text()
                       ) if len(self.screenBlast.LineMATCH.text()) > 0 else " -reward 2"

    def fileEmpty(self):
        with open('ResultAlin.out', 'r') as file:
            file.seek(0, os.SEEK_END)
            isempty = file.tell() == 0
            file.seek(0)    # rebobinar o arquivo
        return isempty
    
    def launchPopup(self):
        self.type_blast = None
        GUI = EmployeeDlg(self)
        if (GUI.exec()):
            self.tela_Filtro_Ali()
            
    def tabularCheck(self):
        if (self.screenBlast.Tabular.isChecked() and self.type_blast == "blastn"):
            return True
        return False
            
    def tela_Filtro_Ali(self):
        """

            Função para entrar na tela de FILTROS do BLAST, utilizando o botão
            "Alinhar" da tela inicial do BLAST.

        """
        self.Result = self.Alinhamento(type=self.type_blast)
        if self.Result != None:  # Dependendo do resultado retornado pela função "Alinhamento", presente no arquivo tela_BLAST.py, o software irá trocar de tela indo para tela de filtros ou para tela de resultado caso seja None o resultado a tela inicial irá permanecer.
            # Se o usuario escolher que o resultado seja de forma Tabular, a proxima tela será a dos FILTROS.
            if (self.tabularCheck()):
                self.homeScreen.tela_resultado_blast.resultadoFiltragem()
                self.QtStack.setCurrentIndex(6)
            else:  # Se não for Tabular, a proxima tela será a de RESULTADOS.
                self.homeScreen.tela_resultado_blast.resultadoAlinhamento()
                self.QtStack.setCurrentIndex(5)

    def apagarValoresTelaBlast(self):
        """

            Função para apagar os valores da tela INICIAL do BLAST.

        """
        self.screenBlast.LineGAP.setText("2")
        self.screenBlast.LineMATCH.setText("2")
        self.screenBlast.LineMISMATCH.setText("-3")
        self.screenBlast.NomeArquivoQUERY.clear()
        self.screenBlast.CabecalhoArquivoQUERY.clear()
        self.screenBlast.NomeArquivoSUBJECT.clear()
        self.screenBlast.CabecalhoArquivoSUBJECT.clear()
        self.screenBlast.Query = ''
        self.screenBlast.Subject = ''

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
