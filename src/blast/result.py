import pathlib
from typing import Union, Optional

class resultBlast():
    
    def initScreens(self, homeScreen) -> None:
        self.homeScreen = homeScreen
        self.screenBlast = homeScreen.tela_blast
        self.screenResult = homeScreen.tela_resultado_blast_1
        
        self.screenResult.Finalizar.clicked.connect(self.voltarTelaPrincipal)
        self.screenResult.Voltar.clicked.connect(self.voltarTela)
        
    def voltarTelaPrincipal(self) -> None:
        self.screenBlast.apagarValoresTelaBlast()
        self.homeScreen.QtStack.setCurrentIndex(0)
        
    def voltarTela(self) -> None:
        """
            Função de funcionalidade do botão "Voltar"
        """
        if self.homeScreen.tela_blast.tabularCheck():
            self.homeScreen.QtStack.setCurrentIndex(6)
        else:
            self.homeScreen.QtStack.setCurrentIndex(4)
            
    def resultadoFiltragem(self, file_path: Optional[Union[str, pathlib.Path]] = None) -> None:
        """
            Função que abre e lê o arquivo filtrado e ilustra o mesmo na tela.
        """
        p = pathlib.Path(file_path) if file_path else pathlib.Path('Filtragem.out')
        if p.exists():
            with open(p, 'r') as f:
                file_text = f.read()
            self.screenResult.Saida.setText(file_text)

    def resultadoAlinhamento(self, file_path: Optional[Union[str, pathlib.Path]] = None) -> None:
        """
            Função que abre e lê o arquivo de resultado e ilustra o mesmo na tela.
        """
        p = pathlib.Path(file_path) if file_path else pathlib.Path('ResultAlin.out')
        if p.exists():
            with open(p, 'r') as f:
                file_text = f.read()
            self.screenResult.Saida.setText(file_text)
