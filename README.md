# Advent_of_Code_2021

| Day | Title | Takeaways |
| ---- | ---------------- | ---------------------- |
| 1 | Sonar Sweep | 1. In *Python*, `file.read()` returns the entire content of file as a string, whereas `file.readlines()` returns a list where each item is a line from file<br>2. `string.strip()` returns a copy of the string with both leading and trailing characters removed |
| 2 | Dive | 1. Using `.replace()` and `.split()` to split the input by two delimiters and store the resulting input into a list |
| 3 | Binary Diagnostic | 1. `Part 1` uses comprehension to count the number of ones and the number of zeros in each bit position<br>2. `int(string, 2)` converts a binary string to a decimal integer<br>3. `Part 2` implements recursion to solve the puzzle<br>4. *CAVEAT:* If we declare two lists as `A = B = []` in *Python*, and even if we just modify list `A` later, the list `B` will be modified accordingly |
