import sys

def read_file(filename):
	f = open(filename, 'rU')
	line = f.readline()
	genes = dict([('A',0), ('C',0), ('G',0), ('T',0)])
	for i in list(line):
		if i == 'A':
			genes['A'] += 1
		elif i == 'C':
			genes['C'] += 1
		elif i == 'G':
			genes['G'] += 1
		elif i == 'T':
			genes['T'] += 1
	
	print str(genes['A']) + ' '
	print str(genes['C']) + ' '
	print str(genes['G']) + ' '
	print str(genes['T'])

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
