import numpy as np

class algorithm_needleman:
    """
    Uma classe para representar o algoritmo de Needleman-Wunsch.

    ...

    Atributos
    ---------
    s1 : str
        String contendo a primeira sequencia inserida pelo usuario.
    s2 : str
        String contendo a segunda sequencia inserida pelo usuario.
    match : str
        Valor em String do Match dos genes.
    mismatch : str
        Valor em String do Mismatch dos genes.
    gap : str
        Valor em String do GAP dos genes.

    Metodos
    -------
    mach(alpha, beta):
        Verificador de valores da matriz dos genomas.
    needle():
        Realização das comparações dos genes (caracteres da string da sequencia) de forma global.
    """
    def __init__(self, s1, s2, match, mismatch, gap):
        self.s1 = s1
        self.s2 = s2
        self.pt_wunsch = {'match': match, 'mismatch': mismatch, 'gap': gap}
        self.ident = None
        self.seq_score = None
        self.align1 = ''
        self.sym = ''
        self.align2 = ''

    def mach(self, alpha, beta):
        """

        Funcionalidade de verificação do valor na matriz dos genomas.
        Condiz com seu percuso e assim descobre se é MATCH, MISMATCH ou GAP.

        Parametros:
            alpha (str): Recebe o GAP. (-)
            beta (str): Recebe o GAP. (-)

        Retorno:
            Serve para realizar a inicialização da matriz.

        """
        if alpha == beta:
            return self.pt_wunsch['match']
        elif alpha == '-' or beta == '-':
            return self.pt_wunsch['gap']
        else:
            return self.pt_wunsch['mismatch']

    def needle(self):
        """

        Realização das comparações, que tem por objetivo realizar o alinhamento
        global de duas seqüências impostas pelo usuario.

        """
        m, n = len(self.s1), len(self.s2)
        self.score = np.zeros((m + 1, n + 1))

        # Initialization
        for i in range(m + 1):
            self.score[i][0] = self.pt_wunsch['gap'] * i
        for j in range(n + 1):
           self. score[0][j] = self.pt_wunsch['gap'] * j

        # Fill
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                diag = self.score[i - 1][j - 1] + self.mach(self.s1[i - 1], self.s2[j - 1])
                delete = self.score[i - 1][j] + self.pt_wunsch['gap']
                insert = self.score[i][j - 1] + self.pt_wunsch['gap']
                self.score[i][j] = max(diag, delete, insert)

        self.align1, self.align2 = '', ''
        i, j = m, n

        # Traceback
        while i > 0 and j > 0:
            score_current = self.score[i][j]
            score_diag = self.score[i - 1][j - 1]
            score_left = self.score[i][j - 1]
            score_up = self.score[i - 1][j]

            if score_current == score_diag + self.mach(self.s1[i - 1], self.s2[j - 1]):
                a1, a2 = self.s1[i - 1], self.s2[j - 1]
                i, j = i - 1, j - 1
            elif score_current == score_up + self.pt_wunsch['gap']:
                a1, a2 = self.s1[i - 1], '-'
                i -= 1
            elif score_current == score_left + self.pt_wunsch['gap']:
                a1, a2 = '-', self.s2[j - 1]
                j -= 1
            self.align1 += a1
            self.align2 += a2

        while i > 0:
            a1, a2 = self.s1[i - 1], '-'
            self.align1 += a1
            self.align2 += a2
            i -= 1

        while j > 0:
            a1, a2 = '-', self.s2[j - 1]
            self.align1 += a1
            self.align2 += a2
            j -= 1

        self.align1 = self.align1[::-1]
        self.align2 = self.align2[::-1]
        seqN = len(self.align1)
        self.sym = ''
        self.seq_score = 0
        self.ident = 0
        for i in range(seqN):
            a1 = self.align1[i]
            a2 = self.align2[i]
            if a1 == a2:
                self.sym += a1
                self.ident += 1
                self.seq_score += self.mach(a1, a2)

            else:
                self.seq_score += self.mach(a1, a2)
                self.sym += ' '

        self.ident = self.ident / seqN * 100
