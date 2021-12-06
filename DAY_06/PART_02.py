"""
Algorithm:
1. Read the input from the text document. Store the input in a dictionary
2. Initialize a variable called day with initial value of 1
3. While the day is less than or equal to the final day:
    1. Copy the current dictionary and reset current dictionary to empty Counter
    2. Iterate through the copied dictionary via key-value pairs:
        1. If the current key is greater than 0:
            1. Increase the dict[key - 1] by value
        2. Else:
            1. Increase the dict[6] by value
            2. Increase the dict[8] by value as well
    2. day += 1
4. Print out the length of the list
"""

from collections import Counter

final_day = 256

if __name__ == "__main__":
    with open("./DAY_06/input.txt") as file:
        fish_set = [int(i) for i in file.read().strip().split(',')]
        fish_set = Counter(fish_set)

    day = 1

    while day <= final_day:
        fish_set_copy = fish_set
        fish_set = Counter()

        for key, value in fish_set_copy.items():
            if key > 0:
                fish_set[key - 1] += value
            else:
                fish_set[6] += value
                fish_set[8] += value

        day += 1

    print(sum(fish_set.values()))