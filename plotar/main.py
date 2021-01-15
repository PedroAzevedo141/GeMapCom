#Arquivo para criar a imagem do resultado.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.patches as mpatches

class criar_imagem:
    """
    Uma classe para criação de um arquivo contendo uma imagem das sequencias
    informadas pelo usuario ou retornadas da ferramenta.

    ...

    Atributos
    ---------
    path : str
        String contendo o caminho no qual o arquivo será salvo.
    seq1 : str
        String contendo a primeira sequencia de genomas.
    seq2 : str
        String contendo a segunda sequencia de genomas.
    sym : str

    ident : str
        String contendo o valor da identidade final.
    score : str
        String contendo o valor do score final.

    Metodos
    -------
    separarLetras(sequencia)
        Tem como funcionalidade pegar uma string e transformar cada caracter
        em uma lista.
    salvarImage()
        Criar a imagem utilizando as ferramentas da biblioteca matplotlib.
    """
    def __init__(self, path, seq1, seq2, sym, ident, score):
        self.path = path
        self.seq1 = seq1
        self.seq2 = seq2
        self.sym = sym
        self.ident = ident
        self.score = score

    def separarLetras(self, sequencia):
        """

        Transformando uma string em lista.

        Parametros:
            sequencia (str): Uma string contendo um tipo de sequencia do resultado
            do alinhamento.

        Retorno:
            A sequencia do resultado do alinhamento só que em formato de LISTA.

        """
        lista = []
        for letra in sequencia:
            lista.append(letra)
        return lista

    def salvarImage(self):
        """

        Cria uma imagem a partir das duas listas, que contem os alinhamentos,
        utilizando as ferramentas da biblioteca do matplotlib.

        --> Função usada no GeMapCom.py

        """
        x_axis = range(len(self.seq1))
        x_axix_legenda = self.separarLetras(self.seq1)
        x2_axis = range(len(self.seq2))
        x2_axix_legenda = self.separarLetras(self.seq2)
        resposta = self.separarLetras(self.sym)

        w = int(np.max([len(self.seq1), len(self.seq2)])/2)

        figure(num=None, figsize=(w, 8), dpi=80, facecolor='w', edgecolor='k')
        index = 0
        tamanhoAxis = len(x_axis)
        plt.xticks(range(tamanhoAxis + 2))
        plt.text(0.9, 0.65, "Sequência 1:", fontsize=15)
        plt.text(0.9, 0.25, "Sequência 2:", fontsize=15)
        for posi in range(0, tamanhoAxis):
            if self.seq1[posi] == self.seq2[posi]:
                plt.text(posi+1, 0.55, self.seq1[index], fontsize=20, bbox=dict(facecolor='green', alpha=0.5))
                plt.text(posi+1, 0.35, self.seq2[index], fontsize=20, bbox=dict(facecolor='green', alpha=0.5))
            else:
                plt.text(posi+1, 0.55, self.seq1[index], fontsize=20, bbox=dict(facecolor='red', alpha=0.5))
                plt.text(posi+1, 0.35, self.seq2[index], fontsize=20, bbox=dict(facecolor='red', alpha=0.5))
            index += 1
        plt.yticks([])
        plt.xticks([])
        texto_identidade = 'Identidade: '+ self.ident[:5]+'%'
        texto_score = 'Score: '+ self.score
        green_patch = mpatches.Patch(color='green', label='Match')
        red_patch = mpatches.Patch(color='red', label='Não Match')
        white_patch1 = mpatches.Patch(color='white', label=texto_identidade)
        white_patch2 = mpatches.Patch(color='white', label=texto_score)
        plt.legend(handles=[white_patch1, white_patch2, red_patch,green_patch], loc='upper left', prop={'size': 13})
        plt.savefig(self.path,bbox_inches='tight')
