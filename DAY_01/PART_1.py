# Algorithm:
# 1. Read the input data from the text document
# 2. Store the data into a list
# 3. Initialize a counting variable (count)
# 4. Iterate through the list starting fron the 2nd element:
#     1. If the next element is greater than the previous one: count += 1
# 5. Print out count

import os

if __name__ == "__main__":
    os.chdir("DAY_01")
    
    file = open("input.txt", "r")
    data = file.readlines()
    file.close()

    data = [num.replace("\n", "") for num in data]
    data = list(map(int, data))
    
    count = 0

    for i in range(1, len(data)):
        if data[i] > data[i - 1]: 
            count += 1
    
    print(count)