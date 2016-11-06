import sys
import itertools
import math

def read_file(filename):
	inf = open(filename,'rU')
	n = int(inf.readline())
	l = itertools.permutations([i for i in range(n)])
	outf = open('outputperm.txt','w')
	f = math.factorial(n)
	outf.write(str(f) + '\n')	
	for i in l:
		a,b,c,d,e,f = i
		outf.write(str(a+1) + ' ' +  str(b+1) + ' ' + str(c+1) + ' ' + str(d+1) + ' ' + str(e+1) + ' ' + str(f+1) + '\n')


def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
