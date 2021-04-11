import math
import sys

def read_file(filename):
    inf = open(filename, 'rU')
    string = inf.readline().strip()
    gc_contents = inf.readline().split(' ')
    gc_contents = [float(gc) for gc in gc_contents]
    totals = []
    for gc in gc_contents:
        log_dict = {}
        c = math.log(gc / 2, 10)
        log_dict['C'] = c
        log_dict['G'] = c
        a = math.log((1-gc)/2, 10)
        log_dict['A'] = a
        log_dict['T'] = a
        total = 0.0
        for s in string:
            total += log_dict[s]
        totals += [total]
    print(' '.join([str(total) for total in totals]))

def main():
    read_file(sys.argv[1])

if __name__ == '__main__':
    main()
