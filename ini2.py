import sys
import math

def calculate(a, b):
	print math.pow(a,2) + math.pow(b,2)

def main():
	calculate(float(sys.argv[1]),float(sys.argv[2]))

if __name__ == '__main__':
	main()
