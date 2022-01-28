import sys
import urllib.request
import regex as re

def get_matches(id):
    base_url = "http://www.uniprot.org/uniprot/"
    url = base_url + id + ".fasta"
    exp = r"(N[^P](S|T)[^P])"
    content = urllib.request.urlopen(url).read()
    fasta = ""
    lines = content.decode("utf-8").split('\n')
    for c in lines[1:]:
        fasta += c.strip()
    matches = re.finditer(exp, fasta, overlapped=True)
    return matches

def readFile(filename):
    with open(filename, 'r') as inf:
        ids = []
        for line in inf.readlines():
            ids += [line.strip()]
        for id in ids:
            matches = get_matches(id)
            count = 0
            match_pos = []
            for match in matches:
                count += 1
                match_pos += [match.start(0) + 1]
            if count > 0:
                print(id)
                print(' '.join([str(mpos) for mpos in match_pos]))

def main():
    readFile(sys.argv[1])

if __name__ == '__main__':
    main()