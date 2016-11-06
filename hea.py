import sys

def swap_down(arr,i,size):
	leftchild = (2*i) + 1
	rightchild = (2*i) + 2
	mi = i
	if leftchild < size and arr[leftchild] > arr[mi]:
		mi = leftchild
	if rightchild < size and arr[rightchild] > arr[mi]:
		mi = rightchild
	
	if mi != i:
		t = arr[i]
		arr[i] = arr[mi]
		arr[mi] = t
		swap_down(arr,mi,size)

def heapify(arr,size):
	last_parent = (size-2)/2
	i = last_parent
	while i >= 0:
		swap_down(arr,i,size)
		i -= 1
	outf = open('outputhea.txt','w')
	for a in arr:
		outf.write(str(a) + ' ')

def read_file(filename):
	inf = open(filename,'rU')
	size = int(inf.readline())
	l = inf.readline().split(' ')
	arr = []
	for s in l:
		arr += [int(s)]
	
	heapify(arr,size)

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
