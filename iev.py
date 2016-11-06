from __future__ import division
import sys

def read_file(filename):
	f = open(filename,'rU')
	line = f.readline().split(' ')
	prob = [1.0,1.0,1.0,0.75,0.5,0.0]
	expect = 0.0
	for i in range(6):
		expect += int(line[i])*prob[i]*2
	print expect


def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
