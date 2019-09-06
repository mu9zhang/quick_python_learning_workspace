"""
The fileinput provides support for processing lines of input from one or more files. It automatically reads the
command-line arguments (out of sys.argv) and takes them as its list of input files. Then it allows you to
sequentially iterate through these lines. 

python script4.py sole1.tst sole2.tst
"""
import fileinput

def main():
    for line in fileinput.input():
        if not line.startswith('##'):
            print(line, end='')

main()
