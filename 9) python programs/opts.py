"""
You can configure a script to accept command-line options as well as arguments.
The argparse module provides support for parsing different types of arguments and can even generate usage messages.
To use the argparse module, you create an instance of ArgumentParser, populate it with arguments, and then read
both the optional and positional arguments.
(*) python opts.py -x100 -q -f outfile 2 args
"""
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()

    # positional arguments (without a prefix character, '-')
    parser.add_argument("indent", type=int, help="indent for report")
    parser.add_argument("input_file", help="read data from this file")

    # optional arguments (option beginning with '-')
    parser.add_argument("-f", "--file", dest="filename", 
                        help="write report to FILE", metavar="FILE")
    parser.add_argument("-x", "--xray",
                        help="specify xray strength factor")
    parser.add_argument("-q", "--quiet",
                        action="store_false", dest="verbose", default=True,
                        help="don't print status messages to stdout")

    # The argparse module returns a Namespace object containing the arguments as
    # attributes. You can get the values of the arguments by using dot notation. If
    # there’s no argument for an option, its value is None. 
    args = parser.parse_args()
    print("arguments: ", args)

main()

