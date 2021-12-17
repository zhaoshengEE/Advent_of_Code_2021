"""
1. Read the input from the text document and extract the ranges of x and y respectively
2. Declare an empty list called max_ys
3. for y_velo in range(y_lower_bound, abs(y_lower_bound)):
    for x_velo in rangg(1, x_upper_bound):
        1. Assign x_velo, y_velo to x_velocity and y_velocity
        2. Assign 0 to x_position and y_position
        3. Loop through 2 * abs(y_lower_bound) times:
            1. Increment x_position by x_velocity
            2. Increment y_position by y_velocity
            3. If x_velocity > 0: Decrement x_velocity by 1
            4. Decrement y_velocity by 1
            5. If y_velocity is 0: Assign y_position to max_y_potential
            6. If the probe is already in the target area: 
                1. Append max_y_potential to list max_ys
                2. Break out of the loop
            7. If the probe already pasts the target area: Break out of the loop
4. Print out the maximum value in the max_ys list
"""

if __name__ == "__main__":
    with open("./DAY_17/input.txt") as file:
        input = file.read().strip()
        X, Y = input.replace("target area: ", "").split(', ')
        x_lower_bound, x_upper_bound = map(int, X.replace("x=","").split('..'))
        y_lower_bound, y_upper_bound = map(int, Y.replace("y=", "").split('..'))
    
    max_ys = []

    for y_velo in range(y_lower_bound, abs(y_lower_bound)):
        for x_velo in range(1, x_upper_bound + 1):
            
            x_velocity = x_velo
            y_velocity = y_velo

            x_position = 0
            y_position = 0
            max_y_potential = 0

            for _ in range(2 * abs(y_lower_bound)):
                x_position += x_velocity
                y_position += y_velocity

                if x_velocity > 0: x_velocity -= 1
                y_velocity -= 1

                if y_velocity == 0: max_y_potential = y_position

                if x_lower_bound <= x_position <= x_upper_bound and y_lower_bound <= y_position <= y_upper_bound:
                    max_ys.append(max_y_potential)
                    break

                if x_position > x_upper_bound or y_position < y_lower_bound: break
    
    print(f"The highest y position is: {max(max_ys)}")