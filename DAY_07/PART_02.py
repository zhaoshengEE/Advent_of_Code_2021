"""
Algorithm:
1. Read the input from the text document and store them into a Counter
2. Declare a variable called min_fule with initial value of float('inf')
3. Iterate from 0 to the maximum key of the Counter:
    1. Initialize a variable called fuel with value of 0
    2. Iterate through key-value pairs of the Counter:
        1. Add the fuel needed to the variable fuel by applying the sum of arithmetic sequence
    3. Assign the minimum between fuel and min_fuel to min_fuel
4. Print out min_fuel
"""

from collections import Counter

if __name__ == "__main__":
    with open("./DAY_07/input.txt") as file:
        position = [int(i) for i in file.read().strip().split(',')]
        position = Counter(position)
    
    min_fuel = float('inf')

    for k in range(max(position.keys()) + 1):
        fuel = 0

        for key, value in position.items():
            step = abs(k - key)
            fuel += ((((1 + step) * step) // 2) * value)
        
        min_fuel = min(min_fuel, fuel)

    print(f"The minimum fuel is {min_fuel}")