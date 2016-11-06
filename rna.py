import sys

def read_file(filename):
	f = open(filename,'rU')
	line = f.readline()
	outf = open('outputRNA.txt','w')
	outf.write(line.replace('T','U'))

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
