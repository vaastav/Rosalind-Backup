import sys

ID_COUNTER=0
def get_node_id():
    global ID_COUNTER
    ID_COUNTER += 1
    return ID_COUNTER

class Node:
    def __init__(self):
        self.children = {}
        self.id = get_node_id()

    def build(self, string):
        potential_child = string[0]
        if potential_child not in self.children:
            self.children[potential_child] = Node()
        if len(string[1:]) > 0:
            node = self.children[potential_child]
            node.build(string[1:])

    def print(self):
        for child, child_node in self.children.items():
            print(self.id, child_node.id, child)
            child_node.print()

class Graph:

    def __init__(self):
        self.root_node = Node()

    def print(self):
        self.root_node.print()

def readFile(filename):
    with open(filename, 'r') as inf:
        dnas = []
        for line in inf.readlines():
            dnas += [line.strip()]
        g = Graph()
        for dna in dnas:
            g.root_node.build(dna)

        g.print()

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()