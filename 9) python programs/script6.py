#! /usr/bin/env python
import sys

_1to9dict = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
             '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
             '9': 'nine'}

_10to19dict = {'0': 'ten', '1': 'eleven', '2': 'twelve',
               '3': 'thirteen', '4': 'fourteen', '5': 'fifteen',
               '6': 'sixteen', '7': 'seventeen', '8': 'eighteen',
               '9': 'nineteen'}

_20to90dict = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
               '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}

def num2words(num_string):
    if num_string == '0':
        return 'zero'
    if len(num_string) > 2:
        return 'Sorry can only handle 1 or 2 digit numbers'
    num_string = '0' + num_string
    tens, ones = num_string[-2], num_string[-1]
    if tens == '0':
        return _1to9dict[ones]
    elif tens == '1':
        return _10to19dict[ones]
    else:
        return _20to90dict[tens] + ' ' + _1to9dict[ones]

# controlling function
def main():
    print(num2words(sys.argv[1]))

"""
(1) People combine scripts with modules when they want to make functions they’ve created in a script
    available to other modules or scripts. Also, a module may be instrumented so it can run as a script
    either to provide a quick interface to it for users or to provide hooks for automated module testing.

(2) Combining a script and a module is a simple matter of putting the following conditional test around the controlling function main()

(3) If it’s called as a script, it will be run with the name __main__, and the controlling function, main, will be called.
    If the test has been imported into an interactive session or another module, its name will be its filename. 
"""
if __name__ == '__main__':
    main()
else:
    # module-specific initialization code if any
