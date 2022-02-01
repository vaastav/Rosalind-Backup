import sys

def edit_distance(s, t):
    l1 = len(s)
    l2 = len(t)
    dp = [[0 for i in range(l2+1)] for j in range(l1+1)]
    bt = [[None for i in range(l2+1)] for j in range(l1+1)]

    for i in range(l1+1):
        for j in range(l2+1):
            if i == 0 and j == 0:
                dp[i][j] = 0
                bt[i][j] = "   "
            elif i == 0:
                dp[i][j] = j
                bt[i][j] = "  " + t[j-1]
            elif j == 0:
                dp[i][j] = i
                bt[i][j] = "  " + s[i-1]
            elif s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]
                bt[i][j] = "NOP"
            else:
                min_val = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1])
                dp[i][j] = 1 + min_val
                if dp[i-1][j-1] == min_val:
                    bt[i][j] = "SUB"
                elif dp[i][j-1] == min_val:
                    bt[i][j] = "INS"
                else:
                    bt[i][j] = "DEL"
                
    print(dp[l1][l2])

    #for i in range(l1+1):
    #    print(' '.join(bt[i]))
        

    # Backtrace
    i = l1
    j = l2
    str1 = ""
    str2 = ""
    while i > 0 and j > 0:
        if bt[i][j] == "NOP" or bt[i][j] == "SUB":
            str1 = s[i-1] + str1
            str2 = t[j-1] + str2
            i = i-1
            j = j-1
        elif bt[i][j] == "INS":
            str1 = "-" + str1
            str2 = t[j-1] + str2
            j = j-1
        else:
            str1 = s[i-1] + str1
            str2 = "-" + str2
            i = i-1

    print(str1)
    print(str2)

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