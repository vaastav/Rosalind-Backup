import sys

def merge(arr1,arr2,s1,s2):
	i = 0
	j = 0
	arr3 = []
	while i < s1 and j <s2:
		if arr1[i] < arr2[j]:
			arr3 += [arr1[i]]
			i += 1
		else:
			arr3 += [arr2[j]]
			j += 1
	while i < s1:
		arr3 += [arr1[i]]
		i += 1
	while j < s2:
		arr3 += [arr2[j]]
		j += 1
	
	outf = open('outputmer.txt','w')
	for a in arr3:
		outf.write(str(a) + ' ')

def read_file(filename):
	inf = open(filename,'rU')
	s1 = int(inf.readline())
	l = inf.readline().split(' ')
	arr1 = []
	for s in l:
		arr1 += [int(s)]
	s2 = int(inf.readline())
	l = inf.readline().split(' ')
	arr2 = []
	for s in l:
		arr2 += [int(s)]
	merge(arr1,arr2,s1,s2)


def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
