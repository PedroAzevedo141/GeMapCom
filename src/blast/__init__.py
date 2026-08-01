import subprocess
import tempfile
import pathlib
from typing import Optional

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from src.blast.searchAlign import EmployeeSearch
from src.blast.qDialogAlinhamento import EmployeeDlg
from .graphKablammo import kablammoBlast


class funcBlast():

    def initScreens(self, homeScreen) -> None:
        self.Query: Optional[pathlib.Path] = None
        self.Subject: Optional[pathlib.Path] = None
        self.homeScreen = homeScreen
        self.screenBlast = homeScreen.tela_blast_1
        self.QtStack = homeScreen.QtStack
        self.screenBlast.ButtonQuery.clicked.connect(self.primeiroArquivo)
        self.screenBlast.ButtonSubject.clicked.connect(self.segundoArquivo)
        self.screenBlast.ButtomSearchQuery.clicked.connect(self.launchPopup_query)
        self.screenBlast.ButtomSearchSubject.clicked.connect(self.launchPopup_subject)
        self.screenBlast.Alinhar.clicked.connect(self.alingCheck)
        self.out_file: Optional[pathlib.Path] = None

    def alingCheck(self) -> None:
        if self.Query is not None:
            if self.Subject is not None:
                self.launchPopup()
            else:
                QMessageBox.about(None, "BLAST",
                                  "Informe o Subject para prosseguir com o alinhamento.")
        else:
            QMessageBox.about(None, "BLAST",
                              "Informe o Query para prosseguir com o alinhamento.")

    def ChecagemCheckBox(self) -> None:
        '''
            Função que faz a checagem dos checkBox da pagina. Tem como funcionalidade
            indicar ao programa qual tipo de arquivo final o usuario deseja.
        '''
        if self.screenBlast.Tabular.isChecked():
            self.Estilo = ["-outfmt", "6"]
        elif self.screenBlast.Pairwise.isChecked():
            self.Estilo = ["-outfmt", "0"]
        elif self.screenBlast.ShowingIdentities.isChecked():
            self.Estilo = ["-outfmt", "1"]
        elif self.screenBlast.NoIdentities.isChecked():
            self.Estilo = ["-outfmt", "2"]
        elif self.screenBlast.FLATIdentities.isChecked():
            self.Estilo = ["-outfmt", "3"]
        elif self.screenBlast.FLATnoIdentities.isChecked():
            self.Estilo = ["-outfmt", "4"]
        elif self.screenBlast.XML.isChecked():
            self.Estilo = ["-outfmt", "5"]
        elif self.screenBlast.Tabular_Co.isChecked():
            self.Estilo = ["-outfmt", "7"]
        elif self.screenBlast.ASN1.isChecked():
            self.Estilo = ["-outfmt", "8"]
        elif self.screenBlast.TextoBinary.isChecked():
            self.Estilo = ["-outfmt", "9"]
        elif self.screenBlast.Comma.isChecked():
            self.Estilo = ["-outfmt", "10"]
        elif self.screenBlast.BLAST_Format.isChecked():
            self.Estilo = ["-outfmt", "11"]
        else:
            self.Estilo = []

    def primeiroArquivo(self) -> None:
        '''
            A função tem como funcionalidade:
                -> Inserir, na variavel "self.Query", o caminho no qual o Arquivo 01
                está na maquina do usuario.
                -> E adicionar na tela inicial do BLAST o nome do arquivo e o nome do
                genoma inserido.
        '''
        Filename, _ = QFileDialog.getOpenFileName(None, "SELECIONE O ARQUIVO QUERY", "", "Arquivo de Fasta (*.fasta *.fa)")
        if Filename:
            filepath = pathlib.Path(Filename)
            self.Query = filepath
            self.screenBlast.NomeArquivoQUERY.setText(filepath.name)
            self.screenBlast.CabecalhoArquivoQUERY.setText(
                self.primeiraLinha(filepath)[1:])

    def segundoArquivo(self) -> None:
        '''
            A função tem como funcionalidade:
                -> Inserir, na variavel "self.Subject", o caminho no qual o Arquivo 02
                está na maquina do usuario.
                -> E adicionar na tela inicial do BLAST o nome do arquivo e o nome do
                genoma inserido.
        '''
        Filename, _ = QFileDialog.getOpenFileName(None, "SELECIONE O ARQUIVO SUBJECT", "", "Arquivo de Fasta (*.fasta *.fa)")
        if Filename:
            filepath = pathlib.Path(Filename)
            self.Subject = filepath
            self.screenBlast.NomeArquivoSUBJECT.setText(filepath.name)
            self.screenBlast.CabecalhoArquivoSUBJECT.setText(
                self.primeiraLinha(filepath)[1:])

    def primeiraLinha(self, Arquivo: pathlib.Path) -> str:
        '''
            Tem como funcionalidade retornar o nome do genoma prescrito no arquivo
            inserido pelo usuario.
                Obs. O nome do genoma fica na primeira linha do mapeamento.

            Parametro:
                    Arquivo (pathlib.Path): Caminho do arquivo.

            Retorno:
                    lines (str): Uma string com o nome do genoma mapeado no arquivo.
        '''
        with open(Arquivo, 'r') as f:
            lines = f.readline()
        return lines

    def func_Paramentros(self) -> None:
        '''
            Tem como funcionalidade, guardar os valores atribuidos para o GAP,
            MATCH e MISMATCH.
        '''
        mismatch_val = self.screenBlast.LineMISMATCH.text()
        self.penalty = ["-penalty", mismatch_val] if len(mismatch_val) > 0 else ["-penalty", "-3"]
        
        match_val = self.screenBlast.LineMATCH.text()
        self.reward = ["-reward", match_val] if len(match_val) > 0 else ["-reward", "2"]

    def fileEmpty(self) -> bool:
        if self.out_file and self.out_file.exists():
            return self.out_file.stat().st_size == 0
        return True

    def launchPopup(self) -> None:
        self.type_blast = None
        GUI = EmployeeDlg(self)
        if GUI.exec():
            self.nextScreen()
            
    def launchPopup_query(self) -> None:
        self.type_blast = None
        GUI = EmployeeSearch(self.screenBlast, self, "query_file", "query")
        GUI.exec()
            
    def launchPopup_subject(self) -> None:
        self.type_blast = None
        GUI = EmployeeSearch(self.screenBlast, self, "subject_file", "subject")
        GUI.exec()

    def tabularCheck(self) -> bool:
        if self.screenBlast.Tabular.isChecked() and self.type_blast == "blastn":
            return True
        return False
    
    def xmlCheck(self) -> bool:
        if self.screenBlast.XML.isChecked() and self.type_blast == "blastn":
            return True
        return False

    def nextScreen(self) -> None:
        """
            Função para entrar na tela de FILTROS do BLAST, utilizando o botão
            "Alinhar" da tela inicial do BLAST.
        """
        self.Result = self.Alinhamento(type=self.type_blast)
        if self.Result is not None:
            if self.tabularCheck():
                self.homeScreen.tela_filtros_blast.CaminhoDiretorio_funcao(self.out_file)
                self.QtStack.setCurrentIndex(6)
            elif self.xmlCheck():
                self.homeScreen.tela_resultado_qWebView.abrirQWebView()
                self.QtStack.setCurrentIndex(7)
            else:
                self.homeScreen.tela_resultado_blast.resultadoAlinhamento(self.out_file)
                self.QtStack.setCurrentIndex(5)

    def apagarValoresTelaBlast(self) -> None:
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
        self.Query = None
        self.Subject = None

    def _handle_blast_exit_code(self, exit_code: int, stderr: str = "") -> bool:
        error_details = f"\n\nDetalhes do BLAST:\n{stderr}" if stderr else ""
        if exit_code == 0:
            if self.type_blast == "blastn" and self.fileEmpty():
                QMessageBox.about(None, "Alinhamento", "Error: Sem resultado, verifique os parametros!!")
                return False
            else:
                QMessageBox.about(None, "Alinhamento", "Sucesso: Alinhado com SUCESSO!!")
                if getattr(self, 'Estilo', []) == ["-outfmt", "9"]:
                    QMessageBox.about(None, "Alinhamento", "Sem Opção de Visualização: Arquivo Binario")
                    return False
                return True
        elif exit_code == 1:
            QMessageBox.about(None, "Resultado do Alinhamento", f"Error: Error in query sequence(s) or BLAST options!!{error_details}")
        elif exit_code == 2:
            QMessageBox.about(None, "Resultado do Alinhamento", f"Error: Error in BLAST database!!{error_details}")
        elif exit_code == 3:
            QMessageBox.about(None, "Resultado do Alinhamento", f"Error: Error in BLAST engine!!{error_details}")
        elif exit_code == 4:
            QMessageBox.about(None, "Resultado do Alinhamento", f"Error: Out of memory!!{error_details}")
        elif exit_code == 5:
            QMessageBox.about(None, "Resultado do Alinhamento", f"Error: Network error connecting to NCBI to fetch sequence data!!{error_details}")
        elif exit_code == 6:
            QMessageBox.about(None, "Resultado do Alinhamento", f"Error: Error creating output files!!{error_details}")
        else:
            QMessageBox.about(None, "Resultado do Alinhamento", f"Error: Unknown error ({exit_code})!!{error_details}")
        return False

    def _get_executable_path(self, executable: str) -> str:
        import shutil
        import os
        import glob
        
        # 1. Tenta achar no PATH (funciona se já estiver configurado corretamente)
        if shutil.which(executable):
            return executable
            
        # 2. No Windows, tenta achar com .exe no PATH
        if os.name == 'nt' and shutil.which(f"{executable}.exe"):
            return f"{executable}.exe"
            
        # 3. Busca recursiva no diretório padrão de instalação do Windows
        if os.name == 'nt':
            import glob
            # Padrão para achar qualquer versão do blast instalada
            pattern = rf"C:\Program Files\NCBI\blast-*\bin\{executable}.exe"
            matches = glob.glob(pattern)
            if matches:
                # Retorna a versão mais recente/encontrada
                return matches[-1]
                
        # Se não achou de nenhum jeito, levanta o erro
        raise FileNotFoundError(f"Comando {executable} não encontrado")

    def Alinhamento(self, type: str) -> Optional[bool]:
        '''
            Função principal do BLAST. Nela está todas as informações inseridas
            pelo usuario.
            O resumo desta função está na função subprocess.run que faz o sistema
            rodar o BLASTN usando comandos do terminal para rodar o que o usuario informou.
            Também contém diversas condições para que não exista falta de informações.

            Retorno:
                    (Bool): O retorno booleano serve para notificar o erro para o software
                    e assim não dar continuidade.
        '''
        if self.Query is None or self.Subject is None:
            QMessageBox.about(None, "Alinhamento", "Error: Arquivo não INSERIDO!!")
            return None

        try:
            exe_path = self._get_executable_path(type)
        except FileNotFoundError:
            QMessageBox.about(None, "Erro", f"Falha ao executar BLAST: O comando '{type}' não foi encontrado.\n\nO GeMapCom tentou procurar na pasta C:\\Program Files\\NCBI, mas não encontrou. Verifique se o NCBI BLAST+ está instalado corretamente.")
            return None

        cmd = [exe_path, "-query", str(self.Query), "-subject", str(self.Subject)]
        
        fd, temp_path = tempfile.mkstemp(suffix=".out")
        import os
        os.close(fd)
        self.out_file = pathlib.Path(temp_path)
        
        if type == "blastn":
            self.func_Paramentros()
            self.ChecagemCheckBox()
            if self.screenBlast.XML.isChecked():
                self.out_file = self.out_file.with_suffix(".xml")
            cmd.extend(self.Estilo)
            cmd.extend(self.penalty)
            cmd.extend(self.reward)
            
        cmd.extend(["-out", str(self.out_file)])
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            exit_code = result.returncode
            stderr_text = result.stderr.strip()
        except FileNotFoundError:
            QMessageBox.about(None, "Erro", f"Falha ao executar BLAST: O comando '{type}' não foi encontrado.\n\nVerifique se o NCBI BLAST+ está instalado e adicionado ao PATH do Windows (Variáveis de Ambiente). Se você instalou agora, reinicie o terminal/computador.")
            return None
        except Exception as e:
            QMessageBox.about(None, "Erro", f"Falha ao executar BLAST: {str(e)}")
            return None
            
        is_success = self._handle_blast_exit_code(exit_code, stderr_text)
        return True if is_success else None
