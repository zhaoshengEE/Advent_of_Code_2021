"""
1. Read the input from the text and convert it to binary string
2. Use Recursion:
    1. (Base case 1) If start index is equal to the end index: Return None
    2. (Base case 2) If the start index is greater than the len(data) - 4: Return getVersionSum(data, -1)
    3. Fetch the typeID from the data
    4. (Recursion 1) If the typeID is 4:
                        1. Set the initial index with 6
                        2. Set binary_string as empty
                        3. While True:
                            1. If data[index] == 0:
                                1. Add the next 4 bits to the string
                                2. Break out the while loop
                            2. Add the next 4 bits to the string
                            3. Increment the index by 5
                        4. Convert the binary string into value in decimal
                        5. Return value and index
    5. Fetch the lengthID
    6. (Recursion 2) If the lengthID is 0:
                        1. Fetch the number_of_bits
                        2. Append values to subpackets
    7. (Recursion 3) Else:
                        1. Fetch the number_of_sub_packets
                        2. Append values to subpackets
    8. Operate according to the TypeID
"""

def compute(data, start, end = -1):
    if start == end or start > len(data) - 4: return None, None

    typeID = int(data[start + 3:start + 6], base = 2)

    if typeID == 4:
        start += 6
        binary_string = ""
        found_end = False
        while found_end == False:
            if data[start] == "0":
                found_end = True

            binary_string += data[start + 1: start + 5]
            start += 5
        
        value = int(binary_string, base = 2)
        
        return value, start
    
    lengthID = data[start + 6]
    subpakcets = []

    if lengthID == "0":
        number_of_bits = int(data[start + 7:start + 22], base = 2)
        end = start + 22 + number_of_bits
        start = start + 22

        while start != None:
            pre_start = start
            value, start = compute(data, start, end)
            subpakcets.append(value)
        subpakcets = subpakcets[:-1]
        start = pre_start

    else:
        number_of_subpackets = int(data[start + 7:start + 18], base = 2)
        start = start + 18

        while number_of_subpackets != 0:
            value, start = compute(data, start)
            subpakcets.append(value)
            number_of_subpackets -= 1
    
    if typeID == 0: return sum(subpakcets), start
    
    elif typeID == 1:
        product = 1
        for value in subpakcets:
            product *= value
        return product, start
    
    elif typeID == 2: return min(subpakcets), start

    elif typeID == 3: return max(subpakcets), start

    elif typeID == 5: return int(subpakcets[0] > subpakcets[1]), start

    elif typeID == 6: return int(subpakcets[0] < subpakcets[1]), start

    elif typeID == 7: return int(subpakcets[0] == subpakcets[1]), start



if __name__ == "__main__":
    with open("./DAY_16/input.txt") as file:
        data_hex = file.read().strip()
        # Python’s zfill function will add 0’s to a string if that string is less than the specified value in length
        data = str(bin(int(data_hex, base=16)))[2:]
        data = data.zfill(len(data_hex) * 4)

    print(compute(data, 0)[0])