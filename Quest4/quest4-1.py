with open("quest4-1.txt", "r") as file:
     data = file.read()

gears = [int(gear) for gear in data.split("\n")]

ROTATIONS = 2025

prev_rotations = ROTATIONS
for i in range(1, len(gears)):
     ratio = gears[i - 1] / gears[i]
     prev_rotations *= ratio

print(int(prev_rotations))