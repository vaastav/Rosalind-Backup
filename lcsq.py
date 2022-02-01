import sys

def lcsq(s, t):
    l1 = len(s)
    l2 = len(t)
    dp = [[None] * (l2+1) for i in range(l1+1)]
    
    for i in range(l1+1):
        for j in range(l2+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    i = l1
    j = l2
    substr = ""
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            substr = s[i-1] + substr
            i = i-1
            j = j-1
        elif dp[i-1][j] > dp[i][j-1]:
            i = i-1
        else:
            j = j-1
    print(substr)

def readFile(filename):
    with open(filename, "r") as inf:
        dnas = []
        current_dna = ""
        for line in inf.readlines():
            if line[0] == '>':
                if current_dna != "":
                    dnas += [current_dna]
                    current_dna = ""
            else:
                current_dna += line.strip()
        dnas += [current_dna]
        s = dnas[0]
        t = dnas[1]
        lcsq(s, t)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()