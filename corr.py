import sys

def dist(str1, str2):
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance

def rcomplement(read):
    new_read = ""
    for r in read:
        if r == 'A':
            new_read += 'T'
        elif r== 'T':
            new_read += 'A'
        elif r == 'G':
            new_read += 'C'
        else:
            new_read += 'G'
    return new_read[::-1]

def readFile(filename):
    with open(filename, 'r') as inf:
        reads = []
        current_read = ""
        for line in inf.readlines():
            line = line.strip()
            if line[0] == '>':
                if current_read != "":
                    reads += [current_read]
                current_read = ""
            else:
                current_read += line
        reads += [current_read]
        read_map = {}
        for r in reads:
            revc = rcomplement(r)
            if r not in read_map and revc not in read_map:
                read_map[r] = 1
            elif r in read_map:
                read_map[r] += 1
            elif revc in read_map:
                read_map[revc] += 1
        errors = []
        for r, val in read_map.items():
            if val < 2:
                errors += [r]
        for e in errors:
            for r, val in read_map.items():
                if val < 2:
                    continue
                if e == r:
                    continue
                elif dist(e,r) == 1:
                    print(e + "->" + r)
                    break
                else:
                    revc = rcomplement(r)
                    if dist(e, revc) == 1:
                        print(e + "->" + revc)
                        break

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()