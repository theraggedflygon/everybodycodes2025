with open("quest6-1.txt", "r") as file:
     data = file.read()

teacher = 0
total = 0
for char in data:
     if char == 'A':
          teacher += 1
     elif char == 'a':
          total += teacher

print(total) 