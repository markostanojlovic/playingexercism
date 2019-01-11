from enum import Enum

class ProteinsPool(Enum):
    Methionine = ('AUG')
    Phenylalanine = {'UUU','UUC'}
    Leucine = {'UUA', 'UUG'}
    Serine = {'UCU', 'UCC', 'UCA', 'UCG'}
    Tyrosine = {'UAU', 'UAC'}
    Cysteine = {'UGU', 'UGC'}
    Tryptophan = {'UGG'}
    STOP = {'UAA', 'UAG', 'UGA'}

def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    proteins = []
    for codon in codons:
        p = next(i.name for i in ProteinsPool if codon in i.value)
        if 'STOP' == p:
            return proteins
        else:
            proteins.append(p)
    return proteins
