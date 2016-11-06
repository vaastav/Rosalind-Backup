import sys

def fib(n):
	if n < 2:
		return n
	else:
		return fib(n-1) + fib(n-2)


def read_file(filename):
	inf = open(filename,'rU')
	n = int(inf.readline())
	print fib(n)

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
