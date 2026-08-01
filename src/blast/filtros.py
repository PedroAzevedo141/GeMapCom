import glob
import warnings
import numpy as np
import pandas as pd
import pathlib
from typing import Optional

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *


class filtrosBlast:

    def initScreens(self, homeScreen) -> None:
        self.homeScreen = homeScreen
        self.screenResult = homeScreen.tela_resultado_blast
        self.screenFiltros_ui = homeScreen.tela_filtros_blast_1
        self.caminhoDiretorio: Optional[pathlib.Path] = None
        self.out_file: Optional[pathlib.Path] = None

        self.screenFiltros_ui.pushButton_Voltar.clicked.connect(
            self.abrirTelaBlast)
        self.screenFiltros_ui.pushButton_Continuar.clicked.connect(
            self.resultadoBlast)

    def resultadoBlast(self) -> None:
        """
            Função para abrir a tela de resultados do BLAST contendo o resultado
            apos as filtragens.
        """
        self.Filtragem()
        self.screenResult.resultadoFiltragem(self.out_file)
        self.homeScreen.QtStack.setCurrentIndex(5)

    def apagarValoresTelaFiltros(self) -> None:
        """
            Função para apagar os valores da tela dos FILTROS do BLAST.
        """
        self.screenFiltros_ui.checkBox_Identidade.setChecked(False)
        self.screenFiltros_ui.checkBox_EValue.setChecked(False)
        self.screenFiltros_ui.checkBox_RAG.setChecked(False)

    def abrirTelaBlast(self) -> None:
        """
            Função para abrir tela do INICIAL do BLAST.
        """
        self.apagarValoresTelaFiltros()
        self.homeScreen.QtStack.setCurrentIndex(4)

    def CaminhoDiretorio_funcao(self, caminhoAlinhamento: pathlib.Path) -> None:
        """
            Função que busca o caminho do arquivo, no servidor do usuario, no
            qual está o resultado do alinhamento realizado.
        """
        self.caminhoDiretorio = pathlib.Path(caminhoAlinhamento)

    def Filtragem(self) -> None:
        """
            Tem como funcionalidade realizar três tipos de filtragem.
        """
        if self.caminhoDiretorio is None:
            return

        file_path = self.caminhoDiretorio
        self.alinhamentos = pd.read_csv(file_path, header=None, delimiter='\t')
        self.out_file = file_path.with_name("Filtragem.out")

        if self.screenFiltros_ui.checkBox_Identidade.isChecked() or self.screenFiltros_ui.checkBox_EValue.isChecked() or self.screenFiltros_ui.checkBox_RAG.isChecked():
            if self.screenFiltros_ui.checkBox_Identidade.isChecked():
                self.filtroIdentidade()
            if self.screenFiltros_ui.checkBox_EValue.isChecked():
                self.filtroEValue()
            if self.screenFiltros_ui.checkBox_RAG.isChecked():
                pass
        else:
            with open(self.out_file, "w") as arquivo:
                arquivo.write(self.alinhamentos.to_string())

    def filtroRAG(self) -> None:
        pass

    def filtroIdentidade(self) -> None:
        genes_unicos = self.alinhamentos[1].unique()
        frames = []
        for gu in genes_unicos:
            t = self.alinhamentos[self.alinhamentos[1] == gu]
            m = t[2].idxmax()
            frames.append(t.loc[[m]])
            
        if frames:
            self.alinhamentos = pd.concat(frames)

        with open(self.out_file, "w") as arquivo:
            arquivo.write(self.alinhamentos.to_string())

    def filtroEValue(self) -> None:
        e = self.screenFiltros_ui.SpinBox_EValue.value()
        self.alinhamentos = self.alinhamentos[self.alinhamentos[10] <= e]

        with open(self.out_file, "w") as arquivo:
            arquivo.write(self.alinhamentos.to_string())
