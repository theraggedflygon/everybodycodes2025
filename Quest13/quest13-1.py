SPINS = 2025

with open("quest13-1.txt", "r") as file:
    nums = [int(num) for num in file.read().split("\n")]

forwards = [1]
backwards = []

for idx, num in enumerate(nums):
    if idx % 2 == 0:
        forwards.append(num)
    else:
        backwards.append(num)

circle = forwards + backwards[::-1]

print(circle[SPINS % len(circle)])
