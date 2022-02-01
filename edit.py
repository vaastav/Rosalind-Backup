import sys

def edit_distance(s, t):
    l1 = len(s)
    l2 = len(t)
    dp = [[0 for i in range(l2+1)] for j in range(l1+1)]

    for i in range(l1+1):
        for j in range(l2+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])
    print(dp[l1][l2])

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
        edit_distance(s, t)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()