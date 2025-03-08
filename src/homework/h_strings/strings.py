def get_hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError("DNA sequences must be of equal length")
    
    hamming_distance= 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            hamming_distance += 1
    
    return hamming_distance

def get_dna_complement(dna):
    complement= ""

    for base in dna:
        if base == 'A':
             complement += 'T'
        elif base == 'T':
            complement += 'A'
        elif base == 'C':
            complement += 'G'
        elif base == 'G':
            complement += 'C'
        else:
             raise ValueError(f"Invalid DNA base: {base}")
    return complement
