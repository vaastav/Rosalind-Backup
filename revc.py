import sys

def read_file(filename):
	inf = open(filename,'rU')
	outf = open('outputRevc.txt','w')
	line = inf.readline()
	string = ''
	for gene in list(line):
		if gene == 'A':
			string += 'T'
		elif gene == 'T':
			string += 'A'
		elif gene == 'C':
			string += 'G'
		elif gene == 'G':
			string += 'C'
	
	outf.write(string[::-1])

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
