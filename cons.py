import sys

A_count = []
C_count = []
G_count = []
T_count = []
maxList = ""

def initializeArray():
	for i in range(1000):
		A_count[i] = 0
		C_count[i] = 0
		G_count[i] = 0
		T_count[i] = 0

def countPosition(dna):
	i = 0
	for base in dna:
		if base == 'A':
			A_count[i] += 1
		elif base == 'C':
			C_count[i] += 1
		elif base == 'G':
			G_count[i] += 1
		else:
			T_count[i] += 1

def findConsensus():
	

def printMatrix():
	print "A: "
	for i in range(len(A_count)):
		print i
		
def printConsensus():
	print maxList

def readFile(filename):
	inf = open(filename,'rU')
	name = ""
	dna = ""
	initializeArray()
	for line in inf:
		line = line.strip()
		if line[0] == '>':
			if name != "" :
				countPosition(dna)
			name = line[1:]
			dna = ""
		else : 
			dna += line
	countPosition(dna)
	findConsensus()
	printMatrix()
	printConsensus()

def main():
	readFile(sys.argv[1])

if __name__ == '__main__':
	main()
