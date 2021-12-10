"""
Algorithm:
1. Read the input from the text document with each line separated as each element in a list (store in a variable called lines)
2. Declare an empty dict called coordinates and the final result with initial value of 0
3. Enumerating through the lines:
    1. Enumerating through each line:
        1. Store the current value (converted into integer) into the dictionary with current coordinate as key
4. Loop through the dictionary items:
    1. Use helper function to find all the adjacent points
    2. If all the adjacent points are greater than the current coordinate: plus current value + 1 to the result
5. Print out the result

Helper Function:
1. Yield four adjacent points one by one
"""

def find_adjacent_points(x, y):
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1

if __name__ == "__main__":
    with open("./DAY_09/input.txt") as file:
        lines = [line for line in file.read().strip().splitlines()]

    coordinates = {}
    result = 0

    for y, line in enumerate(lines):
        for x, element in enumerate(line):
            coordinates[(x, y)] = int(element)
     
    for (x, y), element in coordinates.items():
        if all(coordinates.get(point, 9) > element for point in find_adjacent_points(x, y)):
            result += (element + 1)
    
    print(f"The sum of the risk levels of all low points on your heightmap is: {result}")