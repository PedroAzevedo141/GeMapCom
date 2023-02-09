import os
import sys

from PyQt5.QtCore import QCoreApplication

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Bio import SeqIO

from Plotar.main import criar_imagem

from src.blast import funcBlast as blast
from src.blast.result import resultBlast
from src.blast.filtros import filtrosBlast

from Telas.tela_BLAST import Ui_tela_BLAST
from Telas.tela_principal import Ui_Tela_Principal
from Telas.tela_converter import Ui_Tela_Converter
from Telas.tela_resultado import Ui_Tela_Resultado
from Telas.tela_comparacao import Ui_Tela_Comparacao
from Telas.tela_filtros_BLAST import Ui_tela_Filtros_BLAST
from Telas.tela_resultado_BLAST import Ui_tela_Resultado_BLAST
from Telas.qDialogBlast import Ui_Dialog_Custom

from Algoritmos.algorithm_smith_waterman import algorithm_smith
from Algoritmos.algorithm_needleman_wunsch import algorithm_needleman


class Ui_Main(QWidget):
    """

    Classe que contem todas as configurações da tela inicial da ferramenta.

    Nessa classe usa-se propriedades da biblioteca PyQt5 para facilitar o
    gerenciamento das configurações e interações da tela em questão.

    """

    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(1276, 585)
        Main.setFixedSize(1276, 585)

        self.QtStack = QStackedLayout()

        self.stack0 = QMainWindow()
        self.stack1 = QMainWindow()
        self.stack2 = QMainWindow()
        self.stack3 = QMainWindow()
        self.stack4 = QMainWindow()
        self.stack5 = QMainWindow()
        self.stack6 = QMainWindow()

        self.tela_principal = Ui_Tela_Principal()
        self.tela_principal.setupUi(self.stack0)

        self.tela_comparacao = Ui_Tela_Comparacao()
        self.tela_comparacao.setupUi(self.stack1)

        self.tela_converter = Ui_Tela_Converter()
        self.tela_converter.setupUi(self.stack2)

        self.tela_resultado = Ui_Tela_Resultado()
        self.tela_resultado.setupUi(self.stack3)

        self.tela_blast_1 = Ui_tela_BLAST()
        self.tela_blast_1.setupUi(self.stack4)

        self.tela_resultado_blast_1 = Ui_tela_Resultado_BLAST()
        self.tela_resultado_blast_1.setupUi(self.stack5)

        self.tela_filtros_blast_1 = Ui_tela_Filtros_BLAST()
        self.tela_filtros_blast_1.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        
        self.tela_blast = blast()
        self.tela_resultado_blast = resultBlast()
        self.tela_filtros_blast = filtrosBlast()
        
        self.tela_blast.initScreens(self)
        self.tela_resultado_blast.initScreens(self)
        self.tela_filtros_blast.initScreens(self)

