import sys

def fact(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res

def readFile(filename):
    with open(filename, 'r') as inf:
        l = inf.readline()
        pieces = l.split(' ')
        n = int(pieces[0])
        m = int(pieces[1])
        val = 0
        for i in range(m, n+1):
            val += fact(n) // (fact(i) * fact(n-i))
        print(int(val) % 1000000)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()