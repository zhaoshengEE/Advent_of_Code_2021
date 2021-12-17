"""
1. Read the input from the text and convert it to binary string
2. Use Recursion:
    1. (Base case 1) If data is 0 or empty: Return 0
    2. (Base case 2) If the subpacket is all founded: Return getVersionSum(data, -1)
    3. Fetch the version and typeID from the data
    4. (Recursion 1) If the typeID is 4:
                        1. Set the initial index with 6
                        2. Set binary_string as empty
                        3. While True:
                            1. If data[index] == 0:
                                1. Add the next 4 bits to the string
                                2. Break out the while loop
                            2. Add the next 4 bits to the string
                            3. Increment the index by 5
                        4. Return the ver + getVersionSum(data[index:], -1)
    5. Fetch the lengthID
    6. (Recursion 2) If the lengthID is 0:
                        1. Fetch the number_of_bits
                        2. Return version + getVersionSum(number_of_bits) + getVersionSum(remaining)
    7. (Recursion 3) Else:
                        1. Fetch the number_of_sub_packets
                        2. Return version + getVersionSum(number_of_sub_packets)
"""

def getVersionSum(data, packet_remaining = -1):
    if data == "" or int(data) == 0: return 0

    if packet_remaining == 0:
        return getVersionSum(data, -1)

    version = int(data[0:3], base = 2)
    typeID = int(data[3:6], base = 2)

    if typeID == 4:
        index = 6
        binary_string = ""
        found_end = False
        while found_end == False:
            if data[index] == "0":
                found_end = True

            binary_string += data[index + 1: index + 5]
            index += 5

        return version + getVersionSum(data[index:], packet_remaining - 1)
    
    lengthID = data[6]

    if lengthID == "0":
        number_of_bits = int(data[7:22], base = 2)
        return version + getVersionSum(data[22:22 + number_of_bits], -1) + getVersionSum(data[22 + number_of_bits:], packet_remaining - 1)

    else:
        number_of_subpackets = int(data[7:18], base = 2)
        return version + getVersionSum(data[18:], number_of_subpackets)


if __name__ == "__main__":
    with open("./DAY_16/input.txt") as file:
        data_hex = file.read().strip()
        # Python’s zfill function will add 0’s to a string if that string is less than the specified value in length
        data = str(bin(int(data_hex, base=16)))[2:]
        data = data.zfill(len(data_hex) * 4)

    print(getVersionSum(data))