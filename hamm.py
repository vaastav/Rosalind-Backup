import sys

def hamm(s1,s2):
	count = 0
	for a,b in zip(s1,s2):
		if a != b:
			count += 1
	
	print count

def read_file(filename):
	inf = open(filename,'rU')
	s1 = inf.readline()
	s2 = inf.readline()
	hamm(s1,s2)

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
