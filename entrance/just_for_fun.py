"""
docstring to module
just use windows and linux utilits to count 
what about java? nothing >:(
"""

import subprocess
import os
import sys


def main():
    if os.name == 'posix':
        subprocess.Popen(['wc', '-l'] + sys.argv[1:])
    elif os.name == 'nt':
        subprocess.Popen(['find', '/c', sys.argv[1:], '/v', ""])
    else:
        print('do you use calculate or something else?')


if __name__ == '__main__':
    main()
