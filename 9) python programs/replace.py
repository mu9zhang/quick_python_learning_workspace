# It reads its standard input and writes to its standard output whatever it reads, with all occurrences
# of its first argument replaced by with its second argument.
# python replace.py zero 0 < infile > outfile
# python replace.py zero 0 < infile >> outfile
# python replace.py zero 0 < infile | python replace one 1 > outfile
import sys

def main():
    contents = sys.stdin.read()
    sys.stdout.write(contents.replace(sys.argv[1], sys.argv[2]))

main()
