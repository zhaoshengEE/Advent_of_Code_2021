"""
Algorithm:
1. Read the input from the text document and store the input as string just for now
2. Initialize two empty lists (i.e. x_coordinates & y_coordinates)
3. Iterate through each line of input:
    1. Split each line of input into x_start, y_start, x_end, and y_end
    2. Store the x_start and x_end into the x_coordinates and y_start and y_end into the y_coordiantes
4. Convert x_coordinates and y_coordiantes into numpy array
5. Initialize a 2D numpy array with zeros(i.e. diagram), with the (max(x) + 1, max(y) + 1) as shape
6. Initialize an iterative variable i with value of 0
7. While i < x_coordinates.shape[0]:
    1. Identify the direction on which the x coordinate is moving (x_direction)
    2. Identify the direction on which the y coordinate is moving (y_direction)
    3. Assign staring x and y coordinates to two variables named x and y respectively
        1. While (x, y) != (x_end, y_end):
            1. diagram[x, y] += 1
            2. x += x_direction
            3. y += y_direction
        2. diagram[x_end, y_end] += 1
    4. i += 1
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
        x_coordinates.append([x_start, x_end])
        y_coordinates.append([y_start, y_end])

    x_coordinates = np.array(x_coordinates)
    y_coordinates = np.array(y_coordinates)
    diagram = np.zeros((x_coordinates.max() + 1, y_coordinates.max() + 1), dtype = int)
    i = 0

    while i < x_coordinates.shape[0]:
        if x_coordinates[i, 0] < x_coordinates[i, 1]: x_direction = 1
        elif x_coordinates[i, 0] > x_coordinates[i, 1]: x_direction = -1
        else: x_direction = 0

        if y_coordinates[i, 0] < y_coordinates[i, 1]: y_direction = 1
        elif y_coordinates[i, 0] > y_coordinates[i, 1]: y_direction = -1
        else: y_direction = 0

        x = x_coordinates[i, 0]
        y = y_coordinates[i, 0]
        while (x, y) != (x_coordinates[i, 1], y_coordinates[i, 1]):
            diagram[x, y] += 1
            x += x_direction
            y += y_direction

        diagram[x_coordinates[i, 1], y_coordinates[i, 1]] += 1
        
        i += 1
    
    result = np.sum(diagram >= 2)
    print(result)