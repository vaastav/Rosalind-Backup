import sys

proteins = {'UUU' : 'F','UUC' : 'F','UUA' : 'L','UUG' : 'L','UCU' : 'S','UCC' : 'S','UCA' : 'S','UCG':'S','UAU' : 'Y','UAC' : 'Y','UAA' : 'Stop','UAG' : 'Stop', 'UGU' : 'C', 'UGC' : 'C', 'UGA' : 'Stop','UGG' : 'W','CUU' : 'L','CUC' : 'L', 'CUA' : 'L', 'CUG' : 'L', 'CCU' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 'CAU' : 'H','CAC' : 'H', 'CAA' : 'Q', 'CAG' : 'Q', 'CGU' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R', 'AUU' : 'I', 'AUC' : 'I', 'AUA' : 'I','AUG' : 'M','ACU' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T','AAU' : 'N', 'AAC' : 'N', 'AAA' : 'K', 'AAG' : 'K', 'AGU' : 'S', 'AGC' : 'S','AGA' : 'R', 'AGG' : 'R', 'GUU' : 'V', 'GUC' : 'V', 'GUA' : 'V', 'GUG' : 'V','GCU' : 'A', 'GCC' : 'A','GCA' : 'A', 'GCG' : 'A', 'GAU' : 'D', 'GAC' : 'D', 'GAA' : 'E', 'GAG' : 'E','GGU' : 'G','GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G'}

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step


def find_protein(line):
	protein = ''
	for x in my_range(0,len(line),3):
		codon = line[x:x+3]
		if proteins[codon] == 'Stop':
			break
		protein += proteins[codon] 
	return protein	

def remove_introns(s,introns):
	for intron in introns:
		s = s.replace(intron,'')
	return s

def readFile(filename):
	strings = []
	inf = open(filename,'rU')
	name = ""
	dna = ""
	for line in inf:
		line = line.strip()
		if line[0] == '>':
			if name != "" :
				strings += [dna]
			name = line[1:]
			dna = ""
		else:
			dna += line
	strings += [dna]
	dna_string = strings[0]
	introns = strings[1:]
	dna_string = remove_introns(dna_string,introns)
	dna_string = dna_string.replace('T','U')
	print(find_protein(dna_string))

def main():
	readFile(sys.argv[1])

if __name__ == '__main__':
	main()
