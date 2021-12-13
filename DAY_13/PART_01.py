"""
1. Declare an empty defaultdict called paper
2. Read the input from the text document:
    1. Split with the '\n\n' first into two variables called coordinate_part and instruction_part
    2. Loop through the coordinate_part, use each coordinate as key to update the paper with '#' 
    3. Split the instruction_part into a list called instructions
3. Loop through the instructions:
    1. Get the axis and number, convert number into integer
    2. Declare a new paper
    3. Loop through the keys in paper:
        1. If key is less than the number: 
            1. Insert the current key into the new paper
            2. Continue to the next iteration
        2. Insert the symmetric key into the new paper
    4. Copy the new paper into paper
    5. Break the loop
4. Print out the number of elements on the paper
"""

from collections import defaultdict

if __name__ == "__main__":
    paper = defaultdict(str)

    with open("./DAY_13/input.txt") as file:
        coordinates, instruction_part = file.read().strip().split('\n\n')
    
        for coordiante in coordinates.splitlines():
            x, y = map(int, coordiante.split(','))
            paper[(y, x)] = '#'
        
        instructions = [instruction.replace("fold along ", "") for instruction in instruction_part.splitlines()]

    for instruction in instructions:
        axis, number = instruction.split('=')
        number = int(number)
        new_paper = defaultdict(str)

        for (y, x) in paper.keys():            
            if axis == 'y':
                if y < number:
                    new_paper[(y, x)] = '#'
                    continue
                
                new_paper[(2 * number - y, x)] = '#'

            else:
                if x < number:
                    new_paper[(y, x)] = '#'
                    continue
                
                new_paper[(y, 2 * number - x)] = '#'
            
        paper = new_paper.copy()        
        break
    
    print(f"The number of visible dots after completing just the first fold instruction on my transparent paper: {len(paper)}")