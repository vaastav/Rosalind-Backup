import sys

def read_file(filename):
	f = open(filename,'rU')
	line = f.readline()
	words = dict()
	outf = open('output6.txt','w')
	for word in line.split(' '):
		if word in words:
			words[word] += 1
		else:
			words[word] = 1
	for key, value in words.items():
		outf.write(key + ' ' + str(value) + '\n')

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
