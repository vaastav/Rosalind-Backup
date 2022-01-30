import sys
import csv

def readFile(filename):
    protein_mass = 'protein_mass.csv'
    pm_file = csv.DictReader(open(protein_mass))
    weight_map = {}
    for row in pm_file:
        weight_map[row['Protein']] = float(row['Mass'])
    with open(filename, 'r') as inf:
        L = []
        for line in inf.readlines():
            val = float(line.strip())
            L += [val]
        protein = ""
        epsilon = 1e-3
        for i in range(1, len(L)):
            weight = L[i] - L[i-1]
            found = False
            for prot, mass in weight_map.items():
                if abs(weight-mass) < epsilon:
                    protein += prot
                    found = True
                    break
            if not found:
                print("Not found")
        print(protein)

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()