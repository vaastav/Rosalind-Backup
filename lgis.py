import sys

def find_dec_sequence(arr, sequence):
	seq = []
	max_value = max(arr)
	for i in range(len(arr)-1, -1, -1):
		if max_value == arr[i]:
			seq += [sequence[i]]
			max_value -= 1
	return seq[::-1]

def lis(n,sequence):
	lis = [1]*n
	p = [-1] * n

	for i in range(1, n):
		for j in range(0, i):
			if sequence[i] > sequence[j] and lis[i] < lis[j] + 1:
				lis[i] = lis[j] + 1
				p[i] = j

	ans = lis[0]
	pos = 0
	for i in range (1, n):
		if lis[i] > ans:
			ans = lis[i]
			pos = i
	subseq = []
	while pos != -1:
		subseq += [sequence[pos]]
		pos = p[pos]
	return subseq[::-1]

def lds(n,sequence):
	lds = [1]*n

	for i in range(1, n):
		for j in range(0,i):
			if sequence [i] < sequence[j] and lds[i] < lds[j] + 1:
				lds[i] = lds[j] + 1

	return find_dec_sequence(lds,sequence)

def readFile(filename):
	inf = open(filename,'r')
	n = int(inf.readline().strip())
	sequence = inf.readline().strip().split(' ')
	sequence = [int(s) for s in sequence]
	print(' '.join([str(s) for s in lis(n,sequence)]))
	print(' '.join([str(s) for s in lds(n,sequence)]))

def main():
	readFile(sys.argv[1])

if __name__ == '__main__':
	main()
