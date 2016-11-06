from __future__ import division
import sys

files = {}

def gcContent(dna):
	count = 0
	space = 0
	for a in dna:
		if a == 'G' or a == 'C':
			count += 1
		elif a == '\n' or a == ' ':
			space +=1
	
	gc = (count*100/(len(dna)-space))
	return gc

def read_file(filename):
	inf = open(filename,'rU')
	maxcontent = 0.0
	name = ""
	dna = ""
	for line in inf:
		if line[0] == '>':
			if name != "" :
				files[name] = gcContent(dna)
			name = line[1:]
			dna = ""
		else : 
			dna += line
	files[name] = gcContent(dna)
	max_num = 0.0
	dna_name = ""
	for name in files:
		if files[name] > max_num :
			max_num = files[name]
			#print max_num
			dna_name = name

	print dna_name
	print str(max_num)


def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
