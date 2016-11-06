import sys

def sub(string,a,b):
	print string[a:b]

def read_file(filename):
	f = open(filename, 'rU')
	inp = f.readline()
	sub(inp,int(sys.argv[2]),int(sys.argv[3]) + 1)
	f.close()

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
