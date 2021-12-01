# Algorithm:
# 1. Read the input data from the text document
# 2. Store the data into a list
# 3. Initialize a counting variable (count) and an iterative index (i)
# 4. While the iterative index is less than the length of data:
#     1. If one of the next two elements from current one does not exist: break
#     2. If the sum of the current three elements is greater than the previous three: count += 1
#     3. i += 1
# 5. Print out count

import os

if __name__ == "__main__":
    with open("./DAY_01/input.txt") as file:
        data = [int(i) for i in file.read().strip().split('\n')]

    count = 0
    i = 1

    while i < len(data):
        if i + 1 >= len(data) or i + 2 >= len(data):
            break

        if data[i] + data[i + 1] + data[i + 2] > data[i - 1] + data[i] + data[i + 1]:
            count += 1

        i += 1
    
    print(count)