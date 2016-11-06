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
	
	outf = open('outputprot.txt','w')
	outf.write(protein)
	
def read_file(filename):
	inf = open(filename,'rU')
	find_protein(inf.readline())

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
