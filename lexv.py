import sys

def printStrings(alphabet, base, level, max_level):
    if level > max_level:
        return
    for a in alphabet:
        string = base + a
        print(string)
        printStrings(alphabet, string, level+1, max_level)

def readFile(filename):
    inf = open(filename, 'rU')
    line = inf.readline().strip()
    alphabet = line.split(' ')
    line = inf.readline().strip()
    max_depth = int(line)
    printStrings(alphabet, "", 1, max_depth)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()
