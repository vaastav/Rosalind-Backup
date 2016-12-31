import sys

strings = []

def lcs(strings):
	substr = ''
	if len(strings) > 1 and len(strings[0]) > 0:
		for i in range(len(strings[0])):
			for j in range(len(strings[0]) - i + 1):
					if j > len(substr) and all(strings[0][i:i+j] in x for x in strings):
						substr = strings[0][i:i+j]

	return substr

def read_file(filename):
	inf = open(filename,'rU')
	name = ''
	protein = ''
	global strings
	for line in inf:
		line = line.strip()
		if line[0] == '>':
			if name != '':
				strings += [protein]
			name = line[1:]
			protein = ''
		else:
			protein += line
	strings += [protein]
	print(lcs(strings))

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
