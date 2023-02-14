import glob
import warnings
import numpy as np
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
        print(dir_path)
        files_align = glob.glob(dir_path)
        self.alinhamentos = pd.read_csv(files_align[0], header=None, delimiter='	')
        # print('Alinhamentos da: {}'.format(len(alinhamentos)))
        if self.screenFiltros_ui.checkBox_Identidade.isChecked():
            self.filtroIdentidade()
        if self.screenFiltros_ui.checkBox_EValue.isChecked():
            self.filtroEValue()
        if self.screenFiltros_ui.checkBox_RAG.isChecked():
            pass
        
    def filtroRAG(self):
        pass
        # limiar = self.screenFiltros_ui.SpinBox_RAG.value()
        # len_alig = list(np.absolute(self.alinhamentos[9]-self.alinhamentos[8]))
        # gene_names = list(self.alinhamentos[1])
        # size_gene = []
        # for gn in gene_names:
        #     size_gene.append(look_gene(gn, genes_inform))
        # razao = np.zeros([len(len_alig), 2])
        # for id_la, la in enumerate(len_alig):
        #     razao[id_la, 0] = int(id_la)
        #     razao[id_la, 1] = la/size_gene[id_la]
        # cont_limiar = 0
        # t = pd.DataFrame()
        # for i in razao:
        #     if i[1] >= limiar:
        #         t = t.append(self.alinhamentos.iloc[int(i[0])])
        #         cont_limiar += 1
        # print("Alinhamentos após limiar da razao alinhamento/gene:", len(t))
        # return t, razao
        
    def filtroIdentidade(self):
        genes_unicos = self.alinhamentos[1].unique()
        t = self.alinhamentos[(self.alinhamentos[1] == genes_unicos[0])]
        m = t[2].argmax()
        t.loc[[m]]
        for gu in genes_unicos[1:]:
            t2 = self.alinhamentos[(self.alinhamentos[1] == gu)]
            m = t2[2].argmax()
            t2 = t2.loc[[m]]
            t = t.append(t2)
        self.alinhamentos = t
        # print("Alinhamentos após filtro de identidade:", len(self.alinhamentos))
        
        arquivo = open("Filtragem.out", "w")
        arquivo.write(self.alinhamentos.to_string())
        arquivo.close()
        
    def filtroEValue(self):
        e = self.screenFiltros_ui.SpinBox_EValue.value()
        self.alinhamentos = self.alinhamentos[self.alinhamentos[10] <= e]
        # print("Alinhamentos após limiar do E-value:", len(self.alinhamentos))
        
        arquivo = open("Filtragem.out", "w")
        arquivo.write(self.alinhamentos.to_string())
        arquivo.close()
