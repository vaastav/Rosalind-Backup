import sys

def read_file(filename):
	f = open(filename,'rU')
	line = f.readline().strip()
	words = dict()
	for word in line.split(' '):
		if word in words:
			words[word] += 1
		else:
			words[word] = 1
	for key, value in words.items():
		print(key + ' ' + str(value))

def main():
	read_file(sys.argv[1])

if __name__ == '__main__':
	main()
