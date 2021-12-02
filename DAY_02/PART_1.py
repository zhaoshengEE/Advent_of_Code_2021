# Algorithm:
# 1. Read the input from the text document, split by new line character and space
# 2. Store the input into a 2D list
# 3. Initialize two variables with value of 0 (horizontal and depth)
# 4. Initialize an iterative variable (i) with value of 0
# 5. While i is less than the length of the list:
#     1. If current element is "forward", increment horizontal variable
#     2. Else if current element is "up", decrement depth variable
#     3. Else increment depth variable
#     4. Increment i by 1
# 6. Print out horizontal times depth

import os

if __name__ == "__main__":
    os.chdir("DAY_02")
    
    file = open("input.txt", "r")
    data = file.readlines()
    file.close()

    data = [num.replace("\n", "").split(' ') for num in data]
    
    horizontal = 0 
    depth = 0
    i = 0

    while i < len(data):
        if data[i][0] == 'forward': horizontal += int(data[i][1])

        elif data[i][0] == 'up': depth -= int(data[i][1])

        else: depth += int(data[i][1])

        i += 1
    
    print(horizontal * depth)