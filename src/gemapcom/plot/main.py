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
        String contendo a simbologia de alinhamento.
    ident : str
        String contendo o valor da identidade final.
    score : str
        String contendo o valor do score final.
    """
    def __init__(self, path: str, seq1: str, seq2: str, sym: str, ident: str, score: str):
        self.path = path
        self.seq1 = seq1
        self.seq2 = seq2
        self.sym = sym
        self.ident = ident
        self.score = score

    def salvarImage(self) -> None:
        """
        Cria uma imagem a partir das duas listas, que contem os alinhamentos,
        utilizando as ferramentas da biblioteca do matplotlib.

        --> Função usada no GeMapCom.py
        """
        x_axis = range(len(self.seq1))
        
        w = int(np.max([len(self.seq1), len(self.seq2)]) / 2)
        w = max(w, 8)

        figure(num=None, figsize=(w, 8), dpi=80, facecolor='w', edgecolor='k')
        tamanhoAxis = len(x_axis)
        
        plt.title("Resultado do Alinhamento", fontsize=20, pad=20)
        plt.xticks(range(tamanhoAxis + 2))
        plt.text(0.9, 0.65, "Sequência 1:", fontsize=15)
        plt.text(0.9, 0.25, "Sequência 2:", fontsize=15)
        
        for posi in range(tamanhoAxis):
            char1 = self.seq1[posi]
            char2 = self.seq2[posi]
            if char1 == char2 and char1 != '-':
                bg_color = 'lightgreen'
            else:
                bg_color = 'salmon'
                
            plt.text(posi + 1, 0.55, char1, fontsize=20, bbox=dict(facecolor=bg_color, alpha=0.7))
            plt.text(posi + 1, 0.35, char2, fontsize=20, bbox=dict(facecolor=bg_color, alpha=0.7))
            
        plt.yticks([])
        plt.xticks([])
        
        texto_identidade = f'Identidade: {self.ident[:5]}%'
        texto_score = f'Score: {self.score}'
        
        green_patch = mpatches.Patch(color='lightgreen', label='Match')
        red_patch = mpatches.Patch(color='salmon', label='Não Match / Gap')
        white_patch1 = mpatches.Patch(color='white', label=texto_identidade)
        white_patch2 = mpatches.Patch(color='white', label=texto_score)
        
        plt.legend(handles=[white_patch1, white_patch2, red_patch, green_patch], loc='upper left', prop={'size': 13})
        plt.savefig(self.path, bbox_inches='tight')
        plt.close('all')
