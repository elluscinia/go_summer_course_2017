"""
docstring to module
"""

import sys


def main():
    try:
        with open(sys.argv[1], 'r') as f:
            print(sum((1 for x in f)))
    except IndexError as ex:
        print('You forgot to pass filename. Try again.')
    except FileNotFoundError as ex:
        print('File "%s" does not exist. Check filename and try again.' % sys.argv[1])


if __name__ == '__main__':
    main()
