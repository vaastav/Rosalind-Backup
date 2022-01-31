import sys

def get_revc(dna):
    complement = ""
    for char in dna:
        if char == 'G':
            complement += 'C'
        elif char == 'C':
            complement += 'G'
        elif char == 'A':
            complement += 'T'
        elif char == 'T':
            complement += 'A'
    return complement[::-1]

def readFile(filename):
    with open(filename, 'r') as inf:
        count = 0
        dna = ""
        for line in inf.readlines():
            if count > 0:
                dna += line.strip()
            count += 1
        for i in range(len(dna)):
            for j in range(4, 13):
                if (i + j) > len(dna):
                    break
                substr = dna[i:i+j]
                rev_substr = get_revc(substr)
                if substr == rev_substr:
                    print(i+1, len(substr))


def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()