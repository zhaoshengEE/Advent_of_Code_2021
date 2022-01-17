"""
This codework is adpated from https://github.com/MasterMedo/aoc/blob/master/2021/day/18.py
"""

from dataclasses import dataclass
import math

@dataclass
class Node:
    parent: "Node" = None
    left_child: "Node" = None
    right_child: "Node" = None
    value: int = 0

    @classmethod
    def parse_list(cls, input, parent = None):
        if isinstance(input, int):
            return Node(parent = parent, value = input) 

        left, right = input
        node = Node(parent = parent)
        node.left_child = Node.parse_list(left, parent = node)
        node.right_child = Node.parse_list(right, parent = node)
        return node
   
    def __add__(self, input):  
        node = Node(left_child = self, right_child = input)
        node.left_child.parent = node
        node.right_child.parent = node
        node.explode()
        while node.split():
            node.explode()
        return node 

    def explode(self, depth = 0):
        if self.left_child is None and self.right_child is None:
            return
        
        if depth >= 4:
            self.parent.add_left(self.left_child.value, self, True)
            self.parent.add_right(self.right_child.value, self, True)
            self.value = 0
            self.left_child = None
            self.right_child = None
            return
        
        self.left_child.explode(depth + 1)
        self.right_child.explode(depth + 1)

    # Return True is split happens, otherwise return False
    def split(self):
        if self.value > 9:
            left, right = math.floor(self.value / 2), math.ceil(self.value / 2)
            self.left_child = Node(parent = self, value = left)
            self.right_child = Node(parent = self, value = right)
            self.value = 0
            return True
        
        if self.left_child is not None:
            if self.left_child.split():
                return True

        if self.right_child is not None:
            if self.right_child.split():
                return True

        return False

    def add_right(self, val, child, right=False):
        if right:
            if self.right_child is None or self.right_child is child:
                if self.parent is not None:
                    self.parent.add_right(val, self, True)
                return

            self.right_child.add_right(val, self)
            return

        if self.left_child is None:
            self.value += val
        else:
            self.left_child.add_right(val, self)

    def add_left(self, val, child, left=False):
        if left:
            if self.left_child is None or self.left_child is child:
                if self.parent is not None:
                    self.parent.add_left(val, self, True)
                return

            self.left_child.add_left(val, self)
            return

        if self.right_child is None:
            self.value += val
        else:
            self.right_child.add_left(val, self)

    def magnitude(self):
        if self.left_child is None and self.right_child is None:
            return self.value

        return 3 * self.left_child.magnitude() + 2 * self.right_child.magnitude()

if __name__ == "__main__":
    with open("./DAY_18/input.txt") as file:
        input = list(map(eval, file.readlines()))

    result = Node.parse_list(input[0])

    for line in input[1:]:
        result += Node.parse_list(line)
    
    print(f"The magnitude of the final sum is: {result.magnitude()}")