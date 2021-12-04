# Algorithm:
# 1. Read the input from the text document into a list, and each element in the list should be a string
# 2. Initialize two counting variable with value of 0 (count_zero, count_one)
# 3. Initialize two string variables (gamma and epsilon)
# 4. Iterate through each column of the input:
#       1. Set count_zero and count_one to 0 
#       2. Iterate through each row of the input:
#           1. If input[row][col] = 1:, count_one += 1
#           2. Else: count_zero += 1
#       3. If count_zero > count_one: gamma += '0', epsilon += '1'
#       4. Else: gamma += '1', epsilon += '0'
# 5. Convert gamma and epsilon to decimal integer and print out their product


if __name__ == "__main__":
    with open("./DAY_03/input.txt") as file:
        data = [i for i in file.read().strip().split('\n')]

    count_one = 0
    count_zero = 0
    gamma = ""
    epsilon = ""

    for column in range(len(data[0])):
        count_zero = sum([data[row][column] == '0' for row in range(len(data))])
        count_one = sum([data[row][column] == '1' for row in range(len(data))])

        if count_zero > count_one:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    print(int(gamma, 2) * int(epsilon, 2))