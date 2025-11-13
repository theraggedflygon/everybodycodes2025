NAILS = 32

with open("quest8-1.txt", "r") as file:
     nails = [int(num) for num in file.read().split(",")]

total = 0
for i in range(1, len(nails)):
     if abs(nails[i] - nails[i - 1]) == NAILS // 2:
          total += 1
     
print(total)