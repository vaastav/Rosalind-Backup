import sys
from pprint import pprint

strings = {}

def read_file(filename):
	inf = open(filename,'rU')
	name = ''
	protein = ''
	for line in inf:
		line = line.strip()
		if line[0] == '>':
			if name != '':
				strings[name] = protein
			name = line[1:]
			protein = ''
		else:
			protein += line
	strings[name] = protein

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
