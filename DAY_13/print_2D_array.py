"""
Print a 2-D numpy array in a nicer format

A function adapted from https://stackoverflow.com/a/52905123
"""

def print_2D_array(arr):
    for a in arr:
        for elem in a:
            print("{}".format(elem).rjust(3), end="")
        print(end="\n")