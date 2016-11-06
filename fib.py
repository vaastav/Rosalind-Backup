import sys

def fib(n,k):
	rab_array = []
	for i in range(n):
		if i < 2:
			rab_array += [1]
		else:
			rab_array.append(rab_array[-1] + rab_array[-2]*k)
	return rab_array

def read_file(filename):
	f = open(filename,'rU')
	n, k = f.readline().split(' ')
	print fib(int(n),int(k))[-1]

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
