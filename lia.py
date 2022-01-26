import sys

def factorial(n):
    if n < 2:
        return 1
    val = 1
    for i in range(2,n+1):
        val = val * i
    return val

def prob(n, children):
    x = 1.0 - 0.25
    prob = 0
    for j in range(children - n, children+1):
        prob += factorial(children) / (factorial(j)*factorial(children-j)) \
				* x**j * (1 - x)**(children-j)

    return prob

def calc_probability(k, n):
    children = 2**k
    print(1 - prob(n-1, children))

def readFile(filename):
    inf = open(filename, 'r')
    line = inf.readline().strip()
    pieces = line.split(' ')
    k = int(pieces[0])
    n = int(pieces[1])
    calc_probability(k, n)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()