import sys

def calculate(a,b):
	sum1 = 0
	for i in range(a,b+1):
		if(i%2 == 1):
			sum1 += i
	
	print sum1


def main():
	calculate(int(sys.argv[1]),int(sys.argv[2]))

if __name__ == '__main__' :
	main()
