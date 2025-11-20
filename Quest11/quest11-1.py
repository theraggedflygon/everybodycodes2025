with open("quest11-1.txt", "r") as file:
     data = file.read().split("\n")

cols = [int(num) for num in data]

ROUNDS = 10
round = 0
while True:
     while True:
          change = False
          for j in range(len(cols) - 1):
               if cols[j + 1] < cols[j]:
                    cols[j] -= 1
                    cols[j + 1] += 1
                    change = True
          if not change:
               break
          round += 1
          if round == ROUNDS:
               break
     if round == ROUNDS:
          break
     while True:
          change = False
          for j in range(len(cols) - 1):
               if cols[j + 1] > cols[j]:
                    cols[j] += 1
                    cols[j + 1] -= 1
                    change = True
          if not change:
               break
          round += 1
          if round == ROUNDS:
               break
     if round == ROUNDS:
          break

print(sum([(idx + 1) * val for idx, val in enumerate(cols)]))