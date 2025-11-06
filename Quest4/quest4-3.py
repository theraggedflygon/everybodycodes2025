import math

with open("quest4-3.txt", "r") as file:
     data = file.read().split("\n")

gears = []
for row in data:
     if '|' in row:
          num1, num2 = row.split("|")
          gears.append([int(num1), int(num2)])
     else:
          gears.append([int(row)])


ROTATIONS = 100
prev_rotations = ROTATIONS
for i in range(1, len(gears)):
     out_teeth = gears[i - 1][-1]
     in_teeth = gears[i][0]

     ratio = out_teeth / in_teeth
     prev_rotations *= ratio

print(int(prev_rotations))