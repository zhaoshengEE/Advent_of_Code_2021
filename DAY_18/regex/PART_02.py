import re, math
from typing import Match

PAIR = re.compile(r'\[(\d+),(\d+)\]')
NUMBER_LEFT = re.compile(r'\d+(?!.*\d)')
NUMBER = re.compile(r'\d+')
GREATER_OR_EQUAL_10 = re.compile(r'\d\d+')

def add(s1, s2):
    return f'[{s1},{s2}]'

def reduce(s):
    while True:
        continue_outer = False
        for pair in PAIR.finditer(s):
            before = s[:pair.start()]
            if before.count('[') - before.count(']') >= 4:
                def left_cb(match):
                    return str(int(match[0]) + int(pair[1]))

                def right_cb(match):
                    return str(int(match[0]) + int(pair[2]))

                start = NUMBER_LEFT.sub(left_cb, s[:pair.start()], count = 1)
                end = NUMBER.sub(right_cb, s[pair.end():], count = 1)
                s = f'{start}0{end}'

                continue_outer = True
                break

        if continue_outer:
            continue

        GREATER_OR_EQUAL_10_match = GREATER_OR_EQUAL_10.search(s)
        if GREATER_OR_EQUAL_10_match:
            def match_cb(match: Match[str]) -> str:
                val = int(match[0])
                return f'[{math.floor(val/2)},{math.ceil(val/2)}]'

            s = GREATER_OR_EQUAL_10.sub(match_cb, s, count = 1)
            continue

        return s

def magnitude(s):
    def compute_value(value):
        if isinstance(value, int): return value
        else: return 3 * compute_value(value[0]) + 2 * compute_value(value[1])
    
    return compute_value(eval(s))

if __name__ == "__main__":
    with open("./DAY_18/input.txt") as file:
        input = [line for line in file.read().strip().splitlines()]
    
    result = float("-inf")

    for x in range(len(input)):
        for y in range(len(input)):
            if x == y: continue
            else: result = max(result, magnitude(reduce(add(input[x], input[y]))))
    
    print(f"The largest magnitude of any sum of two different snailfish numbers from the homework assignment is: {result}")
    
