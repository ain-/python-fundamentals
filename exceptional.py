'''A module for demonstrating exceptions.'''


import sys


def convert(s):
    '''Convert to an integer.'''
    try:
        x = int(s)
        print("Conversion succeeded! x=", x)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}"
              .format(str(e)),
              file=sys.stderr)
        x = -1
    return x
