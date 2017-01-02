import sys

def find_sequence(arr,sequence):
	seq = []
	print(arr)
	for i in range(len(arr)):
		if i == len(arr)-1:
			if arr[i] != arr[i-1]:
				seq += [sequence[i]]
		else:
			if arr[i+1] == arr[i] + 1:
				seq += [sequence[i]]

	return seq

def lis(n,sequence):
	lis = [1]*n

	for i in range(1, n):
		for j in range(0, i):
			if sequence[i] > sequence[j] and lis[i] < lis[j] + 1:
				lis[i] = lis[j] + 1

	return find_sequence(lis,sequence)

def lds(n,sequence):
	lds = [1]*n

	for i in range(1, n):
		for j in range(0,i):
			if sequence [i] < sequence[j] and lds[i] < lds[j] + 1:
				lds[i] = lds[j] + 1

	return find_sequence(lds,sequence)

def readFile(filename):
	inf = open(filename,'rU')
	n = int(inf.readline().strip())
	sequence = inf.readline().strip().split(' ')
	print(lis(n,sequence))
	print(lds(n,sequence))

def main():
	readFile(sys.argv[1])

if __name__ == '__main__':
	main()
