import sys

def fibd(n, m):
    result = 0
    rab_array = []
    new_rabs = []
    for i in range(n):
        if i < 1:
            rab_array += [1]
            new_rabs += [1]
        elif i < 2:
            rab_array += [1]
            new_rabs += [0]
        elif i < m:
            rab_array.append(rab_array[-1] + rab_array[-2])
            new_rabs += [rab_array[i] - rab_array[i-1]]
        else:
            print("else case")
            rab_array.append(rab_array[-1] + rab_array[-2] - new_rabs[len(rab_array)-m])
            new_rabs += [rab_array[-1] - rab_array[-2]]
        print(rab_array, new_rabs)
    result = rab_array[-1]
    print(result)

def wabbits(n, m):
    """
    Return the total number of rabbits that remain after n months if all
    rabbits live for m months.
    """
    prev_vals = [1] + (m - 1) * [0]
    print(prev_vals)
    for i in range(2, n + 1):
        next_val = sum(prev_vals[1:])
        prev_vals = [next_val] + prev_vals[:-1]
        print(prev_vals)
    return sum(prev_vals)

def readFile(filename):
    with open(filename, 'r') as inf:
        line = inf.readline().strip()
        pieces = line.split(' ')
        n = int(pieces[0])
        m = int(pieces[1])
        #fibd(n, m)
        print(wabbits(n, m))

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()