import sys

def read_file(filename):
	linenum = 1
	f = open(filename,'rU')
	outf = open('output.txt','w')
	for line in f:
		if(linenum % 2 == 0):
			outf.write(line)
		linenum += 1


def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
