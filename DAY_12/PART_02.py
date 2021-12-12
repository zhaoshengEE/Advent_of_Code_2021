"""
1. Declare a defaultdict named LUT(Look-Up Table), with the type of value as list
2. Read the input from the text document line by line, store the input into a list called lines
3. Declare a Queue with (["start", set(["start"]), False]) at the front
4. Initialize a counting variable with value of 0
5. While the Queue is not empty:
    1. Pop out the front element from the Queue
    2. If the current element is "end":
        1. Increment the counting variable by 1
        2. Continue to the next loop
    3. Loop through the LUT given the current element as key:
        1. If the current value is not in the current_set:
            1. Copy the current_set into new_set
            2. If the current value is lowercase:
                1. Add the current value into the new_set
            3. Append the (current value, new_set, False) into the Queue
        2. Else if the current_flag is False and current value is not "start" or "end":
            1. Append the (current value, current_set, True) into the Queue
6. Print out the value of counting variable
"""

from collections import defaultdict, deque

if __name__ == "__main__":
    LUT = defaultdict(list)

    for line in open("./DAY_12/input.txt"):
        a, b = line.strip().split('-')
        LUT[a].append(b)
        LUT[b].append(a)
    
    Queue = deque([("start", set(["start"]), False)])
    count = 0

    while Queue:
        current_point, current_set, current_flag = Queue.popleft()
        
        if current_point == "end":
            count += 1
            continue
            
        for next_point in LUT[current_point]:
            if next_point not in current_set:
                next_set = current_set.copy()
                
                if next_point.islower():
                    next_set.add(next_point)
                
                Queue.append((next_point, next_set, current_flag))
            
            elif current_flag == False and next_point not in ["start", "end"]:
                Queue.append((next_point, current_set, True))

    
    print(f"The number of paths through this cave system: {count}")