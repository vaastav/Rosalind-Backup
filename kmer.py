import sys

kmers = {}

def gen_fixed_kmer(alphabet, prefix, k):
    if k == 0:
        global kmers
        kmers[prefix] = 0
        return
    for a in alphabet:
        newprefix = prefix + a
        gen_fixed_kmer(alphabet, newprefix, k-1)

def gen_kmers(k):
    alphabet = ['A', 'C', 'G', 'T']
    gen_fixed_kmer(alphabet, "", k)

def readFile(filename):
    with open(filename, 'r') as inf:
        data = ""
        count = 0
        for line in inf.readlines():
            if count > 0:
                data += line.strip()
            count += 1
        global kmers
        for i in range(len(data) - 4 + 1):
            kmer = data[i:i+4]
            kmers[kmer] += 1

def main():
    gen_kmers(4)
    readFile(sys.argv[1])
    outputs = []
    for k, v in kmers.items():
        outputs += [str(v)]
    print(' '.join(outputs))

if __name__ == '__main__':
    main()