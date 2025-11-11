with open("quest6-2.txt", "r") as file:
     data = file.read()

teachers = {}
total = 0
for char in data:
     if char.isupper():
          if char in teachers:
               teachers[char] += 1
          else:
               teachers[char] = 1
     else:
          if char.upper() in teachers:
               total += teachers[char.upper()]

print(total) 