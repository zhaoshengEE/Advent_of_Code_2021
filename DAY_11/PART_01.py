"""
1. Read the input from the text document into a 2D list, with each element converted into integer
2. Convert the 2D list into a numpy array
3. Declare a variable called flash with initial value of 0
4. Iterate 100 times:
    1. Increment all elements by 1
    2. Initialize an empty set
    3. While there exists elements greater than 9 in the array:
        1. Fetch the x and y coordinate on which the element are greater than 9
        2. Loop through the combination of x and y coordiantes:
            1. Replace the current element with 0
            2. Add the current coordinate into the set
            3. Loop through the adjacent points of the current point:
                1. If the current coordinate is in the set: Continue to the next adjacent point
                2. Increment the value of the adjacent point by 1
    4. Increment the flash with the number of zeros in the array
5. Print out the flash
"""

import numpy as np

STEP_TOTAL = 100
boundary = range(0, 10)

def find_adjacent_points(x, y):
    yield x - 1, y - 1
    yield x - 1, y
    yield x - 1, y + 1
    yield x, y - 1
    yield x, y + 1
    yield x + 1, y - 1
    yield x + 1, y
    yield x + 1, y + 1

if __name__ == "__main__":
    with open("./DAY_11/input.txt") as file:
        data = [[int(i) for i in line] for line in file.read().strip().splitlines()]

    grid = np.array(data)
    flash = 0

    for _ in range(STEP_TOTAL):
        grid += 1
        point_set = set()

        while np.any(grid > 9):
            x_coordinates, y_coordinates = np.where(grid > 9)
            
            for (x, y) in zip(x_coordinates, y_coordinates):
                grid[x, y] = 0
                
                point_set.add((x, y))
                
                for point in find_adjacent_points(x, y):
                    if point not in point_set and point[0] in boundary and point[1] in boundary:
                        grid[point[0], point[1]] += 1
        
        flash += np.sum(grid == 0)
    
    print(f"The total flashes after 100 steps are: {flash}")