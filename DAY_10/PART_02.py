"""
Algorithm:
1. Read the input from the text document line by line, stored the input into a list called lines
2. Initialize an Stack object called stack
3. Declare an empty list called score_list
4. Loop through each line in the lines:
    1. Assume the current line is not corrupted
    2. Loop through each element on each line:
        1. If the current element is an open parenthesis:
            1. Push it to the top of the stack
        2. Else:
            1. Assign target_parenthesis according to the close parenthesis
            2. Fetch the top element from the stack
            3. If the top element is not the same with target_parenthesis (i.e. this is a corrupted line)
                1. Set the corrupted flag to True
                2. Reset the stack
                3. Break
            4. Pop out the top element from the stack
    3. If the corrupted flag is still False:
        1. Assign 0 to autocompletion_score
        2. While the stack is not empty:
            1. Fetch the top element from the stack
            2. Assign score according to the top element
            3. Update the autocompletion_score
            4. Pop out the top element from the stack
        3. Append autocompletion_score to the score_list
4. Sort the score_list and print out the middle value
"""

from STACK import Stack

open_parentheses = ['(', '[', '{', '<']
close_parentheses = [')', ']', '}', '>']
scores = [1, 2, 3, 4]

if __name__ == "__main__":
    with open("./DAY_10/input.txt") as file:
        lines = [line for line in file.read().strip().splitlines()]
    
    stack = Stack()
    score_list = []

    for line in lines:
        is_corrupted = False
        for element in line:
            if element in open_parentheses:
                stack.push(element)
            
            else:
                target_parenthesis = open_parentheses[close_parentheses.index(element)]
                last_parenthesis = stack.peek()
                
                if last_parenthesis != target_parenthesis:
                    is_corrupted = True
                    stack.reset()
                    break
                    
                stack.pop()

        if is_corrupted == False:
            autocompletion_score = 0

            while stack.isNotEmpty():
                last_parenthesis = stack.peek()
                score = scores[open_parentheses.index(last_parenthesis)]
                autocompletion_score = (autocompletion_score * 5 + score)
                stack.pop()

            score_list.append(autocompletion_score)
    
    score_list.sort()

    print(f"The middle score is: {score_list[len(score_list) // 2]}")