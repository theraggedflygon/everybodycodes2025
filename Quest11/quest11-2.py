def check_cols(cols):
     if cols.count(cols[0]) == len(cols):
          return True
     return False

with open("quest11-2.txt", "r") as file:
     data = file.read().split("\n")

cols = [int(num) for num in data]

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
          if check_cols(cols):
               break
     if check_cols(cols):
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
          if check_cols(cols):
               break
     if round == check_cols(cols):
          break

print(round)