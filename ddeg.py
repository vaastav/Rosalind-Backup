import sys
from collections import defaultdict

graph = defaultdict(list)
count = {}

def readFile(filename):
	inf = open(filename,'rU')
	size = inf.readline().split(' ')
	n = int(size[0])
	m = int(size[1])
	for i in range(1,n+1):
		graph[i] = []
	for line in inf:
		pair = line.split(' ')
		a = int(pair[0])
		b = int(pair[1])
		graph[a].append(b)
		graph[b].append(a)

	for key in graph:
		count[key] = 0
		for values in graph[key]: 
			count[key] += len(graph[values])
	
	for i in range(1,len(count)+1):
		print str(count[i]),


def main():
	readFile(sys.argv[1])

if __name__ == '__main__':
	main()
