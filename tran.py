import sys

# Transtions : (A <-> G) and (C <-> T)

def calc_ratio(s1,s2):
	transitions = 0
	transversions = 0
	for a,b in zip(s1,s2):
		if a != b:
			if a == 'T' and b == 'C':
				transitions += 1
			elif a == 'C' and b == 'T':
				transitions += 1
			elif a == 'A' and b == 'G':
				transitions += 1
			elif a == 'G' and b == 'A':
				transitions += 1
			else:
				transversions += 1

	return transitions/transversions

def readFile(filename):
	inf = open(filename,'rU')
	name = ""
	dna = ""
	strings = []
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
	print(calc_ratio(strings[0],strings[1]))
		

def main():
	readFile(sys.argv[1])

if __name__ == '__main__':
	main()
