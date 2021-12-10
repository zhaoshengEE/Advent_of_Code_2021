"""
Algorithm:
1. Read the input from the text document with each line separated as each element in a list (store in a variable called lines)
2. Declare an empty dict called coordinates and an empty list called sizes
3. Enumerating through the lines:
    1. Enumerating through each line:
        1. Store the current value (converted into integer) into the dictionary with current coordinate as key
4. Loop through the dictionary items:
    1. Use helper function to find all the adjacent points
    2. Figure out if the current element is a low point, if it is:
       (Condition: if all the adjacent points are greater than the current coordinate)
        1. Initialize an empty set
        2. Initialize a stack with current coordinate as the only element
        3. While the stack is not empty:
            1. Pop the element from the stack into xx, yy
            2. Add (xx, yy) into the set
            3. Loop through the adjacent points with the help of the helper function:
                1. If the point is not in the set and the point is not 9:
                    1. Add the point to the stack
        4. Append the length of set to the list sizes
5. Sort the sizes list in place and in reversed order
6. Print out the product of the first three elements in sizes

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
    sizes = []

    for y, line in enumerate(lines):
        for x, element in enumerate(line):
            coordinates[(x, y)] = int(element)
     
    for (x, y), element in coordinates.items():
        size = 0
        if all(coordinates.get(point, 9) > element for point in find_adjacent_points(x, y)):
            points_set = set()
            
            stack = [(x, y)]
            
            while stack:
                xx, yy = stack.pop()
                points_set.add((xx, yy))

                for point in find_adjacent_points(xx, yy):
                    if point not in points_set and coordinates.get(point, 9) != 9:
                        stack.append(point)

            sizes.append(len(points_set))
    
    sizes.sort(reverse = True)

    print(f"The product of the sizes of the three largest basins is: {sizes[0] * sizes[1] * sizes[2]}")