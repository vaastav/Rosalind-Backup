import sys
from itertools import permutations

def readFile(filename):
    with open(filename, 'r') as inf:
        n = int(inf.readline().strip())
        arr = []
        for i in range(1, n+1):
            arr += [i]
            arr += [-1 * i]
        perms = list(permutations(arr, n))
        new_perms = []
        for p in perms:
            map = {}
            has_duplicate = False
            for j in p:
                if abs(j) in map:
                    has_duplicate = True
                    break
                else:
                    map[abs(j)] = True
            if not has_duplicate:
                new_perms += [p]
        print(len(new_perms))
        for p in new_perms:
            print(' '.join([str(e) for e in p]))

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()