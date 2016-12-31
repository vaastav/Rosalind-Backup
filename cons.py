import sys

A_count = []
C_count = []
G_count = []
T_count = []
maxList = ""
length = 0

def initializeArray():
	global A_count
	global C_count
	global G_count
	global T_count
	for i in range(1000):
		A_count += [0]
		C_count += [0]
		G_count += [0]
		T_count += [0]

def countPosition(dna):
	i = 0
	global A_count
	global C_count
	global G_count
	global T_count
	global length
	for base in dna:
		if base == 'A':
			A_count[i] += 1
		elif base == 'C':
			C_count[i] += 1
		elif base == 'G':
			G_count[i] += 1
		else:
			T_count[i] += 1

		i += 1

	length = i

def findMax(i):
	global A_count
	global C_count
	global G_count
	global T_count
	a = A_count[i]
	c = C_count[i]
	g = G_count[i]
	t = T_count[i]
	arr = [a,c,g,t]
	m = max(arr)
	if m == a:
		return 'A'
	elif m == c:
		return 'C'
	elif m == g:
		return 'G'
	else:
		return 'T'


def findConsensus():
	global A_count
	global maxList
	for i in range(length):
		char = findMax(i)
		maxList += char

def printMatrix():
	global A_count
	global C_count
	global G_count
	global T_count
	print("A: " + ' '.join(map(str, A_count[:length])))

	print("C: " + ' '.join(map(str, C_count[:length])))

	print("G: " + ' '.join(map(str, G_count[:length])))

	print("T: " + ' '.join(map(str, T_count[:length])))
		
def printConsensus():
	global maxList
	print(maxList)

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
