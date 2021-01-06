import numpy as np

class algorithm_smith:

    def __init__(self, s1, s2, match, mismatch, gap):
        self.s1 = s1
        self.s2 = s2
        self.pt_waterman = {'match': match, 'mismatch': mismatch, 'gap': gap}
        self.identity = None
        self.max_score = None
        self.align1 = ''
        self.sym = ''
        self.align2 = ''

    def mch(self, alpha, beta):
        if alpha == beta:
            return self.pt_waterman['match']
        elif alpha == '-' or beta == '-':
            return self.pt_waterman['gap']
        else:
            return self.pt_waterman['mismatch']

    def water(self):
        m, n = len(self.s1), len(self.s2)
        H = np.zeros((m + 1, n + 1))
        T = np.zeros((m + 1, n + 1))
        self.max_score = 0
        # Score, Pointer Matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                sc_diag = H[i - 1][j - 1] + self.mch(self.s1[i - 1], self.s2[j - 1])
                sc_up = H[i][j - 1] + self.pt_waterman['gap']
                sc_left = H[i - 1][j] + self.pt_waterman['gap']
                H[i][j] = max(0, sc_left, sc_up, sc_diag)
                if H[i][j] == 0: T[i][j] = 0
                if H[i][j] == sc_left: T[i][j] = 1
                if H[i][j] == sc_up: T[i][j] = 2
                if H[i][j] == sc_diag: T[i][j] = 3
                if H[i][j] >= self.max_score:
                    max_i = i
                    max_j = j
                    self.max_score = H[i][j]

        # print('H=\n', H, '\n')
        # print('T=\n', T, '\n')
        self.align1, self.align2 = '', ''
        i, j = max_i, max_j

        # Traceback
        while T[i][j] != 0:
            if T[i][j] == 3:
                a1 = self.s1[i - 1]
                a2 = self.s2[j - 1]
                i -= 1
                j -= 1
            elif T[i][j] == 2:
                a1 = '-'
                a2 = self.s2[j - 1]
                j -= 1
            elif T[i][j] == 1:
                a1 = self.s1[i - 1]
                a2 = '-'
                i -= 1
            # print('%s ---> a1 = %s\t a2 = %s\n' % ('Add', a1, a2))
            self.align1 += a1
            self.align2 += a2

        self.align1 = self.align1[::-1]
        self.align2 = self.align2[::-1]
        self.sym = ''
        iden = 0
        for i in range(len(self.align1)):
            a1 = self.align1[i]
            a2 = self.align2[i]
            if a1 == a2:
                self.sym += a1
                iden += 1
            elif a1 != a2 and a1 != '-' and a2 != '-':
                self.sym += ' '
            elif a1 == '-' or a2 == '-':
                self.sym += ' '

        self.identity = iden / len(self.align1) * 100
        # print('Identity = %2.1f percent' % self.identity)
        # print('Score = %d' % self.max_score)
        # print(self.align1)
        # print(self.sym)
        # print(self.align2)

# if __name__ == '__main__':
#     # a = algorithm_smith("AGCACACA","ACACACTA", 2, -1, -1)
#     a = algorithm_smith("GGAT","GAT", 1, -1, -1)
#     a.water()