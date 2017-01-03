import sys
import itertools

def combs(alphabet,n,res,acc=''):
	if n == 0:
		res.append(acc)
	else:
		for c in alphabet:
			combs(alphabet,n-1,res,acc + c)
	return res
	

def readFile(filename):
	inf = open(filename,'rU')
	line = inf.readline()
	line = line.strip()
	alphabet = line.split(' ')
	line = inf.readline()
	line = line.strip()
	n = int(line)
	res = []
	res = combs(alphabet,n,res)
	for r in res:
		print(r)

def main():
	readFile(sys.argv[1])

if __name__ == '__main__':
	main()
