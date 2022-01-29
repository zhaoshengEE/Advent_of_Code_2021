"""
Assumption: Scanner 0 is at coordiantes (0, 0, 0)

1. Read the input from the text document:
    1. Store the whole input as a list named scanners, each element in the list is a set that consists of multiple tuples
    (i.e. all the beacons' coordinates w.r.t. to the corresponding beacon)
2. Initialize a list named found, which has initial value of 0 (The list to store the scanners have found)
3. Initialize a list named unfound, which has numbers ranging from 1 to len(scanners) (The list to store the scanners have not found)
4. Initialize a list named scanners_pos, which has len(scanners) (0, 0, 0)
5. While found is not empty:
    1. Pop the last element from the list found
    2. Iterate through unfound:
        1. Try to find unfound scanner from the found one (Helper Function)
6. Print out the length of the SET scanners

Helper Function:
* Input: Two indices. One is the found scanner, the other is the unfound one*
1. Map the beacons of unfound scanner into different orientations, store the result as a set named mapped_beacons
2. Iterate through the beacons of the found scanner:
    1. Iterate through the beacons of the mapped beacons:
        1. Compute the displacement
        2. Add the displacement into the mapped_beacons, name the new coordinates as beacons
        3. If the intersection between the beacons of found scanner and the beacons is greater than 12:
            1. Assign displacement to the corresponding element in scanners_pos list
            2. Append the index of unfound scanner to the found list
            3. Remove the index of unfound scanner from the unfound list
            4. Assign beacons to the corresoonding element in scanners list
            5. Terminate the function
"""

from itertools import starmap

orientations = [
    lambda x, y, z: (x, y, z), 
    lambda x, y, z: (x, z, -y), 
    lambda x, y, z: (x, -y, -z), 
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (-x, -y, z), 
    lambda x, y, z: (-x, z, y), 
    lambda x, y, z: (-x, y, -z), 
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (y, z, x), 
    lambda x, y, z: (y, x, -z), 
    lambda x, y, z: (y, -z, -x), 
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (-y, x, z), 
    lambda x, y, z: (-y, z, -x), 
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (z, x, y), 
    lambda x, y, z: (z, y, -x), 
    lambda x, y, z: (z, -x, -y), 
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (-z, -x, y), 
    lambda x, y, z: (-z, y, x), 
    lambda x, y, z: (-z, x, -y), 
    lambda x, y, z: (-z, -y, -x)
]

def find_scanner(i, j):

    for orientation in orientations:
        mapped_beacons = set(starmap(orientation, scanners[j]))

        for x0, y0, z0 in scanners[i]:
            for xx, yy, zz in mapped_beacons:
                dx, dy, dz = x0 - xx, y0 - yy, z0 - zz
                beacons = set((x + dx, y + dy, z + dz) for x, y, z in mapped_beacons)

                if len(beacons.intersection(scanners[i])) >= 12:
                    scanners_pos[j] = (dx, dy, dz)
                    found.append(j)
                    unfound.remove(j)
                    scanners[j] = beacons
                    return
    return

with open("./DAY_19/input.txt") as file:
    scanners = list(
                set(
                    tuple(map(int, coordinate.split(','))) for coordinate in bulks.split("\n")[1:]
                    ) 
                    for bulks in file.read().strip().split("\n\n")
                )

found = [0]
unfound = set(range(1, len(scanners)))
scanners_pos = [(0, 0, 0)] * len(scanners)

while found:
    i = found.pop()
    for j in list(unfound):
        find_scanner(i, j)

max_dist = float("-inf")

for i in range(0, len(scanners_pos)):
    for j in range(i, len(scanners_pos)):
        x, y, z = scanners_pos[i]
        xx, yy, zz = scanners_pos[j]
        max_dist = max(max_dist, abs(x - xx) + abs(y - yy) + abs(z - zz))

print(f"The largest Manhattan distance between any two scanners is: {max_dist}")