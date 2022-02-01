import sys

class Graph:

    def __init__(self, n):
        self.vertices = list(range(1,n+1))
        self.adj_list = {}
        self.visited = {}
        for i in self.vertices:
            self.adj_list[i] = set()
            self.visited[i] = False
        
    def add_edge(self, v1, v2):
        self.adj_list[v1].add(v2)
        self.adj_list[v2].add(v1)

    def dfs(self, temp, i):
        self.visited[i] = True
        temp += [i]
        for j in self.adj_list[i]:
            if self.visited[j] == False:
                temp = self.dfs(temp, j)
        return temp

    def connectedcomponents(self):
        cc = []
        for i in self.vertices:
            if self.visited[i] == False:
                temp = []
                temp = self.dfs(temp, i)
                cc += [temp]
        return cc

def readFile(filename):
    with open(filename, 'r') as inf:
        count = 0
        n = -1
        line = inf.readline()
        n = int(line.strip())
        g = Graph(n)
        for line in inf.readlines():
            edge = line.strip().split(' ')
            g.add_edge(int(edge[0]), int(edge[1]))
        cc = g.connectedcomponents()
        print(len(cc)-1)


def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()