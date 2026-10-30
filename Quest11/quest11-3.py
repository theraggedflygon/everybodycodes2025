import math

def phase_1_complete(test_cols):
     for i in range(1, len(test_cols)):
          if test_cols[i] < test_cols[i - 1]:
               return False
     return True

with open("quest11-3.txt", "r") as file:
     data = file.read().split("\n")

cols = [int(num) for num in data]

total = 0
while not phase_1_complete(cols):
     pass

print(total)