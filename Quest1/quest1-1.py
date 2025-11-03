with open("quest1-1.txt", "r") as file:
     names, moves = file.read().split("\n\n")

names = names.split(",")
moves = moves.split(",")

idx = 0
for move in moves:
     if move[0] == 'L':
          idx -= int(move[1:])
          if idx < 0:
               idx = 0
     else:
          idx += int(move[1:])
          if idx >= len(names):
               idx = len(names) - 1
     

print(names[idx])