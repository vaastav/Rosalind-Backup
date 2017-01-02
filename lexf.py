import sys
import itertools

def enum(alphabet,n):
	

def readFile(filename):
	inf = open(filename,'rU')
	line = inf.readline()
	line = line.strip()
	alphabet = line.split(' ')
	line = inf.readline()
	line = line.strip()
	n = int(line)
	enum(alphabet,n)

def main():
	readFile(sys.argv[1])

if __name__ == '__main__':
	main()
