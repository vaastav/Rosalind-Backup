import sys

def get_match_len(dna1, dna2):
    length = 0
    i = min(len(dna1), len(dna2))
    while i >= 0:
        if dna1[-i:] == dna2[:i]:
            return len(dna2[:i])
        i -= 1
    return length

def shortest_superstring(dnas):
    dna_set = set(dnas)
    while len(dna_set) != 1:
        longest_string1 = ""
        longest_string2 = ""
        longest_match = -1
        superstring = ""
        for dna1 in dna_set:
            for dna2 in dna_set:
                if dna1 == dna2:
                    continue
                # Check the matching length of dna1's suffix with dna2's prefix
                length = get_match_len(dna1, dna2)
                if length > longest_match:
                    longest_match = length
                    longest_string1 = dna1
                    longest_string2 = dna2
                    superstring = dna1 + dna2[length:]
                # Check the matching length of dna2's suffix with dna1's prefix
                other_length = get_match_len(dna2, dna1)
                if other_length > longest_match:
                    longest_match = other_length
                    longest_string1 = dna2
                    longest_string2 = dna1
                    superstring = dna2 + dna1[other_length:]
                #print(dna1, dna2, length, other_length)
        dna_set.remove(longest_string1)
        dna_set.remove(longest_string2)
        dna_set.add(superstring)
    for item in dna_set:
        print(item)

def readFile(filename):
    with open(filename, "r") as inf:
        dnas = []
        cur_dna = ""
        for line in inf.readlines():
            line = line.strip()
            if line[0] == '>':
                if cur_dna != "":
                    dnas += [cur_dna]
                cur_dna = ""
            else:
                cur_dna += line
        dnas += [cur_dna]
        shortest_superstring(dnas)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()