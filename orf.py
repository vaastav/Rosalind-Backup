import sys
from prot import proteins, my_range

def revc(rna):
    string = ''
    for gene in list(rna):
        if gene == 'A':
            string += 'T'
        elif gene == 'T':
            string += 'A'
        elif gene == 'C':
            string += 'G'
        elif gene == 'G':
            string += 'C'
    return string[::-1]

def readFile(filename):
    with open(filename, 'r') as inf:
        lines = []
        dna = ""
        count = 0
        for line in inf.readlines():
            if count > 0:
                dna += line.strip()
            count += 1
        rna = dna.replace('T', 'U')
        START = 'AUG'
        rev_dna = revc(dna)
        rev_rna = rev_dna.replace('T', 'U')
        lop = set()
        list_of_rnas = []
        for i in range(len(rna)):
            codon = rna[i:i+3]
            if codon == START:
                list_of_rnas += [rna[i:]]
        for i in range(len(rev_rna)):
            codon = rev_rna[i:i+3]
            if codon == START:
                list_of_rnas += [rev_rna[i:]]
        for orf in list_of_rnas:
            has_started = False
            has_stopped = False
            protein = ""
            codons = []
            for x in my_range(0, len(orf), 3):
                codon = orf[x:x+3]
                if len(codon) < 3:
                    continue
                if has_started:
                    if proteins[codon] == 'Stop':
                        has_stopped = True
                        break
                    protein += proteins[codon]
                    codons += [codon]
                elif codon == START:
                    has_started = True
                    protein += proteins[codon]
                    codons += [codon]
            if protein != "" and has_stopped:
                lop.add(protein)
        for protein in lop:
            print(protein) 

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()