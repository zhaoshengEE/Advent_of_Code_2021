"""
Algorithm:
1. Read the input from the text document:
    1. Split by '/n' first and by ' | ' and then store into pairs
2. Declare a variable named final_sum with initial value of 0
3. Loop through pairs:
    1. Assign current pair[0] and pair[1] and split by whitespace to two variables named patterns and digits
    2. Declare two empty dictinaries number_to_pattern and pattern_to_number and the current_number with initial value of 0
    3. Figure out which letter strings have the length of 2, 3, 4, 7 first, and store the pattern into number_to_letter dict:
        (For reference only, not in the codework
         1. If it is 2, number_to_pattern[1] = pattern
         2. Else If it is 3, number_to_pattern[7] = pattern
         3. ElseIf it is 4, number_to_pattern[4] = pattern
         4. Else, number_to_pattern[8] = pattern)
    4. Then, find out the patterns with length 6, store the result into a variable called pattern_len_6
    5. Find out number 6 from pattern_len_6
    6. Then find out number 9 from pattern_len_6, and the rest is 0
    7. After that find out the patterns with length 6, store the result into a variable called pattern_len_5
    8. Find out number 5 from pattern_len_5
    9. Then find out 3 from pattern_len_5, and the rest is 2
    10. Invert the number_to_pattern to pattern_to_number
    11. Find the digit number in current digit and sum up. Add the sum to the variable final_sum
4. Print out sum
"""

if __name__ == "__main__":
    with open("./DAY_08/input.txt") as file:
        pairs = [line.split(' | ') for line in file.read().strip().splitlines()]

    final_sum = 0

    for pair in pairs:
        patterns = [''.join(sorted(pattern)) for pattern in pair[0].split()]
        digits = [''.join(sorted(digit)) for digit in pair[1].split()]

        number_to_pattern = {}
        pattern_to_number = {}
        current_number = 0

        number_to_pattern[1] = [pattern for pattern in patterns if len(pattern) == 2][0]
        number_to_pattern[7] = [pattern for pattern in patterns if len(pattern) == 3][0]
        number_to_pattern[4] = [pattern for pattern in patterns if len(pattern) == 4][0]
        number_to_pattern[8] = [pattern for pattern in patterns if len(pattern) == 7][0]

        pattern_len_6 = {pattern for pattern in patterns if len(pattern) == 6}
        number_to_pattern[6] = [pattern for pattern in pattern_len_6 if len(set(pattern) & set(number_to_pattern[1])) == 1][0]
        number_to_pattern[9] = [pattern for pattern in pattern_len_6 if len(set(pattern) & set(number_to_pattern[4])) == 4][0]
        number_to_pattern[0] = list(pattern_len_6 - {number_to_pattern[6], number_to_pattern[9]})[0]

        pattern_len_5 = {pattern for pattern in patterns if len(pattern) == 5}
        number_to_pattern[5] = [pattern for pattern in pattern_len_5 if len(set(pattern) & set(number_to_pattern[6])) == 5][0]
        number_to_pattern[3] = [pattern for pattern in pattern_len_5 if len(set(pattern) & set(number_to_pattern[1])) == 2][0]
        number_to_pattern[2] = list(pattern_len_5 - {number_to_pattern[5], number_to_pattern[3]})[0]

        pattern_to_number = {value : key for key, value in number_to_pattern.items()}
        
        for digit in digits:
            current_number = (10 * current_number + pattern_to_number[digit])

        final_sum += current_number

    print(f"The sum of output values is {final_sum}")