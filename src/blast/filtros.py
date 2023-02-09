import glob
import warnings
import pandas as pd

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class filtrosBlast:
    
    def initScreens(self, homeScreen) -> None:
        self.homeScreen = homeScreen
        self.screenResult = homeScreen.tela_resultado_blast
        self.screenFiltros_ui = homeScreen.tela_filtros_blast_1
        
        self.screenFiltros_ui.pushButton_Voltar.clicked.connect(self.abrirTelaBlast)
        self.screenFiltros_ui.pushButton_Continuar.clicked.connect(self.resultadoBlast)
        
    def resultadoBlast(self):
        """

            Função para abrir a tela de resultados do BLAST contendo o resultado
            apos as filtragens.

        """
        self.Filtragem()
        self.screenResult.resultadoFiltragem()
        self.homeScreen.QtStack.setCurrentIndex(5)
        
    def apagarValoresTelaFiltros(self):
        """

            Função para apagar os valores da tela dos FILTROS do BLAST.

        """
        self.screenFiltros_ui.checkBox_Identidade.setChecked(False)
        self.screenFiltros_ui.checkBox_EValue.setChecked(False)
        self.screenFiltros_ui.checkBox_RAG.setChecked(False)
        
    def abrirTelaBlast(self):
        """

            Função para abrir tela do INICIAL do BLAST.

        """
        self.apagarValoresTelaFiltros()
        self.homeScreen.QtStack.setCurrentIndex(4)
        
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
        alinhamentos = pd.read_csv(files_align[0], header=None, delimiter='	')
        # print('Alinhamentos da: {}'.format(len(alinhamentos)))
        if self.screenFiltros_ui.checkBox_Identidade.isChecked():
            genes_unicos = alinhamentos[1].unique()
            t = alinhamentos[(alinhamentos[1] == genes_unicos[0])]
            m = t[2].argmax()
            t.loc[[m]]
            for gu in genes_unicos[1:]:
                t2 = alinhamentos[(alinhamentos[1] == gu)]
                m = t2[2].argmax()
                t2 = t2.loc[[m]]
                t = t.append(t2)
            alinhamentos = t
            # print("Alinhamentos após filtro de identidade:", len(alinhamentos))
        if self.screenFiltros_ui.checkBox_EValue.isChecked():
            e = self.screenFiltros_ui.SpinBox_EValue.value()
            alinhamentos = alinhamentos[alinhamentos[10] <= e]
            # print("Alinhamentos após limiar do E-value:", len(alinhamentos))
        if self.screenFiltros_ui.checkBox_RAG.isChecked():
            pass
        arquivo = open("Filtragem.out", "w")
        arquivo.write(alinhamentos.to_string())
        arquivo.close()
