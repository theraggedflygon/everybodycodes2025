MOVES = 20

def move_dragon(dragon):
     targets = []
     options = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
     for row_delta, col_delta in options:
          new_dragon = [dragon[0] + row_delta, dragon[1] + col_delta]
          if 0 <= new_dragon[0] < len(grid) and 0 <= new_dragon[1] < len(grid[0]):
               targets.append(new_dragon)
     return targets


with open("quest10-3.txt", "r") as file:
     grid = file.read().split("\n")

dragon = [None, None]
dragons = [None for _ in range(MOVES + 1)]

sheep = [None for _ in range(MOVES + 1)]
hideouts = []

hits = set()
start_sheep = []
for i in range(len(grid)):
     for j in range(len(grid)):
          if grid[i][j] == 'D':
               dragon = [i, j]
          elif grid[i][j] == 'S':
               start_sheep.append([i, j])
          elif grid[i][j] == '#':
               hideouts.append([i, j])

dragons[0] = [dragon]
sheep[0] = start_sheep

for i in range(1, MOVES + 1):
     all_hits = []
     for dragon in dragons[i - 1]:
          dragon_hits = move_dragon(dragon)
          for hit in dragon_hits:
               if hit not in all_hits:
                    all_hits.append(hit)
     dragons[i] = all_hits
     sheep[i] = [[s1 + 1, s2] for s1, s2 in sheep[i - 1]]

dead_sheep = set()
for i in range(1, MOVES + 1):
     print(i, len(dead_sheep))
     for dragon in dragons[i]:
          if dragon not in hideouts and dragon in sheep[i - 1]:
               original_sheep = [dragon[0] - (i - 1), dragon[1]]
               dead_sheep.add(str(original_sheep))
          if dragon not in hideouts and dragon in sheep[i]:
               original_sheep = [dragon[0] - i, dragon[1]]
               dead_sheep.add(str(original_sheep))

print(len(dead_sheep))
