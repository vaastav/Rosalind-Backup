import sys

def binary(A,key,first,last):
	if first > last:
		return -1
	mid = int((first + last)/2)
	if A[mid] == key:
		return mid
	else:
		if key > A[mid]:
			return binary(A,key,mid+1,last)
		elif key < A[mid]:
			return binary(A,key,first,mid-1)


def readFile(filename):
	inf = open(filename,'rU')
	A = []
	K = []
	indices = []
	n = int(inf.readline())
	m = int(inf.readline())
	line = inf.readline().split(' ')
	for num in line:
		A += [int(num)]
	line = inf.readline().split(' ')
	for num in line:
		K += [int(num)]
	for key in K:
		result = binary(A,key,0,n-1)
		if result != -1:
			indices += [result + 1]
		else:
			indices += [result]
	print(' '.join(map(str,indices)))

def main():
	readFile(sys.argv[1])

if __name__ == '__main__':
	main()
