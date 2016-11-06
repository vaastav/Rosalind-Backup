from __future__ import division
import sys
import math

def perm(n,k):
	f = math.factorial
	print f(n)/f(n-k) % 1000000
	

def read_file(filename):
	f = open(filename,'rU')
	line = f.readline().split(' ')
	n = line[0]
	k = line[1]
	perm(int(n),int(k))

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
