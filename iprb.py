from __future__ import division
import sys


def read_file(filename):
	prob = {'x|a':1,'x|b':0.75,'x|d':1,'x|e':0.5,'x|f':1}
	f = open(filename,'rU')
	line = f.readline()
	char = line.split(' ')
	k = int(char[0])
	m = int(char[1])
	n = int(char[2])
	prob['a'] = (k*(k-1))/(k+m+n)/(k+m+n-1)
	prob['b'] = (m*(m-1))/(k+m+n)/(k+m+n-1)
	prob['d'] = 2*(k*n)/(k+m+n)/(k+m+n-1)
	prob['e'] = 2*(m*n)/(k+m+n)/(k+m+n-1)
	prob['f'] = 2*(k*m)/(k+m+n)/(k+m+n-1)
	p = prob['a']*prob['x|a'] + prob['b']*prob['x|b'] + prob['d']*prob['x|d']+prob['e']*prob['x|e'] + prob['f']*prob['x|f']
	print p

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
