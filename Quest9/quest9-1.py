with open("quest9-1.txt", "r") as file:
     p1, p2, child = file.read().split("\n")

     _, p1 = p1.split(":")
     _, p2 = p2.split(":")
     _, child = child.split(":")

p1_score = 0
p2_score = 0

for i in range(len(p1)):
     if p1[i] == child[i]:
          p1_score += 1
     if p2[i] == child[i]:
          p2_score += 1

print(p1_score * p2_score)