import sys

def dist_matrix(dnas):
    matrix = []
    for d in dnas:
        arr = []
        for d2 in dnas:
            mismatch = 0
            for i in range(len(d)):
                if d[i] != d2[i]:
                    mismatch += 1
            arr += [mismatch/len(d)]
        matrix += [arr]
    for arr in matrix:
        print(' '.join([str(round(a, 4)) for a in arr]))

def readFile(filename):
    with open(filename, 'r') as inf:
        dnas = []
        dna = ""
        for line in inf.readlines():
            line = line.strip()
            if line[0] == '>':
                if dna != "":
                    dnas += [dna]
                dna = ""
            else:
                dna += line
        dnas += [dna]
        dist_matrix(dnas)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()