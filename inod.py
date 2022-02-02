import sys

def readFile(filename):
    with open(filename,'r') as inf:
        n = int(inf.readline().strip())
        print(n-2)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()