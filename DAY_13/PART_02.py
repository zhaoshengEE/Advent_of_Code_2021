"""
1. Declare an empty defaultdict called paper
2. Read the input from the text document:
    1. Split with the '\n\n' first into two variables called coordinate_part and instruction_part
    2. Loop through the coordinate_part, use each coordinate as key to update the paper with '#' 
    3. Split the instruction_part into a list called instructions
3. Loop through the instructions:
    1. Get the axis and number, convert number into integer
    2. Declare a new paper
    3. Loop through the keys in paper:
        1. If key is less than the number: 
            1. Insert the current key into the new paper
            2. Continue to the next iteration
        2. Insert the symmetric key into the new paper
    4. Copy the new paper into paper
4. Loop through the paper to find the maximum y and x respectively
5. Declare a numpy array fulfilled with '.' and named as code
6. Loop through the paper to replace the '.' with '#' in code accordingly
7. Print out the code
"""

from collections import defaultdict
import numpy as np
from print_2D_array import print_2D_array

if __name__ == "__main__":
    paper = defaultdict(str)

    with open("./DAY_13/input.txt") as file:
        coordinates, instruction_part = file.read().strip().split('\n\n')
    
        for coordiante in coordinates.splitlines():
            x, y = map(int, coordiante.split(','))
            paper[(y, x)] = '#'
        
        instructions = [instruction.replace("fold along ", "") for instruction in instruction_part.splitlines()]

    for instruction in instructions:
        axis, number = instruction.split('=')
        number = int(number)
        new_paper = defaultdict(str)

        for (y, x) in paper.keys():            
            if axis == 'y':
                if y < number:
                    new_paper[(y, x)] = '#'
                    continue
                
                new_paper[(2 * number - y, x)] = '#'

            else:
                if x < number:
                    new_paper[(y, x)] = '#'
                    continue
                
                new_paper[(y, 2 * number - x)] = '#'
            
        paper = new_paper.copy()


    x_max = float("-inf")
    y_max = float("-inf")

    for (y, x) in paper.keys():
        y_max = y if y > y_max else y_max
        x_max = x if x > x_max else x_max
    
    code = np.full((y_max + 1, x_max + 1), '.', dtype = str)
    
    for (y, x) in paper.keys():
        code[y, x] = '#'
    
    print_2D_array(code)