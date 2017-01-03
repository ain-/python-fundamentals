'''A module for demonstrating exceptions.'''


def convert(s):
    '''Convert to an integer.'''
    try:
        x = int(s)
        print("Conversion succeeded! x=", x)
    except (ValueError, TypeError):
        print("conversion failed!")
        x = -1
    return x
