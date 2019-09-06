"""
Other functions in module fileinput:

(*) At any point to determine the total number of lines that have been read (lineno), 
(*) The number of lines that have been read out of the current file (filelineno),
(*) The name of the current file (filename),
(*) Whether this is the first line of a file (isfirstline),
(*) And/or whether standard input is currently being read (isstdin). 
(*) You can at any point skip to the next file (nextfile) or close the whole stream (close).


If you call fileinput.input with an argument of a single filename or a list of filenames,
they’re used as its input files rather than the arguments in sys.argv.

fileinput.input also has an inplace option that leaves its output in the same file as its input
while optionally leaving the original around as a backup file.

(*) python script5.py infile outfile
"""

# python script5.py file1 file2
import fileinput

def main():
    for line in fileinput.input():
        if fileinput.isfirstline():
            print("<start of file {0}>".format(fileinput.filename()))
        print(line, end="")

main()
