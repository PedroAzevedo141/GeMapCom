import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from Bio import SeqIO

from telas.tela_principal import Ui_Tela_Principal
from telas.tela_comparacao import Ui_Tela_Comparacao
from telas.tela_converter import Ui_Tela_Converter
from telas.tela_resultado import Ui_Tela_Resultado
from telas.tela_BLAST import Ui_tela_BLAST
from telas.tela_resultado_BLAST import Ui_tela_Resultado_BLAST
from telas.tela_filtros_BLAST import Ui_tela_Filtros_BLAST


from algoritmos.algorithm_needleman_wunsch import algorithm_needleman
from algoritmos.algorithm_smith_waterman import algorithm_smith

from plotar.main import criar_imagem

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(1276, 585)
        Main.setFixedSize(1276, 585)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()

        self.tela_principal = Ui_Tela_Principal()
        self.tela_principal.setupUi(self.stack0)

        self.tela_comparacao = Ui_Tela_Comparacao()
        self.tela_comparacao.setupUi(self.stack1)

        self.tela_converter = Ui_Tela_Converter()
        self.tela_converter.setupUi(self.stack2)

        self.tela_resultado = Ui_Tela_Resultado()
        self.tela_resultado.setupUi(self.stack3)

        self.tela_blast = Ui_tela_BLAST()
        self.tela_blast.setupUi(self.stack4)

        self.tela_resultado_blast = Ui_tela_Resultado_BLAST()
        self.tela_resultado_blast.setupUi(self.stack5)

        self.tela_filtros_blast = Ui_tela_Filtros_BLAST()
        self.tela_filtros_blast.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.seq1 = '' # sequencia 1 data 1
        self.data1 = ''

        self.seq2 = '' # sequencia 2 data 2
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
        self.string_converter1  = ''
        self.string_convertida1 = ''

        self.lista_converter2 = []
        self.seq_converter1 = ''
        self.string_converter2 = ''
        self.string_convertida2 = ''

        self.tela_principal.botao_tela_comparacao.clicked.connect(self.abrirTelaComparacao) # funções dos botões da tela principal
        self.tela_principal.botao_sair.clicked.connect(self.fecharAplicacao)
        self.tela_principal.botao_tela_converter.clicked.connect(self.abrirTelaConverter)
        self.tela_principal.botao_tela_outras.clicked.connect(self.abrirTelaBlast)

        self.tela_comparacao.botao_voltar.clicked.connect(self.voltarTelaPrincipal) # funções dos botões da tela comparação
        self.tela_comparacao.botao_abrir_arquivo1.clicked.connect(self.abrirArquivo1)
        self.tela_comparacao.botao_abrir_arquivo2.clicked.connect(self.abrirArquivo2)
        self.tela_comparacao.botao_realizar_comparacao.clicked.connect(self.comparacao)

        self.tela_converter.botao_voltar.clicked.connect(self.voltarTelaPrincipal) # funções dos botões da tela converter
        self.tela_converter.botao_abrir_arquivo.clicked.connect(self.abrirArquivoConverter)
        self.tela_converter.botao_converter.clicked.connect(self.converter)

        self.tela_resultado.botao_voltar.clicked.connect(self.abrirTelaComparacao) # funções dos botões da tela resultado
        self.tela_resultado.botao_salvar.clicked.connect(self.salvarResultadoTxt)
        self.tela_resultado.bota_gerar_imagem.clicked.connect(self.salvarImgem)


        self.Result = None

        self.CaminhoDiretorio = os.path.dirname(os.path.realpath(__file__))          #TELA BLAST
        self.tela_blast.Voltar_Prin.clicked.connect(self.voltarTelaPrincipal)
        self.tela_blast.Alinhar.clicked.connect(self.tela_Filtro1_F)
        self.tela_filtros_blast.CaminhoDiretorio_funcao(self.CaminhoDiretorio)
        self.tela_resultado_blast.Voltar.clicked.connect(self.tela_Filtro2_F)
        self.tela_resultado_blast.Finalizar.clicked.connect(self.voltarTelaPrincipal)
        self.tela_filtros_blast.pushButton_Voltar.clicked.connect(self.abrirTelaBlast)
        self.tela_filtros_blast.pushButton_Continuar.clicked.connect(self.resultadoBlast)

    def apagarValoresTelaComparacao(self): # apagar os valores da tela comparação
        self.tela_comparacao.setar_sequencia1.setText('')
        self.tela_comparacao.setar_sequencia2.setText('')
        self.tela_comparacao.match.setText('')
        self.tela_comparacao.mismatch.setText('')
        self.tela_comparacao.gap.setText('')

        self.tela_resultado.setar_resultado.setText('')

        self.resultado = ''
        self.resultado_salvar = ''
        self.lista_salvar_resultado = []


        self.algo_needle = algorithm_needleman('', '', None , None, None)

        self.algo_water = algorithm_smith('', '', None, None, None)

        self.create_image = criar_imagem('', '', '', '', None, None)

        self.lista_converter1 = []
        self.seq_converter1 = ''
        self.string_converter1  = ''
        self.string_convertida1 = ''

        self.lista_converter2 = []
        self.seq_converter2 = ''
        self.string_converter2 = ''
        self.string_convertida2 = ''

    def apagarValoresTelaConverter(self):
        self.tela_converter.setar_sequencia.setText('') # apagar os valores da tela converter

    def apagarValoresTelaBlast(self):
        self.tela_blast.NomeArquivoQUERY.clear()
        self.tela_blast.CabecalhoArquivoQUERY.clear()
        self.tela_blast.NomeArquivoSUBJECT.clear()
        self.tela_blast.CabecalhoArquivoSUBJECT.clear()
        self.tela_blast.Query = ''
        self.tela_blast.Subject = ''

    def apagarValoresTelaFiltros(self):
        self.tela_filtros_blast.checkBox_Identidade.setChecked(False)
        self.tela_filtros_blast.checkBox_EValue.setChecked(False)
        self.tela_filtros_blast.checkBox_RAG.setChecked(False)

    def voltarTelaPrincipal(self): # função para voltar tela principal
        self.apagarValoresTelaComparacao()
        self.apagarValoresTelaConverter()
        self.apagarValoresTelaBlast()

        self.QtStack.setCurrentIndex(0)

    def tela_Filtro1_F(self):
        self.Result = self.tela_blast.Alinhamento()
        if self.Result != None:
            self.tela_resultado_blast.Teste()
            if (self.tela_blast.Tabular.isChecked()):
                self.QtStack.setCurrentIndex(6)
            else:
                self.QtStack.setCurrentIndex(5)

    def tela_Filtro2_F(self):
        if (self.tela_blast.Tabular.isChecked()):
            self.QtStack.setCurrentIndex(6)
        else:
            self.apagarValoresTelaBlast()
            self.QtStack.setCurrentIndex(4)

    def tela_Main2_F(self):
        self.apagarValoresTelaBlast()
        self.QtStack.setCurrentIndex(4)

    def resultadoBlast(self):
        self.tela_filtros_blast.Filtragem()
        self.tela_resultado_blast.Teste()
        self.QtStack.setCurrentIndex(5)

    def abrirTelaComparacao(self): # função para abrir tela de comparação
        self.apagarValoresTelaComparacao()
        self.QtStack.setCurrentIndex(5)

    def abrirTelaConverter(self): # função para abrir tela de converter
        self.QtStack.setCurrentIndex(6)

    def abrirTelaBlast(self):
        self.apagarValoresTelaFiltros()
        self.QtStack.setCurrentIndex(4)

    def abrirArquivo1(self): # função para abrir sequencia 1 e colocar na tela
        self.seq1 = QFileDialog.getOpenFileName(self, 'Abrir sequencia 1', '/home', "Fasta Files (*.fasta *.fa)")
        if self.seq1[0]:
            f = open(self.seq1[0], 'r')

            with f:
                # self.data1 = f.readline()
                self.data1 = f.read()
                self.tela_comparacao.setar_sequencia1.setText(self.data1)

    def abrirArquivo2(self): # função para abrir sequencia 2 e colocar na tela
        self.seq2 = QFileDialog.getOpenFileName(self, 'Abrir sequencia 2', '/home', "Fasta Files (*.fasta *.fa)")
        if self.seq2[0]:
            f = open(self.seq2[0], 'r')

            with f:
                # self.data2 = f.readline()
                self.data2 = f.read()
                self.tela_comparacao.setar_sequencia2.setText(self.data2)

    def comparacao(self):
        match = self.tela_comparacao.match.text()
        mismatch = self.tela_comparacao.mismatch.text()
        gap = self.tela_comparacao.gap.text()

        if self.tela_comparacao.setar_sequencia1.toPlainText() == '' or self.tela_comparacao.setar_sequencia2.toPlainText() == '':
            QMessageBox.about(self, 'Atenção', 'Selecione um arquivo')

        elif not self.validarNumero(match, mismatch, gap):
            QMessageBox.about(self, 'Atenção', 'Preencha todos os campos somente com números!!')

        elif self.tela_comparacao.comboBox.currentText() == 'GLOBAL':
            self.comparacaoGlobal()

        else:
            self.comparacaoLocal()

    def comparacaoGlobal(self):
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
        try:
            match = int(match)
            mismatch = int(mismatch)
            gap = int(gap)
            return True
        except:
            return False

    def salvarResultadoTxt(self):
        self.resultado = QFileDialog.getSaveFileName(self, 'Salvar Resultado', '/home', "Text (*.txt *.asc)")

        if self.resultado[0]:
            self.resultado_salvar = open(self.resultado[0], 'w')
            with self.resultado_salvar:
                self.resultado_salvar.writelines(self.lista_salvar_resultado)
                self.resultado_salvar.close()

        QMessageBox.about(self,'Atenção', 'Resultado Salvo')

    def salvarImgem(self):
        if(self.tela_comparacao.comboBox.currentText() == 'GLOBAL'):
            img, _ = QFileDialog.getSaveFileName(self, 'Salvar Imagem', '/home', filter="PNG(*.png);; JPEG(*.jpg)")
            self.create_image = criar_imagem(img, self.algo_needle.align1, self.algo_needle.align2, self.algo_needle.sym, str(self.algo_needle.ident), str(self.algo_needle.seq_score))
            if img[-3:] == "png":
                self.create_image.salvarImage()
                QMessageBox.about(self,'Atenção', 'Imagem Salva')
            elif img[-3:] == "jpg":
                self.create_image.salvarImage()
                QMessageBox.about(self,'Atenção', 'Imagem Salva')

        else:
            img, _ = QFileDialog.getSaveFileName(self, 'Salvar Imagem', '/home', filter="PNG(*.png);; JPEG(*.jpg)")
            self.create_image = criar_imagem(img, self.algo_water.align1, self.algo_water.align2, self.algo_water.sym, str(self.algo_water.identity), str(self.algo_water.max_score))
            if img[-3:] == "png":
                self.create_image.salvarImage()
                QMessageBox.about(self,'Atenção', 'Imagem Salva')
            elif img[-3:] == "jpg":
                self.create_image.salvarImage()
                QMessageBox.about(self,'Atenção', 'Imagem Salva')

    def abrirArquivoConverter(self): # função para abrir sequencia de converter
        if self.tela_converter.comboBox.currentText() == 'GENBANK - FASTA':
            self.gefasta = QFileDialog.getOpenFileName(self, 'Abrir sequencia', '/home', "Genbank Files (*.gbk)")
            if self.gefasta[0]:
                f = open(self.gefasta[0], 'r')

                with f:
                    self.datage = f.read()
                    self.tela_converter.setar_sequencia.setText(self.datage)
        else:
            self.fqfasta = QFileDialog.getOpenFileName(self, 'Abrir sequencia', '/home', "FastaQ Files (*.fastaq)")
            if self.fqfasta[0]:
                f = open(self.fqfasta[0], 'r')

                with f:
                    self.datafq = f.read()
                    self.tela_converter.setar_sequencia.setText(self.datafq)

    def converter(self): # função para converter sequencia de converter
        if self.tela_converter.setar_sequencia.toPlainText() == '':
            QMessageBox.about(self, 'Atenção', 'Selecione um arquivo')
        else:
            if self.tela_converter.comboBox.currentText() == 'GENBANK - FASTA':
                QMessageBox.about(self,'Atenção', 'Sequencia convertida')
                self.gefasta_salvar = QFileDialog.getSaveFileName(self, 'Salvar', '/home', "Fasta Files (*.fasta)")
                with open(self.gefasta[0], "r") as input_handle:
                    with open(self.gefasta_salvar[0], "w") as output_handle:
                        sequences = SeqIO.parse(input_handle, "genbank")
                        count = SeqIO.write(sequences, output_handle, "fasta")
                self.apagarValoresTelaConverter()
            else:
                QMessageBox.about(self,'Atenção', 'Sequencia convertida')
                self.fqfasta_salvar = QFileDialog.getSaveFileName(self, 'Salvar', '/home', "Fasta Files (*.fasta)")
                with open(self.fqfasta[0], "r") as input_handle:
                    with open(self.fqfasta_salvar[0], "w") as output_handle:
                        sequences = SeqIO.parse(input_handle, "fastq")
                        count = SeqIO.write(sequences, output_handle, "fasta")
                self.apagarValoresTelaConverter()

    def fecharAplicacao(self): # função para fechar aplicação
        QCoreApplication.instance().quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
