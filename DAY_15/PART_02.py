"""
1. Read the input from the text and store it into a 2D list
2. Get the boundary of the 2D list and multiply by 5
3. Declare a heap called heap with [(0,0,0)] as the initial element, which represents coordinate (0, 0) with risk value of 0
4. Declare a defaultdict called risk
5. Declare a set called visited_vertices
6. While the heap is not empty:
    1. Pop up the first element from the heap
    2. If the element is in the visited_vertices set: Continue to the next iteration
    3. If the element is the bottom-right element, break out of the while loop
    4. Store the element into the visited_vertices set
    5. Update the risk dictionary with (row, col)-> risk_value
    6. Loop through the neighbour vertices around the current element:
        1. If the neighbour vertex is out of bound: Continue to the next loop
        2. Push the row, col, and accumulated risk value into the heap
8. Print out the risk_value
"""

from collections import defaultdict
import heapq

if __name__ == "__main__":
    with open("./DAY_15/input.txt") as file:
        cavern = [[int(i) for i in line] for line in file.read().strip().splitlines()]

    boundary = len(cavern)
    total_boundary = boundary * 5

    heap = [(0, 0, 0)]

    # Transform list into a heap, in-place, in linear time.
    heapq.heapify(heap)

    risk = defaultdict(int)
    visited_vertices = set()

    while heap:
        risk_value, row, column = heapq.heappop(heap) # Pop and return the smallest element from the heap

        if (row, column) in visited_vertices: 
            continue

        visited_vertices.add((row, column))
        
        risk[(row, column)] = risk_value

        if row == total_boundary - 1 and column == total_boundary - 1: 
            break

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr = row + dr
            cc = column + dc
            if not (0 <= rr < total_boundary and 0 <= cc < total_boundary): 
                continue
            
            temp = cavern[rr % boundary][cc % boundary] + (rr // boundary) + (cc // boundary)
            value = (temp - 1) % 9 + 1
            heapq.heappush(heap, (risk_value + value, rr, cc))

    print(f"The lowest total risk of any path from the top left to the bottom right is: {risk[(total_boundary - 1, total_boundary - 1)]}")