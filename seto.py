import sys

def print_set(s):
    string = "{"
    string += ", ".join([str(i) for i in s])
    string += "}"
    print(string)

def readFile(filename):
    with open(filename, 'r') as inf:
        n = int(inf.readline().strip())
        l1 = inf.readline().strip().strip("{}").replace(" ", "")
        l2 = inf.readline().strip().strip("{}").replace(" ", "")
        s1 = set([int(i) for i in l1.split(",")])
        s2 = set([int(i) for i in l2.split(",")])
        U = set(list(range(1,n+1)))
        union = s1 | s2
        intersection = s1 & s2
        a_b = s1 - s2
        b_a = s2 - s1
        ac = U - s1
        bc = U - s2
        print_set(union)
        print_set(intersection)
        print_set(a_b)
        print_set(b_a)
        print_set(ac)
        print_set(bc)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()