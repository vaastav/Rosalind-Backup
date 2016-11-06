import sys

def insertion_sort(n,a):
	count = 0
	for i in range(n):
		k = i
		while k > 0 and a[k] < a[k-1]:
			tmp = a[k-1]
			a[k-1] = a[k]
			a[k] = tmp
			k -= 1
			count += 1
	
	print count

def read_file(filename):
	inf = open(filename,'rU')
	size = int(inf.readline())
	l = inf.readline().split(' ')
	arr = []
	for s in l:
		arr += [int(s)]
	insertion_sort(size,arr)

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
