# Algorithm:
# 1. Read the data from the file as input and store the input as list, each element in the list should be string
# 2. o2 = find_oxygen(data, 0)
# 3. co2 = find_carbon_dioxide(data, 0)
# 4. Convert o2 and co2 into decimal and print their product
#
# find_oxygen(data, pos):
# 1. If len(data) == 1: return data[0]
#    Else: 
#     1. Initialize two empty lists (cache_zero, cache_one)
#     2. Initialize two counting variables with value of 0 (count_zero, count_one)
#     3. Iterate through each row of data:
#         1. If current element(i.e. data[row][pos]) is '1' : count_one += 1, cache_one.append(data[row])
#         2. Else: count_zero += 1, cache_zero.append(data[row])
#     4. If count_one >= count_zero: find_carbon_dioxide(cache_one, pos + 1)
#        Else: find_carbon_dioxide(cache_zero, pos + 1)
#
# find_carbon_dioxide(data, pos):
# 1. If len(data) == 1: return data[0]
#    Else: 
#     1. Initialize two empty lists (cache_zero, cache_one)
#     2. Initialize two counting variables with value of 0 (count_zero, count_one)
#     3. Iterate through each row of data:
#         1. If current element(i.e. data[row][pos]) is '1' : count_one += 1, cache_one.append(data[row])
#         2. Else: count_zero += 1, cache_zero.append(data[row])
#     4. If count_one >= count_zero: find_carbon_dioxide(cache_zero, pos + 1)
#        Else: find_carbon_dioxide(cache_one, pos + 1)

def find_oxygen(data, pos):
    if len(data) == 1: 
        return data[0]

    else:
        count_zero = 0 
        count_one = 0
        cache_zero = []
        cache_one = []

        for row in range(len(data)):
            if data[row][pos] == '1':
                count_one += 1
                cache_one.append(data[row])
            else:
                count_zero += 1
                cache_zero.append(data[row])

        if count_one >= count_zero:
            return find_oxygen(cache_one, pos + 1)
        else:
            return find_oxygen(cache_zero, pos + 1)


def find_carbon_dioxide(data, pos):
    if len(data) == 1: 
        return data[0]

    else:
        count_zero = 0 
        count_one = 0
        cache_zero = []
        cache_one = []

        for row in range(len(data)):
            if data[row][pos] == '1':
                count_one += 1
                cache_one.append(data[row])
            else:
                count_zero += 1
                cache_zero.append(data[row])
        
        if count_one >= count_zero:
            return find_carbon_dioxide(cache_zero, pos + 1)
        else:
            return find_carbon_dioxide(cache_one, pos + 1)


if __name__ == "__main__":
    with open("./DAY_03/input.txt") as file:
        data = [i for i in file.read().strip().split('\n')]

    o2 = find_oxygen(data, 0)
    co2 = find_carbon_dioxide(data, 0)

    print(int(o2, 2) * int(co2, 2))