RNA_TRANSCRIPTION = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U'
}


def to_rna(dna_strand):
    return ''.join(
        [RNA_TRANSCRIPTION[nucleotide] for nucleotide in dna_strand])
