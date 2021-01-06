import numpy as np
import threading
import time

class algorithm_needleman:

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
        if alpha == beta:
            return self.pt_wunsch['match']
        elif alpha == '-' or beta == '-':
            return self.pt_wunsch['gap']
        else:
            return self.pt_wunsch['mismatch']

    def funcaoFor(self, i, n):
        for j in range(1, n+1):
            diag = self.score[i - 1][j - 1] + self.mach(self.s1[i - 1], self.s2[j - 1])
            delete = self.score[i - 1][j] + self.pt_wunsch['gap']
            insert = self.score[i][j - 1] + self.pt_wunsch['gap']
            valor=max(diag, delete, insert)
            self.score[i][j] = valor

    def Traceback(self, i, j):
        while i > 0 and j > 0:
            score_current = self.score[i][j]
            score_diag = self.score[i - 1][j - 1]
            score_left = self.score[i][j - 1]
            score_up = self.score[i - 1][j]

            print('score_current: ', score_current)
            print('score_diag: ', score_diag)
            print('score_left: ', score_left)
            print('score_up: ', score_up)

            if score_current == score_diag + self.mach(self.s1[i - 1], self.s2[j - 1]):
                print('diag')
                a1, a2 = self.s1[i - 1], self.s2[j - 1]
                i, j = i - 1, j - 1
            elif score_current == score_up + self.pt_wunsch['gap']:
                print('up')
                a1, a2 = self.s1[i - 1], '-'
                i -= 1
            elif score_current == score_left + self.pt_wunsch['gap']:
                print('left')
                a1, a2 = '-', self.s2[j - 1]
                j -= 1
            print('%s ---> a1 = %s\t a2 = %s\n' % ('Add', a1, a2))
            self.align1 += a1
            self.align2 += a2

        while i > 0:
            a1, a2 = self.s1[i - 1], '-'
            print('%s ---> a1 = %s\t a2 = %s\n' % ('Add', a1, a2))
            self.align1 += a1
            self.align2 += a2
            i -= 1

        while j > 0:
            a1, a2 = '-', self.s2[j - 1]
            print('%s --> a1 = %s\t a2 = %s\n' % ('Add', a1, a2))
            self.align1 += a1
            self.align2 += a2
            j -= 1
            
    def concatenarStrings(self):
        self.seqN = len(self.align1)
        for i in range(self.seqN):
            a1 = self.align1[i]
            a2 = self.align2[i]
            if a1 == a2:
                self.sym += a1
                self.ident += 1
                self.seq_score += self.mach(a1, a2)

            else:
                self.seq_score += self.mach(a1, a2)
                self.sym += ' '

    def needle(self):
        m, n = len(self.s1), len(self.s2)
        self.score = np.zeros((m + 1, n + 1))

        # Initialization
        for i in range(m + 1):
            self.score[i][0] = self.pt_wunsch['gap'] * i
        for j in range(n + 1):
            self.score[0][j] = self.pt_wunsch['gap'] * j

        # Fill
        lista = []
        print('Preparando Threads')
        for i in range(1, m + 1):
            lista.append(threading.Thread(target=self.funcaoFor, args=(i, n)))
        print('Iniciando Tarefas')
        for index, item in enumerate(lista):
            print('\r Thread: '+ str(index), end='')
            item.start()
        print()
        vivo = True
        tamanhoLista = len(lista)
        contador = 0
        print('AGUARDE\n')
        while vivo:
            cont = 0
            for item in lista:
                if not item.is_alive():
                    cont += 1
            print('\rMortos: '+str(cont)+'/'+str(tamanhoLista), end='')
            if cont == tamanhoLista:
                vivo = False
            else:
                time.sleep(1)
            contador += 1

        # print('score matrix = \n%s\n' % self.score)
        self.align1, self.align2 = '', ''
        i, j = m, n

        # Traceback
        print('\n\nIniciando Traceback\n')        
        traceback = threading.Thread(target=self.Traceback,args=(i,j))
        traceback.start()

        espera = 1
        
        while espera:
            if traceback.is_alive():
                time.sleep(1)
            else:
                espera = 0
        
        print('\n\nIniciando cancatenação de sequencias: ')

        self.align1 = self.align1[::-1]
        self.align2 = self.align2[::-1]
        #seqN = len(self.align1)
        self.sym = ''
        self.seq_score = 0
        self.ident = 0
        
        concatenagem = threading.Thread(target=self.concatenarStrings)
        concatenagem.start()

        espera = 1
        
        while espera:
            if concatenagem.is_alive():
                time.sleep(1)
            else:
                espera = 0

        # while i > 0 and j > 0:
        #     score_current = self.score[i][j]
        #     score_diag = self.score[i - 1][j - 1]
        #     score_left = self.score[i][j - 1]
        #     score_up = self.score[i - 1][j]

        #     print('score_current: ', score_current)
        #     print('score_diag: ', score_diag)
        #     print('score_left: ', score_left)
        #     print('score_up: ', score_up)

        #     if score_current == score_diag + self.mach(self.s1[i - 1], self.s2[j - 1]):
        #         print('diag')
        #         a1, a2 = self.s1[i - 1], self.s2[j - 1]
        #         i, j = i - 1, j - 1
        #     elif score_current == score_up + self.pt_wunsch['gap']:
        #         print('up')
        #         a1, a2 = self.s1[i - 1], '-'
        #         i -= 1
        #     elif score_current == score_left + self.pt_wunsch['gap']:
        #         print('left')
        #         a1, a2 = '-', self.s2[j - 1]
        #         j -= 1
        #     print('%s ---> a1 = %s\t a2 = %s\n' % ('Add', a1, a2))
        #     self.align1 += a1
        #     self.align2 += a2

        # while i > 0:
        #     a1, a2 = self.s1[i - 1], '-'
        #     print('%s ---> a1 = %s\t a2 = %s\n' % ('Add', a1, a2))
        #     self.align1 += a1
        #     self.align2 += a2
        #     i -= 1

        # while j > 0:
        #     a1, a2 = '-', self.s2[j - 1]
        #     print('%s --> a1 = %s\t a2 = %s\n' % ('Add', a1, a2))
        #     self.align1 += a1
        #     self.align2 += a2
        #     j -= 1

        # self.align1 = self.align1[::-1]
        # self.align2 = self.align2[::-1]
        # seqN = len(self.align1)
        # self.sym = ''
        # self.seq_score = 0
        # self.ident = 0
        # for i in range(seqN):
        #     a1 = self.align1[i]
        #     a2 = self.align2[i]
        #     if a1 == a2:
        #         self.sym += a1
        #         self.ident += 1
        #         self.seq_score += self.mach(a1, a2)

        #     else:
        #         self.seq_score += self.mach(a1, a2)
        #         self.sym += ' '

        self.ident = self.ident / self.seqN * 100

        print()

        print('Identity = %2.1f percent' % self.ident)
        print('Score = %d\n' % self.seq_score)

        #print(self.align1)
        #print(self.sym)
        #print(self.align2)

def ler_fasta(arquivo):
    sequencia = ''
    lista = []
    with open(arquivo, 'r') as fasta:
        sequencia = ''
        for linha in fasta:
            if not linha.startswith('>'):
            #if not linha.find('>'):
                sequencia += linha.strip()
        lista.append(sequencia)

    return lista

if __name__ == '__main__':
    # lista1 = ler_fasta("Mus_musculus.GRCm38.dna.chromosome.1.fa")
    # lista2 = ler_fasta("Mus_musculus.GRCm38.dna.chromosome.1.fa")
    
    lista1 = ler_fasta("r1.fasta")
    lista2 = ler_fasta("r2.fasta")

    string1 = (str(lista1))
    string2 = (str(lista2))
    string1 = string1[2:-2]
    # print(len(string1))
    string2 = string2[2:-2]
    # print(len(string1))

    # print(string1)
    # print(string2)

    # a = algorithm_needleman("TTCATA","TGCTCGTA", 5, -2, -6)
    a = algorithm_needleman(string1, string2, 5, -2, -6)
    a.needle()