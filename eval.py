import sys

def readFile(filename):
    with open(filename, "r") as inf:
        lines = inf.readlines()
        N = int(lines[0].strip())
        dna = ''.join([l.strip() for l in lines[1:len(lines)-1]])
        A = lines[len(lines)-1].strip().split(' ')
        A = [float(a) for a in A]
        #print(N, dna, A)
        probs_list = []
        for a in A:
            prob_g = a / 2
            prob_c = a / 2
            prob_a = (1-a) / 2
            prob_t = (1-a) / 2
            probs = {'A': prob_a, 'T': prob_t, 'G': prob_g, 'C': prob_c}
            prob = 1.0
            for base in dna:
                prob = prob * probs[base]
            probs_list += [prob * (N - len(dna) + 1)]
        print(' '.join([str(round(p,3)) for p in probs_list]))

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()