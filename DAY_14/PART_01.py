"""
1. Declare a defaultdict called components to store the current pairs with initial value of 0
2. Decalre a defaultdict called counter to store the number of occurrences for each letter with initial value of 0
3. Declare two empty lists called pairs and letters
4. Read the input from the text, split by the empty line into two variables called template and rules:
    1. Loop through the template to update the components and counter
    2. Loop through the rules to store each insertion pair and letter into the two empty lists
5. Loop through 10 times:
    1. Copy the components dictionary to the new_components dictionary
    2. Loop through the combination of pairs and letters:
        1. If the current pair does not exist in the components dictionary:
            1. Continue to next iteration directly
        2. Fetch the number of occurrences of the current pair in the components dictionary into count
        3. Store the pair[0] + letter and letter + pair[1] into the new_components dictionary with count times
        4. counter[letter] += count
        5. Decrement the occurrences of the current pair in new_components dictionary by count
        6. If the occurences of the current pair in new_components dictionary is 0:
            1. Pop out the current pair from the new_components dictionary
    3. Copy the new_components dictionary to the components dictionary
6. Print out the difference between the maximum and minimum of components' values
"""

from collections import defaultdict

STEP = 10

if __name__ == "__main__":
    components = defaultdict(int)
    counter = defaultdict(int)
    pairs = []
    letters = []

    with open("./DAY_14/input.txt") as file:
        template, rules = file.read().strip().split('\n\n')
        
        for i in range(len(template) - 1):
            counter[template[i]] += 1
            components[template[i] + template[i + 1]] += 1
        counter[template[len(template) - 1]] += 1
        
        for rule in rules.splitlines():
            pairs.append(rule[0:2])
            letters.append(rule[-1])

    for _ in range(STEP):
        new_components = components.copy()
        for (pair, letter) in zip(pairs, letters):
            if components.get(pair, 0) == 0:
                continue
            else:
                count = components[pair]
                new_components[pair[0] + letter] += count
                new_components[letter + pair[1]] += count
                counter[letter] += count
                new_components[pair] -= count

                if new_components[pair] == 0:
                    new_components.pop(pair)

        components = new_components.copy()

    print(f"The difference between the quantity of the most common element and the quantity of the least common element is: {max(counter.values()) - min(counter.values())}")