import sys

def read_file(filename):
	inf = open(filename,'rU')
	fn, fm = inf.readline().split(' ')
	n = int(fn)
	m = int(fm)
	a = {}
	for i in range(n):
		a[i] = 0
	for i in range(m):
		fx, fy = inf.readline().split(' ')
		x = int(fx)
		y = int(fy)
		a[x-1] += 1
		a[y-1] += 1
	outf = open('outputdeg.txt','w')
	for i in a:
		outf.write('%s ' % a[i])


def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
