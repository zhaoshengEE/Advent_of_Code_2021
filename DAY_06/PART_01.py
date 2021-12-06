"""
Algorithm:
1. Read the input from the text document. Store the input in a integer list
2. Initialize a variable called day with initial value of 1
3. While the day is less than or equal to the final day:
    1. Iterate through the input:
        1. If the current element is greater than 0:
            1. Decrease current element by 1
        2. Else:
            1. Reset current element to 6
            2. Append an 8 at the end of the list
    2. day += 1
4. Print out the length of the list
"""

final_day = 80

if __name__ == "__main__":
    with open("./DAY_06/input.txt") as file:
        fish_set = [int(i) for i in file.read().strip().split(',')]
    
    day = 1

    while day <= final_day:
        fish_set_copy = fish_set
        
        for i in range(len(fish_set_copy)):
            if fish_set_copy[i] > 0:
                fish_set[i] -= 1
            else:
                fish_set[i] = 6
                fish_set.append(8)

        day += 1

    print(len(fish_set))