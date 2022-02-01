import sys
import csv

def edit_distance(s, t, sub_map):
    l1 = len(s)
    l2 = len(t)
    dp = [[0 for i in range(l2+1)] for j in range(l1+1)]

    for i in range(l1+1):
        for j in range(l2+1):
            if i == 0:
                dp[i][j] = j * 5
            elif j == 0:
                dp[i][j] = i * 5
            elif s[i-1] == t[j-1]:
                sub_cost = sub_map[s[i-1]][t[j-1]]
                dp[i][j] = dp[i-1][j-1] + sub_cost
            else:
                sub_cost = sub_map[s[i-1]][t[j-1]]
                dp[i][j] = min(min(dp[i-1][j] + 5, dp[i][j-1] + 5), dp[i-1][j-1] + sub_cost)
    print(-1 * dp[l1][l2])

def readFile(filename):
    with open(filename, 'r') as inf:
        proteins = []
        current_prot = ""
        for line in inf.readlines():
            if line[0] == '>':
                if current_prot != "":
                    proteins += [current_prot]
                    current_prot = ""
            else:
                current_prot += line.strip()
        proteins += [current_prot]
        s = proteins[0]
        t = proteins[1]
        inf = csv.DictReader(open('blosum62.csv','r'))
        alphabet = 'A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y'.split(',')
        sub_map = {}
        for row in inf:
            spec_sub_map = {}
            for a in alphabet:
                spec_sub_map[a] = int(row[a]) * -1
            sub_map[row['Protein']] = spec_sub_map
        edit_distance(s, t, sub_map)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()