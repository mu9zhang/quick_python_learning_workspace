#! /usr/bin/env python
"""
If you’re on UNIX, you can easily make a script directly executable. Add the above
line to its top, and change its mode appropriately (that is, chmod +x script_exe.py):
(*) script_exe.py 0 arg1 arg2 3

If you’re writing administrative scripts on UNIX, several library modules are available that you may find useful:
(1) grp for accessing the group database
(2) pwd for accessing the password database
(3) resource for accessing resource usage information
(4) syslog for working with the syslog facility
(5) stat for working with information about a file or directory obtained from an os.stat call
"""
import sys

print(sys.argv)
