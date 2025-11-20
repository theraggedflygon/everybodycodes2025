import math

with open("quest11-3.txt", "r") as file:
     data = file.read().split("\n")

cols = [int(num) for num in data]

total = 0
for i in range(len(cols) - 1):
     diff = cols[i] - cols[i + 1]
     total += math.ceil(abs(diff) / 2)

print(total)