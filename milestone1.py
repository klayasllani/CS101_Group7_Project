#Module1
#By Klaybis Asllani
#Atlai Ortiz, Colin Zimmers, Jeremy Kelly

def dna_count(dna):
    dna = dna.upper()
    count_A = dna.count('A')
    count_C = dna.count('C')
    count_G = dna.count('G')
    count_T = dna.count('T')
    return [count_A,count_C,count_G,count_T]
    
def dna2rna(dna):
    rna = dna.upper()
    rna = rna.replace("T","U")
    return rna

def reverse_complement(dna):
    dna_rev = dna[::-1]
    rev_comp = '' 
    for symbol in dna_rev:
        if symbol == 'A':
            rev_comp = rev_comp + 'T'
        elif symbol == 'T':
            rev_comp = rev_comp + 'A'
        elif symbol == 'C':
            rev_comp = rev_comp + 'G'
        elif symbol == 'G':
            rev_comp = rev_comp + 'C'
    return rev_comp
# test cond: print(reverse_complement('AAAACCCGGT'))

def fibonacci_rabbits(n,k):
    f1,f2 = 1,1
    for i in range(n-1):
        f2,f1 = f1, f1 + (f2*k)
        #recursion by switching x1 and x2 results and multiplying the prior f2 by the k pairs produced
    return f2
    
def GC_content(dna_list):
    dna_list = dna_list.upper()
    highest_index = dna_list.find("GC") 
    percentage = (dna_list.count('G') + dna_list.count('C'))/len(dna_list)
    return (highest_index,percentage)
	
def rna2codon(rna):
    genetic_code = {
    'UUU': 'F',
    'CUU': 'L',
    'AUU': 'I',
    'GUU': 'V',
    'UUC': 'F',
    'CUC': 'L',
    'AUC': 'I',
    'GUC': 'V',
    'UUA': 'L',
    'CUA': 'L',
    'AUA': 'I',
    'GUA': 'V',
    'UUG': 'L',
    'CUG': 'L',
    'AUG': 'M',
    'GUG': 'V',
    'UCU': 'S',
    'CCU': 'P',
    'ACU': 'T',
    'GCU': 'A',
    'UCC': 'S',
    'CCC': 'P',
    'ACC': 'T',
    'GCC': 'A',
    'UCA': 'S',
    'CCA': 'P',
    'ACA': 'T',
    'GCA': 'A',
    'UCG': 'S',
    'CCG': 'P',
    'ACG': 'T',
    'GCG': 'A',
    'UAU': 'Y',
    'CAU': 'H',
    'AAU': 'N',
    'GAU': 'D',
    'UAC': 'Y',
    'CAC': 'H',
    'AAC': 'N',
    'GAC': 'D',
    'UAA': 'Stop',
    'CAA': 'Q',
    'AAA': 'K',
    'GAA': 'E',
    'UAG': 'Stop',
    'CAG': 'Q',
    'AAG': 'K',
    'GAG': 'E',
    'UGU': 'C',
    'CGU': 'R',
    'AGU': 'S',
    'GGU': 'G',
    'UGC': 'C',
    'CGC': 'R',
    'AGC': 'S',
    'GGC': 'G',
    'UGA': 'Stop',
    'CGA': 'R',
    'AGA': 'R',
    'GGA': 'G',
    'UGG': 'W',
    'CGG': 'R',
    'AGG': 'R',
    'GGG': 'G'
    }
    amino = ''
    if rna in genetic_code:
        amino = genetic_code[rna]
    return amino

def hamming_dist(dna1, dna2):
    number_of_dif = 0
    i = 0
    while (i < len(dna1)):
        if  dna1[i] != dna2[i]:
            number_of_dif += 1
    i += 1
    return number_of_dif
    
def locate_substring(dna_snippet, dna):
    for i in dna:
       indexes = dna.find(dna_snippet)
    return indexes
    
def splice_rna(dna,intron_list):
    rna = dna2rna(dna)
    for i in range(0,len(intron_list)):
        rna = rna.replace(intron_list[i], '')
    return rna2codon(rna)
    
def count_dom_phenotype(genotypes):
    return 2*(genotypes[0]+genotypes[1]+genotypes[2]) + 1.5*(genotypes[3])+(genotypes[4])

def mendels_law(hom,het,rec):
    population = hom+het+rec 
    a = rec/population * (rec-1)/(population-1)
    b = 0.5*(rec/population)*(het/(population-1))
    c = 0.5*(het/population)*(rec/(population-1))
    d = 0.25*(het/population)*((het-1)/(population-1))
    probability = 1 - a - b - c - d
    return probability

def source_rna(protein):
        protein_count = {
    'F':2,
    'L':6,
    'S':6,
    'Y':2,
    'C':2,
    'W':1,
    'P':4,
    'H':2,
    'Q':2,
    'R':6,
    'I':3,
    'M':1,
    'T':4,
    'N':2,
    'K':2,
    'V':4,
    'A':4,
    'D':2,
    'E':2,
    'G':4
    }
        for character in protein:
            for i in range(len(protein)):
                result = 3
                results *= protein_count[protein[i]]
        return result
