# Command-line arguments have been stored in sys.argv as a list of string
# (*) python script2.py arg1 arg2 3
import sys

def main():
    print("this is our second test script file")
    print(sys.argv)

main()
