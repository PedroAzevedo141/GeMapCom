from Bio import Align

class algorithm_smith:
    """
    Classe para realizar o alinhamento local de Smith-Waterman
    utilizando a biblioteca Biopython.
    """
    def __init__(self, s1: str, s2: str, match: float, mismatch: float, gap: float):
        self.s1 = s1
        self.s2 = s2
        self.match = match
        self.mismatch = mismatch
        self.gap = gap
        self.align1 = ""
        self.align2 = ""
        self.sym = ""
        self.identity = 0.0
        self.max_score = 0.0

    def water(self) -> None:
        """
        Executa o alinhamento local.
        """
        aligner = Align.PairwiseAligner(mode='local')
        aligner.match_score = self.match
        aligner.mismatch_score = self.mismatch
        aligner.open_gap_score = self.gap
        aligner.extend_gap_score = self.gap

        alignments = aligner.align(self.s1, self.s2)
        try:
            best_alignment = next(alignments)
        except StopIteration:
            return
        self.max_score = best_alignment.score
        
        lines = best_alignment.format().split("\n")
        if len(lines) >= 3:
            self.align1 = lines[0]
            self.align2 = lines[2]

        matches = 0
        sym_list = []
        for a, b in zip(self.align1, self.align2):
            if a == b and a != "-":
                sym_list.append(a)
                matches += 1
            else:
                sym_list.append(" ")
        
        self.sym = "".join(sym_list)
        length = len(self.align1)
        self.identity = (matches / length) * 100 if length > 0 else 0.0
