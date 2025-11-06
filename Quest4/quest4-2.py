import math

with open("quest4-2.txt", "r") as file:
     data = file.read()

gears = [int(gear) for gear in data.split("\n")]

prev_rotations = 1
for i in range(1, len(gears)):
     ratio = gears[i - 1] / gears[i]
     prev_rotations *= ratio

NEEDED = 10000000000000

print(math.ceil(NEEDED / prev_rotations))