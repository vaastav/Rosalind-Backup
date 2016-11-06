import sys

def read_file(filename):
	inf = open(filename,'rU')
	s = inf.readline()
	t = inf.readline()
	outf = open('outputsubs.txt','w')
	l = []
	k = len(t)
	for i in range(len(s)):
		if s[i:i+k] == t:
			l += [i+1]
	for i in l:
		outf.write(str(i) + ' ')

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
