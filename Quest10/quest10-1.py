MOVES = 4

def move_dragon(dragon, remaining):
     print(dragon)
     if dragon in sheep:
          hits.add(str(dragon))

     if remaining == 0:
          return
     
     options = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
     for row_delta, col_delta in options:
          new_dragon = [dragon[0] + row_delta, dragon[1] + col_delta]
          if 0 <= new_dragon[0] < len(grid) and 0 <= new_dragon[1] < len(grid[0]):
               move_dragon(new_dragon, remaining - 1)

with open("quest10-1.txt", "r") as file:
     grid = file.read().split("\n")

dragon = [None, None]
sheep = []
hits = set()
for i in range(len(grid)):
     for j in range(len(grid)):
          if grid[i][j] == 'D':
               dragon = [i, j]
          elif grid[i][j] == 'S':
               sheep.append([i, j])

move_dragon(dragon, MOVES)
print(len(hits))
