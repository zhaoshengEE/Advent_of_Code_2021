"""
Algorithm:
1. Read the input from the text document into two variables (data, *board_strings)
2. Store the data variable into a list called data_stream
3. Parse the board strings into 3D list variable called boards
4. Initilize an empty list to store the index of winning board (winning_list) and a bool flag (found_the_last_win) as False
5. Iterate through the data_stream:
    1. Iterate through the boards:
        1. Discard the current number from the current board (a built-in method of set)
    2. Iterate through the boards:
        1. If there exists a winner AND the board index is NOT in the winning_list:
            1. Fetch the sum of remaining numbers into a variable called sum_unmarked_data
            2. Store the current data into a variable called last_call_data
            3. Append the index to the winning_list
        2. If the length of winning list is equal to the number of boards:
            1. Set the found_the_last_win to True
            2. Break
6. Print out the product of sum_unmarked_data and last_call_data

Class Boards:
1. Initialize two class variables: one is a set of integers names remains, the other is the 2D list named grid
2. Class method: parse the board_string into a class(remains, grid)
3. Instance method: is_winner:
    1. Iterate through all the elements in the grid:
        1. If there exist a row or column that has no elements exist in the set, return True
           Else return False
4. Instance method: sum_of_remains:
    1. Sum up all the remaining elements in the set
"""

from __future__ import annotations
from typing import NamedTuple

grid_side = 5

class Board(NamedTuple):
    remains: set[int]
    grid: list[list[int]]

    @classmethod
    def parse_boards(cls, board_strings):
        nums = [[int(i) for i in board_string.split()] for board_string in board_strings.split('\n')]
        grid = [[nums[row][col]
                 for row in range(grid_side)]
                 for col in range(grid_side)]
        return cls(set.union(*map(set, nums)), grid)
    
    @property
    def is_winner(self):
        # check if there exists a winning column
        for row in range(grid_side):
            for col in range(grid_side):
                if self.grid[row][col] in self.remains:
                    break
            else:
                return True

        # check if there exists a winning row
        for col in range(grid_side):
            for row in range(grid_side):
                if self.grid[row][col] in self.remains:
                    break
            else:
                return True
        
        return False
    
    @property
    def sum_of_remains(self):
        return sum(self.remains)

if __name__ == "__main__":
    with open("./DAY_04/input.txt") as file:
        data, *board_strings = [i for i in file.read().strip().split("\n\n")]
    
    data_stream = [int(i) for i in data.split(',')]
    boards = [Board.parse_boards(board_string) for board_string in board_strings]
    sum_unmarked_data = None
    winning_list = []
    found_the_last_win = False

    for curr_data in data_stream:
        for board in boards:
            board.remains.discard(curr_data)
        
        for index, board in enumerate(boards):
            if board.is_winner and index not in winning_list:
                sum_unmarked_data = board.sum_of_remains
                last_call_data = curr_data
                winning_list.append(index)

            if len(winning_list) == len(boards):
                found_the_last_win = True
                break
        
        if sum_unmarked_data != None and found_the_last_win:
            break

    print(sum_unmarked_data * last_call_data)