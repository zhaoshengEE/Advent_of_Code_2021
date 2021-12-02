# Algorithm:
# 1. Read the input from the text document, split by new line character and space
# 2. Store the input into a 2D list
# 3. Initialize three variables with value of 0 (horizontal, depth, and aim)
# 4. Initialize an iterative variable (i) with value of 0
# 5. While i is less than the length of the list:
#     1. If current element is "forward":
#       1. increment horizontal variable by X
#       2. increment depth by (aim * X)
#     2. Else if current element is "up", decrement aim variable by X
#     3. Else increment aim variable by X
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
    aim = 0
    i = 0

    while i < len(data):
        if data[i][0] == 'forward': 
            horizontal += int(data[i][1])
            depth += (aim * int(data[i][1]))

        elif data[i][0] == 'up': aim -= int(data[i][1])

        else: aim += int(data[i][1])

        i += 1
    
    print(horizontal * depth)