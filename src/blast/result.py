class resultBlast():
    
    def initScreens(self, homeScreen) -> None:
        self.homeScreen = homeScreen
        self.screenBlast = homeScreen.tela_blast
        self.screenResult = homeScreen.tela_resultado_blast_1
        
        self.screenResult.Finalizar.clicked.connect(self.voltarTelaPrincipal)
        self.screenResult.Voltar.clicked.connect(self.voltarTela)
        
    def voltarTelaPrincipal(self):
        self.screenBlast.apagarValoresTelaBlast()
        
        self.homeScreen.QtStack.setCurrentIndex(0)
        
    def voltarTela(self):
        """

            Função de funcionalidade do botão "Voltar" que está na tela de RESULTADOS
            do BLAST, dependendo do tipo de saida do resultado o "Voltar" irá para
            uma tela especifica, como os filtros só tem funcionalidade para as saídas
            TABULAR, então, se o resultado for TABULAR, quando apertar o botão "Voltar"
            irá para tela de filtros, caso não seja TABULAR a tela será a de INICIO
            do BLAST.

        """
        if (self.homeScreen.tela_blast.tabularCheck()):
            self.homeScreen.QtStack.setCurrentIndex(6)
        else:
            self.homeScreen.QtStack.setCurrentIndex(4)
            
    def resultadoFiltragem(self):
        """

            Função que abre e lê o arquivo "Filtragem.out" e ilustra o mesmo na
            tela.

        """
        Result = 'Filtragem.out'
        f = open(Result, 'r')
        file_text = f.read()
        self.screenResult.Saida.setText(file_text)
        f.close()

    def resultadoAlinhamento(self):
        """

            Função que abre e lê o arquivo "ResultAlin.out" e ilustra o mesmo na
            tela.

        """
        Result = 'ResultAlin.out'
        f = open(Result, 'r')
        file_text = f.read()
        self.screenResult.Saida.setText(file_text)
        f.close()
