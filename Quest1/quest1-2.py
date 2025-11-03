with open("quest1-2.txt", "r") as file:
     names, moves = file.read().split("\n\n")

names = names.split(",")
moves = moves.split(",")

idx = 0
for move in moves:
     if move[0] == 'L':
          idx -= int(move[1:])
          idx %= len(names)
     else:
          idx += int(move[1:])
          idx %= len(names)
     

print(names[idx])