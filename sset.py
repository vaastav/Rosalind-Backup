import sys

def readFile(filename):
    with open(filename, 'r') as inf:
        line = inf.readline()
        n = int(line.strip())
        ssets = (2 ** n) % 1000000
        print(ssets)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()