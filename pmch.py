from math import factorial
import sys

def factorial(n):
    val = 1
    for i in range(1,n+1):
        val = val * i
    return val

def readFile(filename):
    with open(filename, 'r') as inf:
        l0 = inf.readline()
        dna = ""
        for line in inf.readlines():
            dna += line.strip()
        au_count = 0
        gc_count = 0
        for base in dna:
            if base == 'A':
                au_count += 1
            elif base == 'G':
                gc_count += 1
        print(factorial(au_count) * factorial(gc_count))

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()