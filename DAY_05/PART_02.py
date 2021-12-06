"""
Algorithm:
1. Read the input from the text document and store the input as string just for now
2. Initialize two empty lists (i.e. x_coordinates & y_coordinates)
3. Iterate through each line of input:
    1. Split each line of input into x_start, y_start, x_end, and y_end
    2. If x_start == x_end OR y_start == y_end OR the absolute value of the slope is 1:
        1. Store the x_start and x_end into the x_coordinates and y_start and y_end into the y_coordiantes
4. Convert x_coordinates and y_coordiantes into numpy array
5. Initialize a 2D numpy array with zeros(i.e. diagram), with the (max(x) + 1, max(y) + 1) as shape
6. Initialize an iterative variable i with value of 0
7. While i < x_coordinates.shape[0]:
    1. If x_coordinates[i, 0] == x_coordinates[i, 1]:
        1. Assign x_coordinates[i, 0] to x
        2. Iterate from y_coordinates[i, 0] to y_coordinates[i, 1] (or reverse):
            1. diagram[x, y] += 1
    2. Else if y_coordinates[i, 0] == y_coordinates[i, 1]:
        1. Assign y_coordinates[i, 0] to y
        2. Iterate from x_coordinates[i, 0] to x_coordinates[i, 1] (or reverse):
            1. diagram[x, y] += 1
    3. Else if the slope is 1:
        1. If x is increasing (x_coordinates[i, 1] > x_coordinates[i, 0]):
            1. Increase the diagram through accordingly diagonal by 1
        2. Else:
            1. Increase the diagram through accordingly diagonal by 1
    4. Else:(i.e. the slope is -1)
        1. If x is increasing (x_coordinates[i, 1] > x_coordinates[i, 0]):
            1. Increase the diagram through accordingly diagonal by 1
        2. Else:
            1. Increase the diagram through accordingly diagonal by 1
    5. i += 1
8. Print out np.sum(diagram >= 2)
"""

import numpy as np
import re

if __name__ == "__main__":
    with open("./DAY_05/input.txt") as file:
        lines = [i for i in file.read().strip().splitlines()]
    
    x_coordinates = [] 
    y_coordinates = []

    for line in lines:
        x_start, y_start, x_end, y_end = map(int, re.split(",| -> ", line))

        if x_start == x_end or y_start == y_end or abs((y_end - y_start) // (x_end - x_start)) == 1:
            x_coordinates.append([x_start, x_end])
            y_coordinates.append([y_start, y_end])

    x_coordinates = np.array(x_coordinates)
    y_coordinates = np.array(y_coordinates)
    diagram = np.zeros((x_coordinates.max() + 1, y_coordinates.max() + 1), dtype = int)
    i = 0

    while i < x_coordinates.shape[0]:
        if x_coordinates[i, 0] == x_coordinates[i, 1]:
            x = x_coordinates[i, 0]
            if y_coordinates[i, 1] > y_coordinates[i, 0]:
                diagram[x, y_coordinates[i, 0] : y_coordinates[i, 1] + 1] += 1
            else:
                diagram[x, y_coordinates[i, 1] : y_coordinates[i, 0] + 1] += 1
        
        elif y_coordinates[i, 0] == y_coordinates[i, 1]:
            y = y_coordinates[i, 0]
            if x_coordinates[i, 1] > x_coordinates[i, 0]:
                diagram[x_coordinates[i, 0] : x_coordinates[i, 1] + 1, y] += 1
            else:
                diagram[x_coordinates[i, 1] : x_coordinates[i, 0] + 1, y] += 1

        elif (y_coordinates[i, 1] - y_coordinates[i, 0]) // (x_coordinates[i, 1] - x_coordinates[i, 0]) == 1:
            x = x_coordinates[i, 0]
            y = y_coordinates[i, 0]
            if x_coordinates[i, 1] > x_coordinates[i, 0]:
                while x != x_coordinates[i, 1] + 1:
                    diagram[x, y] += 1
                    x += 1
                    y += 1
            else:
                while x != x_coordinates[i, 1] - 1:
                    diagram[x, y] += 1
                    x -= 1
                    y -= 1

        else:
            x = x_coordinates[i, 0]
            y = y_coordinates[i, 0]
            if x_coordinates[i, 1] > x_coordinates[i, 0]:
                while x != x_coordinates[i, 1] + 1:
                    diagram[x, y] += 1
                    x += 1                    
                    y -= 1
            else:
                while x != x_coordinates[i, 1] - 1:
                    diagram[x, y] += 1
                    x -= 1
                    y += 1

        i += 1
    
    result = np.sum(diagram >= 2)
    print(result)