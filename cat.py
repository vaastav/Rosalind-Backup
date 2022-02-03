import sys

def catalan(n):
    if (n == 0 or n == 1):
        return 1
 
    # Table to store results of subproblems
    catalan =[0]*(n+1)
 
    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1
 
    # Fill entries in catalan[]
    # using recursive formula
    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j]* catalan[i-j-1]
 
    # Return last entry
    return catalan[n]

def readFile(filename):
    with open(filename, "r") as inf:
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
        print((catalan(au_count) * catalan(gc_count)) % 1000000)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()