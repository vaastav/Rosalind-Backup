import sys

strings = {}
graph = {}

def build_graph():
	global strings
	global graph
	for k1,v1 in strings.items():
		for k2,v2 in strings.items():
			if k1 != k2 :
				if v1[len(v1)-3:] == v2[:3]:
					graph[k1] += [k2]


def readFile(filename):
	global strings
	global graph
	inf = open(filename,'rU')
	name = ""
	dna = ""
	for line in inf:
		line = line.strip()
		if line[0] == '>':
			if name != "":
				strings[name] = dna
				graph[name] = []
			name = line[1:]
			dna = ""
		else:
			dna += line
	strings[name] = dna
	graph[name] = []
	build_graph()
	for key,val in graph.items():
		for v in val:
			print(key + " " + v)

def main():
	readFile(sys.argv[1])

if __name__ == '__main__':
	main()
