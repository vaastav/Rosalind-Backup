import sys

def readFile(filename):
    with open(filename, 'r') as inf:
        dnas = []
        cur_dna = ""
        for line in inf.readlines():
            if len(line.strip()) == 0:
                continue
            if line.strip()[0] == '>':
                if cur_dna != "":
                    dnas += [cur_dna]
                cur_dna = ""
            else:
                cur_dna += line.strip()
        dnas += [cur_dna]
        source = dnas[0]
        target = dnas[1]
        j = 0
        i = 0
        arr = []
        while j < len(target) and i < len(source):
            if target[j] == source[i]:
                j += 1
                i += 1
                arr += [i]
            else:
                i += 1
        print(' '.join([str(a) for a in arr]))

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()