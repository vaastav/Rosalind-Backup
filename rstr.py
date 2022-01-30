import sys

def calc_probability(N, x, s):
    prob = 1.0
    for c in s:
        if c == 'G' or c == 'C':
            prob *= x * 0.5
        else:
            prob *= (1-x) * 0.5
    prob = (1-prob) ** N
    print(round(1 - prob, 3))

def readFile(filename):
    with open(filename, 'r') as inf:
        l1 = inf.readline()
        l1_pieces = l1.strip().split(' ')
        N = int(l1_pieces[0])
        x = float(l1_pieces[1])
        l2 = inf.readline()
        s = l2.strip()
        calc_probability(N, x, s)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()