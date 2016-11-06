import sys

codon = {'F':2,'L':6,'S':6,'Y':2,'C':2,'W':1,'P':4,'H':2,'Q':2,'R':6,'I':3,'M':1,'T':4,'N':2,'K':2,'V':4,'A':4,'D':2,'E':2,'G':4,'\n':1}

def read_file(filename):
	f = open(filename,'rU')
	protein = f.readline()
	output = 3
	for p in protein:
		output = (output*codon[p])%1000000
	print output

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
