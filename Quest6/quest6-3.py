DISTANCE_LIMIT = 1000
REPEATS = 1000

with open("quest6-3.txt", "r") as file:
     data = file.read()

total_score = 0
start_teachers = {}
for i in range(DISTANCE_LIMIT):
     char = data[i]
     if char.isupper():
          if char in start_teachers:
               start_teachers[char] += 1
          else:
               start_teachers[char] = 1

for i in range(DISTANCE_LIMIT):
     char = data[i]
     to_add = data[i + DISTANCE_LIMIT]
     if to_add.isupper():
          if to_add in start_teachers:
               start_teachers[to_add] += 1
          else:
               start_teachers[to_add] = 1
     if char.islower():
          if char.upper() in start_teachers:
               total_score += start_teachers[char.upper()]


end_teachers = {}
for i in range(1, DISTANCE_LIMIT):
     char = data[-(i + 1)]
     if char.isupper():
          if char in end_teachers:
               end_teachers[char] += 1
          else:
               end_teachers[char] = 1

for i in range(1, DISTANCE_LIMIT + 1):
     char = data[-i]
     to_add = data[-(i + DISTANCE_LIMIT)]
     if to_add.isupper():
          if to_add in end_teachers:
               end_teachers[to_add] += 1
          else:
               end_teachers[to_add] = 1
     if char.islower():
          if char.upper() in end_teachers:
               total_score += end_teachers[char.upper()]


teachers = {}
for i in range(-DISTANCE_LIMIT - 1, DISTANCE_LIMIT):
     char = data[i]
     if char.isupper():
          if char in teachers:
               teachers[char] += 1
          else:
               teachers[char] = 1


score = [0 for _ in range(len(data))]
for idx, char in enumerate(data):
     to_add = data[(idx + DISTANCE_LIMIT) % len(data)]
     if to_add.isupper():
          if to_add in teachers:
               teachers[to_add] += 1
          else:
               teachers[to_add] = 1

     to_remove = data[(idx - DISTANCE_LIMIT - 1) % len(data)]
     if to_remove.isupper():
          teachers[to_remove] -= 1

     if char.islower():
          if char.upper() in teachers:
               score[idx] = teachers[char.upper()]

for i in range(len(data)):
     if i - DISTANCE_LIMIT < 0 or i + DISTANCE_LIMIT >= len(data):
          total_score += (REPEATS - 1) * score[i]
     else:
          total_score += REPEATS * score[i]

print(total_score)