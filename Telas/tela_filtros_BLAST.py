from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import os
import Bio
import glob
import warnings
import numpy as np
import pandas as pd
from Bio import SeqIO
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
from matplotlib.lines import Line2D
class Ui_tela_Filtros_BLAST(object):
    """

    Classe que contem todas as configurações da tela dos filtros do BLAST.

    Nessa classe usa-se propriedades da biblioteca PyQt5 para facilitar o
    gerenciamento das configurações e interações da tela em questão.

    """
    def setupUi(self, Filtros):
        Filtros.setObjectName("Filtros")
        Filtros.resize(922, 586)
        Filtros.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(Filtros)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QScrollArea(self.centralwidget)
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.scrollArea.setFont(font)
        self.scrollArea.setContextMenuPolicy(Qt.CustomContextMenu)
        self.scrollArea.setAcceptDrops(True)
        self.scrollArea.setStatusTip("")
        self.scrollArea.setWhatsThis("")
        self.scrollArea.setAccessibleDescription("")
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 837, 481))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_Voltar = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Voltar.setMaximumSize(QSize(100, 16777215))
        self.pushButton_Voltar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Voltar.setObjectName("pushButton_Voltar")
        self.gridLayout_2.addWidget(self.pushButton_Voltar, 11, 0, 1, 1)
        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 5, 1, 1, 1)
        self.line_8 = QFrame(self.scrollAreaWidgetContents)
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_2.addWidget(self.line_8, 8, 0, 1, 1)
        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 3, 1, 1, 1)
        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 7, 1, 1, 1)
        self.line_10 = QFrame(self.scrollAreaWidgetContents)
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_2.addWidget(self.line_10, 8, 2, 1, 1)
        self.line_7 = QFrame(self.scrollAreaWidgetContents)
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 2, 0, 1, 1)
        self.checkBox_EValue = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_EValue.setObjectName("checkBox_EValue")
        self.gridLayout_2.addWidget(self.checkBox_EValue, 5, 0, 1, 1)
        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 6, 0, 1, 2)
        self.checkBox_RAG = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_RAG.setObjectName("checkBox_RAG")
        self.gridLayout_2.addWidget(self.checkBox_RAG, 7, 0, 1, 1)
        self.line_11 = QFrame(self.scrollAreaWidgetContents)
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_2.addWidget(self.line_11, 6, 2, 1, 1)
        self.checkBox_Identidade = QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox_Identidade.setObjectName("checkBox_Identidade")
        self.gridLayout_2.addWidget(self.checkBox_Identidade, 3, 0, 1, 1)
        self.logo = QLabel(self.scrollAreaWidgetContents)
        self.logo.setFrameShape(QFrame.Box)
        self.logo.setFrameShadow(QFrame.Sunken)
        self.logo.setLineWidth(3)
        self.logo.setAlignment(Qt.AlignCenter)
        self.logo.setWordWrap(False)
        self.logo.setObjectName("logo")
        self.gridLayout_2.addWidget(self.logo, 0, 0, 1, 4)
        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 4, 0, 1, 1)
        self.label_EspacoBranco1 = QLabel(self.scrollAreaWidgetContents)
        self.label_EspacoBranco1.setAutoFillBackground(True)
        self.label_EspacoBranco1.setText("")
        self.label_EspacoBranco1.setObjectName("label_EspacoBranco1")
        self.gridLayout_2.addWidget(self.label_EspacoBranco1, 10, 0, 1, 4)
        self.SpinBox_RAG = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.SpinBox_RAG.setCursor(QCursor(Qt.IBeamCursor))
        self.SpinBox_RAG.setDecimals(10)
        self.SpinBox_RAG.setMaximum(1.0)
        self.SpinBox_RAG.setObjectName("SpinBox_RAG")
        self.gridLayout_2.addWidget(self.SpinBox_RAG, 7, 2, 1, 2)
        self.SpinBox_EValue = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.SpinBox_EValue.setCursor(QCursor(Qt.IBeamCursor))
        self.SpinBox_EValue.setWrapping(False)
        self.SpinBox_EValue.setAccelerated(False)
        self.SpinBox_EValue.setKeyboardTracking(True)
        self.SpinBox_EValue.setProperty("showGroupSeparator", False)
        self.SpinBox_EValue.setDecimals(10)
        self.SpinBox_EValue.setMaximum(1.0)
        self.SpinBox_EValue.setObjectName("SpinBox_EValue")
        self.gridLayout_2.addWidget(self.SpinBox_EValue, 5, 2, 1, 2)
        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 3, 2, 1, 2)
        self.line_12 = QFrame(self.scrollAreaWidgetContents)
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout_2.addWidget(self.line_12, 4, 2, 1, 2)
        self.line_9 = QFrame(self.scrollAreaWidgetContents)
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_2.addWidget(self.line_9, 2, 2, 1, 2)
        self.pushButton_Continuar = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_Continuar.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_Continuar.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Continuar.setObjectName("pushButton_Continuar")
        self.gridLayout_2.addWidget(self.pushButton_Continuar, 11, 3, 1, 1)
        self.label_EspacoBranco2 = QLabel(self.scrollAreaWidgetContents)
        self.label_EspacoBranco2.setText("")
        self.label_EspacoBranco2.setObjectName("label_EspacoBranco2")
        self.gridLayout_2.addWidget(self.label_EspacoBranco2, 1, 0, 1, 4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        Filtros.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Filtros)
        self.statusbar.setObjectName("statusbar")
        Filtros.setStatusBar(self.statusbar)

        self.retranslateUi(Filtros)
        QMetaObject.connectSlotsByName(Filtros)

    def CaminhoDiretorio_funcao(self, caminhoAlinhamento):
        """

            Função que busca o caminho do arquivo, no servidor do usuario, no
            qual está o resultado do alinhamento realizado.

            Parametro:
                    caminhoAlinhamento (str): Uma string que contém o endereço do arquivo.

            --> Função usada no GeMapCom.py

        """
        self.caminhoDiretorio = caminhoAlinhamento

    def Filtragem(self):
        """

            Tem como funcionalidade realizar três tipos de filtragem, sendo eles:
                - Filtro de identidade: Filtra de acordo com a identidade resultante
                dos alinhamentos comparado com o valor inserido pelo usuario.
                - Filtro do E-Value: Filtra de acordo com o E-Value resultante
                dos alinhamentos comparado com o valor inserido pelo usuario.
                - Filtro RAG: Filtragem pela Razão entre o Tamanho do Alinhamento e o
                Tamanho do Gene (RAG)

            Ao terminar de filtrar o alinhamento obtido, o resultado é colocado
            em um novo arquivo, nomeado de "Filtragem.out", para ser ilustrado na
            tela de resultados.

            --> Função usada no GeMapCom.py

        """
        dir_path = self.caminhoDiretorio + "/ResultAlin.out"
        files_align = glob.glob(dir_path)
        alinhamentos = pd.read_csv(files_align[0],header=None,delimiter = '	')
        # print('Alinhamentos da: {}'.format(len(alinhamentos)))
        if self.checkBox_Identidade.isChecked():
            genes_unicos = alinhamentos[1].unique()
            t = alinhamentos[(alinhamentos[1]==genes_unicos[0])]
            m = t[2].argmax()
            t.loc[[m]]
            for gu in genes_unicos[1:]:
                t2 = alinhamentos[(alinhamentos[1]==gu)]
                m = t2[2].argmax()
                t2 = t2.loc[[m]]
                t = t.append(t2)
            alinhamentos = t
            # print("Alinhamentos após filtro de identidade:", len(alinhamentos))
        if self.checkBox_EValue.isChecked():
            e = self.SpinBox_EValue.value()
            alinhamentos = alinhamentos[alinhamentos[10] <= e]
            # print("Alinhamentos após limiar do E-value:", len(alinhamentos))
        if self.checkBox_RAG.isChecked():
            pass
        arquivo = open("Filtragem.out", "w")
        arquivo.write(alinhamentos.to_string())
        arquivo.close()

    def retranslateUi(self, Filtros):
        _translate = QCoreApplication.translate
        Filtros.setWindowTitle(_translate("Filtros", "BLAST - Tela dos Filtros"))
        self.scrollArea.setToolTip(_translate("Filtros", "Digite o valor o E-Value ..."))
        self.scrollArea.setAccessibleName(_translate("Filtros", "Digite o valor o E-Value ..."))
        self.pushButton_Voltar.setText(_translate("Filtros", "Voltar"))
        self.checkBox_EValue.setText(_translate("Filtros", "Filtro dos alinhamentos gerados pelo E-Value"))
        self.checkBox_RAG.setText(_translate("Filtros", "Filtro pela Razão entre o Tamanho do Alinhamento e o Tamanho do Gene (RAG)"))
        self.checkBox_Identidade.setText(_translate("Filtros", "Filtro por Identidade"))
        self.logo.setText(_translate("Filtros", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; text-decoration: underline;\">BLAST</span></p></body></html>"))
        self.SpinBox_RAG.setToolTip(_translate("Filtros", "Digite o valor do Limiar ..."))
        self.SpinBox_EValue.setToolTip(_translate("Filtros", "Digite o valor o E-Value ..."))
        self.pushButton_Continuar.setText(_translate("Filtros", "Continuar"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Filtros = QMainWindow()
    ui = Ui_tela_Filtros_BLAST()
    ui.setupUi(Filtros)
    Filtros.show()
    sys.exit(app.exec_())
