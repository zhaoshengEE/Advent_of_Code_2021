"""
Algorithm:
1. Read the input from the text document:
    1. Split by '/n' first and by ' | ' and then store into pairs
    2. Separate pairs into two variables named patterns and values
    3. Split values by whitespace into a variable named digits
2. Declare a counting variable with initial value of 0
3. Iterate through the digits:
    1. If the length of current element is 2, 3, 4, or 7:
        1. count += 1
4. Print out count
"""

import numpy as np

unique_segment_length = [2, 3, 4, 7]

if __name__ == "__main__":
    with open("./DAY_08/input.txt") as file:
        pairs = [line.split(' | ') for line in file.read().strip().splitlines()]

        patterns = [pair[0] for pair in pairs]
        values = [pair[1] for pair in pairs]

        digits = [value.split() for value in values]
        digits = (np.array(digits)).flatten()

    count = 0

    for digit in digits:
        if len(digit) in unique_segment_length: count += 1
    
    print(f"The number of times that 1, 4, 7, 8 appear is {count}")