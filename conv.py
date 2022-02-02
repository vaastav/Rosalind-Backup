import sys

def readFile(filename):
    with open(filename, "r") as inf:
        l1 = inf.readline().strip()
        l2 = inf.readline().strip()
        s1 = [float(s) for s in l1.split(" ")]
        s2 = [float(s) for s in l2.split(" ")]
        multiset = {}
        for e1 in s1:
            for e2 in s2:
                diff = round(e1 - e2,3)
                if diff not in multiset:
                    multiset[diff] = 0
                multiset[diff] += 1
        max_count = 0
        max_val = -1
        for val, count in multiset.items():
            if count > max_count:
                max_count = count
                max_val = abs(val)
        print(max_count)
        print(max_val)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()