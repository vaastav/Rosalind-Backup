import sys

def readFile(filename):
    with open(filename, 'r') as inf:
        count = 0
        dna = ""
        for line in inf.readlines():
            if count > 0:
                dna += line.strip()
            count += 1
        arr = [0] * (len(dna) + 1)
        i = 0
        j = -1
        arr[i] = j
        while i < len(dna):
            while j >= 0 and dna[i] != dna[j]:
                j = arr[j]
            i += 1
            j += 1
            arr[i] = j
        print(' '.join([str(a) for a in arr[1:]]))

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()