class Main(QMainWindow, Ui_Main):
    """

    Classe que contem todas as funcionalidades da tela inicial da ferramenta.

    """

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.seq1 = ''  # sequencia 1 data 1
        self.data1 = ''

        self.seq2 = ''  # sequencia 2 data 2
        self.data2 = ''

        self.gefasta = ''
        self.gefasta_salvar = ''

        self.fqfasta = ''
        self.fqfasta_salvar = ''

        self.resultado = ''
        self.resultado_salvar = ''
        self.lista_salvar_resultado = []

        self.algo_needle = algorithm_needleman('', '', None, None, None)

        self.algo_water = algorithm_smith('', '', None, None, None)

        self.create_image = criar_imagem('', '', '', '', None, None)

        self.lista_converter1 = []
        self.seq_converter1 = ''
        self.string_converter1 = ''
        self.string_convertida1 = ''

        self.lista_converter2 = []
        self.seq_converter1 = ''
        self.string_converter2 = ''
        self.string_convertida2 = ''

        # Funções dos botões da tela principal.
        self.tela_principal.botao_sair.clicked.connect(self.fecharAplicacao)
        self.tela_principal.botao_tela_outras.clicked.connect(
            self.tela_filtros_blast.abrirTelaBlast)
        self.tela_principal.botao_tela_converter.clicked.connect(
            self.abrirTelaConverter)
        self.tela_principal.botao_tela_comparacao.clicked.connect(
            self.abrirTelaComparacao)

        # Funções dos botões da tela comparação.
        self.tela_comparacao.botao_voltar.clicked.connect(
            self.voltarTelaPrincipal)
        self.tela_comparacao.botao_abrir_arquivo1.clicked.connect(
            self.abrirArquivo1)
        self.tela_comparacao.botao_abrir_arquivo2.clicked.connect(
            self.abrirArquivo2)
        self.tela_comparacao.botao_realizar_comparacao.clicked.connect(
            self.comparacao)

        # Funções dos botões da tela converter.
        self.tela_converter.botao_converter.clicked.connect(self.converter)
        self.tela_converter.botao_voltar.clicked.connect(
            self.voltarTelaPrincipal)
        self.tela_converter.botao_abrir_arquivo.clicked.connect(
            self.abrirArquivoConverter)

        # Funções dos botões da tela resultado.
        self.tela_resultado.bota_gerar_imagem.clicked.connect(self.salvarImgem)
        self.tela_resultado.botao_salvar.clicked.connect(
            self.salvarResultadoTxt)
        self.tela_resultado.botao_voltar.clicked.connect(
            self.abrirTelaComparacao)

        # Funções dos botões da tela do BLAST.
        self.Result = None
        self.CaminhoDiretorio = os.path.dirname(os.path.realpath(__file__))
        self.tela_blast_1.Voltar_Prin.clicked.connect(self.voltarTelaPrincipal)
        
        self.tela_filtros_blast.CaminhoDiretorio_funcao(self.CaminhoDiretorio)

    def apagarValoresTelaComparacao(self):
        """

            Função para apagar os valores da tela comparação.

        """
        self.tela_comparacao.setar_sequencia1.setText('')
        self.tela_comparacao.setar_sequencia2.setText('')
        self.tela_comparacao.match.setText('')
        self.tela_comparacao.mismatch.setText('')
        self.tela_comparacao.gap.setText('')

        self.tela_resultado.setar_resultado.setText('')

        self.resultado = ''
        self.resultado_salvar = ''
        self.lista_salvar_resultado = []

        self.algo_needle = algorithm_needleman('', '', None, None, None)

        self.algo_water = algorithm_smith('', '', None, None, None)

        self.create_image = criar_imagem('', '', '', '', None, None)

        self.lista_converter1 = []
        self.seq_converter1 = ''
        self.string_converter1 = ''
        self.string_convertida1 = ''

        self.lista_converter2 = []
        self.seq_converter2 = ''
        self.string_converter2 = ''
        self.string_convertida2 = ''

    def apagarValoresTelaConverter(self):
        """

            Função para apagar os valores da tela converter.

        """
        self.tela_converter.setar_sequencia.setText('')

    def voltarTelaPrincipal(self):
        """

            Função para voltar à tela INICIAL.

        """
        self.apagarValoresTelaComparacao()
        self.apagarValoresTelaConverter()
        self.tela_blast.apagarValoresTelaBlast()

        self.QtStack.setCurrentIndex(0)

    def abrirTelaComparacao(self):
        """

            Função para abrir tela de comparação.

        """
        self.apagarValoresTelaComparacao()
        self.QtStack.setCurrentIndex(1)

    def abrirTelaConverter(self):
        """

            Função para abrir tela de converter.

        """
        self.QtStack.setCurrentIndex(2)

    def abrirArquivo1(self):
        """

            Função para abrir sequencia 1 e colocar na tela.

        """
        self.seq1 = QFileDialog.getOpenFileName(
            self, 'Abrir sequencia 1', "", "Fasta Files (*.fasta *.fa)")
        if self.seq1[0]:
            f = open(self.seq1[0], 'r')

            with f:
                # self.data1 = f.readline()
                self.data1 = f.read()
                self.tela_comparacao.setar_sequencia1.setText(self.data1)

    def abrirArquivo2(self):
        """

            Função para abrir sequencia 2 e colocar na tela.

        """
        self.seq2 = QFileDialog.getOpenFileName(
            self, 'Abrir sequencia 2', "", "Fasta Files (*.fasta *.fa)")
        if self.seq2[0]:
            f = open(self.seq2[0], 'r')

            with f:
                # self.data2 = f.readline()
                self.data2 = f.read()
                self.tela_comparacao.setar_sequencia2.setText(self.data2)

    def comparacao(self):
        """

            Função que realiza a comparação LOCAL e GLOBAL, submetendo os arquivos.

            -> Usada no arquivo tela_comparacao.py

        """
        match = self.tela_comparacao.match.text()
        mismatch = self.tela_comparacao.mismatch.text()
        gap = self.tela_comparacao.gap.text()

        if self.tela_comparacao.setar_sequencia1.toPlainText() == '' or self.tela_comparacao.setar_sequencia2.toPlainText() == '':
            QMessageBox.about(self, 'Atenção', 'Selecione um arquivo')

        elif not self.validarNumero(match, mismatch, gap):
            QMessageBox.about(
                self, 'Atenção', 'Preencha todos os campos somente com números!!')

        elif self.tela_comparacao.comboBox.currentText() == 'GLOBAL':
            self.comparacaoGlobal()

        else:
            self.comparacaoLocal()

    def comparacaoGlobal(self):
        """

            Função que realiza a comparação GLOBAL, utilizando o algoritmo de Needleman-Wunsch.

            -> Usada no arquivo tela_comparacao.py / algorithm_needleman_wunsch.py

        """
        with open(self.seq1[0], 'r') as fasta:
            for linha in fasta:
                if not linha.startswith('>'):
                    self.seq_converter1 += linha.strip()
            self.lista_converter1.append(self.seq_converter1)

        self.string_converter1 = (str(self.lista_converter1))
        self.string_convertida1 = self.string_converter1[2:-2]

        with open(self.seq2[0], 'r') as fasta:
            for linha in fasta:
                if not linha.startswith('>'):
                    self.seq_converter2 += linha.strip()
            self.lista_converter2.append(self.seq_converter2)

        self.string_converter2 = (str(self.lista_converter2))
        self.string_convertida2 = self.string_converter2[2:-2]

        self.algo_needle = algorithm_needleman(self.string_convertida1,
                                               self.string_convertida2,
                                               int(self.tela_comparacao.match.text()),
                                               int(self.tela_comparacao.mismatch.text()),
                                               int(self.tela_comparacao.gap.text()))

        self.algo_needle.needle()
        self.QtStack.setCurrentIndex(3)

        self.tela_resultado.setar_resultado.append('Identidade: ' + str(self.algo_needle.ident)[:5] + '\n' +
                                                   'Score: ' + str(self.algo_needle.seq_score)[:5] + '\n' +
                                                   'Sequencia 1: ' + self.algo_needle.align1 + '\n' +
                                                   'Sym:                ' + self.algo_needle.sym + '\n' +
                                                   'Sequencia 2: ' + self.algo_needle.align2)

        self.lista_salvar_resultado.append('Identidade: ' + str(self.algo_needle.ident) + '\n' +
                                           'Score: ' + str(self.algo_needle.seq_score) + '\n' +
                                           'Sequencia 1: ' + self.algo_needle.align1 + '\n' +
                                           'Sym:         ' + self.algo_needle.sym + '\n' +
                                           'Sequencia 2: ' + self.algo_needle.align2)

    def comparacaoLocal(self):
        """

            Função que realiza a comparação LOCAL, utilizando o algoritmo de Smith-Waterman.

            -> Usada no arquivo tela_comparacao.py / algorithm_smith_waterman.py

        """
        with open(self.seq1[0], 'r') as fasta:
            for linha in fasta:
                if not linha.startswith('>'):
                    self.seq_converter1 += linha.strip()
            self.lista_converter1.append(self.seq_converter1)

        self.string_converter1 = (str(self.lista_converter1))
        self.string_convertida1 = self.string_converter1[2:-2]

        with open(self.seq2[0], 'r') as fasta:
            for linha in fasta:
                if not linha.startswith('>'):
                    self.seq_converter2 += linha.strip()
            self.lista_converter2.append(self.seq_converter2)

        self.string_converter2 = (str(self.lista_converter2))
        self.string_convertida2 = self.string_converter2[2:-2]

        self.algo_water = algorithm_smith(self.string_convertida1,
                                          self.string_convertida2,
                                          int(self.tela_comparacao.match.text()),
                                          int(self.tela_comparacao.mismatch.text()),
                                          int(self.tela_comparacao.gap.text()))

        self.algo_water.water()
        self.QtStack.setCurrentIndex(3)

        self.tela_resultado.setar_resultado.append('Identidade: ' + str(self.algo_water.identity)[:5] + '\n' +
                                                   'Score: ' + str(self.algo_water.max_score) + '\n' +
                                                   'Sequencia 1: ' + self.algo_water.align1 + '\n' +
                                                   'Sym:                ' + self.algo_water.sym + '\n' +
                                                   'Sequencia 2: ' + self.algo_water.align2)

        self.lista_salvar_resultado.append('Identidade: ' + str(self.algo_water.identity)[:5] + '\n' +
                                           'Score: ' + str(self.algo_water.max_score) + '\n' +
                                           'Sequencia 1: ' + self.algo_water.align1 + '\n' +
                                           'Sym:         ' + self.algo_water.sym + '\n' +
                                           'Sequencia 2: ' + self.algo_water.align2)

    def validarNumero(self, match, mismatch, gap):
        """

        Tem como funcionalidade validar o numero o MATCH, MISMATCH e GAP. Para
        não ficar nenhum campo sem preenchimento.

        -> tela_comparacao.py

        """
        try:
            match = int(match)
            mismatch = int(mismatch)
            gap = int(gap)
            return True
        except:
            return False

    def salvarResultadoTxt(self):
        """

        Funcionalidade de impressão dos resultados como .txt.

        -> tela_resultado.py

        """
        self.resultado = QFileDialog.getSaveFileName(
            self, 'Salvar Resultado', '/home', "Text (*.txt *.asc)")

        if self.resultado[0]:
            self.resultado_salvar = open(self.resultado[0], 'w')
            with self.resultado_salvar:
                self.resultado_salvar.writelines(self.lista_salvar_resultado)
                self.resultado_salvar.close()

        QMessageBox.about(self, 'Atenção', 'Resultado Salvo')

    def salvarImgem(self):
        """

        Funcionalidade de impressão dos resultados como IMAGEM.

        -> Função da pasta plotar.

        """
        if (self.tela_comparacao.comboBox.currentText() == 'GLOBAL'):
            img, _ = QFileDialog.getSaveFileName(
                self, 'Salvar Imagem', '/home', filter="PNG(*.png);; JPEG(*.jpg)")
            self.create_image = criar_imagem(img, self.algo_needle.align1, self.algo_needle.align2, self.algo_needle.sym, str(
                self.algo_needle.ident), str(self.algo_needle.seq_score))
            if img[-3:] == "png":
                self.create_image.salvarImage()
                QMessageBox.about(self, 'Atenção', 'Imagem Salva')
            elif img[-3:] == "jpg":
                self.create_image.salvarImage()
                QMessageBox.about(self, 'Atenção', 'Imagem Salva')

        else:
            img, _ = QFileDialog.getSaveFileName(
                self, 'Salvar Imagem', '/home', filter="PNG(*.png);; JPEG(*.jpg)")
            self.create_image = criar_imagem(img, self.algo_water.align1, self.algo_water.align2, self.algo_water.sym, str(
                self.algo_water.identity), str(self.algo_water.max_score))
            if img[-3:] == "png":
                self.create_image.salvarImage()
                QMessageBox.about(self, 'Atenção', 'Imagem Salva')
            elif img[-3:] == "jpg":
                self.create_image.salvarImage()
                QMessageBox.about(self, 'Atenção', 'Imagem Salva')

    def abrirArquivoConverter(self):
        """

            Função para salvar o caminho da sequencia inserida pelo usuario na
            tela de converter (tela_converter.py).

        """
        if self.tela_converter.comboBox.currentText() == 'GENBANK - FASTA':
            self.gefasta = QFileDialog.getOpenFileName(
                self, 'Abrir sequencia', "", "Genbank Files (*.gbk)")
            if self.gefasta[0]:
                f = open(self.gefasta[0], 'r')

                with f:
                    self.datage = f.read()
                    self.tela_converter.setar_sequencia.setText(self.datage)
        else:
            self.fqfasta = QFileDialog.getOpenFileName(
                self, 'Abrir sequencia', "", "FastaQ Files (*.fastaq)")
            if self.fqfasta[0]:
                f = open(self.fqfasta[0], 'r')

                with f:
                    self.datafq = f.read()
                    self.tela_converter.setar_sequencia.setText(self.datafq)

    def converter(self):
        """

            Função que da funcionalidade a tela de converter da ferramenta,
            convertendo assim a sequencia inserida pelo usuario.

        """
        if self.tela_converter.setar_sequencia.toPlainText() == '':
            QMessageBox.about(self, 'Atenção', 'Selecione um arquivo')
        else:
            if self.tela_converter.comboBox.currentText() == 'GENBANK - FASTA':
                self.gefasta_salvar = QFileDialog.getSaveFileName(
                    self, 'Salvar', "", "Fasta Files (*.fasta)")
                if self.gefasta_salvar[0] != '':
                    with open(self.gefasta[0], "r") as input_handle:
                        with open(self.gefasta_salvar[0], "w") as output_handle:
                            sequences = SeqIO.parse(input_handle, "genbank")
                            count = SeqIO.write(
                                sequences, output_handle, "fasta")
                    QMessageBox.about(None, 'Atenção', 'Sequência convertida')
                else:
                    QMessageBox.about(
                        None, 'Atenção', 'Sequência não convertida')
                self.apagarValoresTelaConverter()
            else:
                self.fqfasta_salvar = QFileDialog.getSaveFileName(
                    self, 'Salvar', "", "Fasta Files (*.fasta)")
                if self.fqfasta_salvar[0] != '':
                    with open(self.fqfasta[0], "r") as input_handle:
                        with open(self.fqfasta_salvar[0], "w") as output_handle:
                            sequences = SeqIO.parse(input_handle, "fastq")
                            count = SeqIO.write(
                                sequences, output_handle, "fasta")
                    QMessageBox.about(None, 'Atenção', 'Sequência convertida')
                else:
                    QMessageBox.about(
                        None, 'Atenção', 'Sequência não convertida')
                self.apagarValoresTelaConverter()

    def fecharAplicacao(self):
        """

            Função para fechar o software.

        """
        QCoreApplication.instance().quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec())
