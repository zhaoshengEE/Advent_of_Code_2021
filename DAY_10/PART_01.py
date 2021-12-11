"""
Algorithm:
1. Read the input from the text document line by line, stored the input into a list called lines
2. Initialize an Stack object called stack and a variable score called error_score with initial value of 0
3. Loop through each line in the lines:
    1. Loop through each element on each line:
        1. If the current element is an open parenthesis:
            1. Push it to the top of the stack
        2. Else:
            1. Assign score according to the close parenthesis
            2. Assign target_parenthesis according to the close parenthesis
            3. Fetch the top element from the stack
            4. If the top element is not the same with target_parenthesis
                1. Increment error_score
                2. Reset the stack
                3. Break
            5. Pop out the top element from the stack
4. Print out the error_score
"""

from STACK import Stack

open_parentheses = ['(', '[', '{', '<']
close_parentheses = [')', ']', '}', '>']
scores = [3, 57, 1197, 25137]

if __name__ == "__main__":
    with open("./DAY_10/input.txt") as file:
        lines = [line for line in file.read().strip().splitlines()]
    
    stack = Stack()
    error_score = 0

    for line in lines:
        for element in line:
            if element in open_parentheses:
                stack.push(element)
            
            else:
                score = scores[close_parentheses.index(element)]
                target_parenthesis = open_parentheses[close_parentheses.index(element)]
                last_parenthesis = stack.peek()
                
                if last_parenthesis != target_parenthesis:
                    error_score += score
                    stack.reset()
                    break
                    
                stack.pop()
    
    print(f"The total syntax error score for errors is: {error_score}")