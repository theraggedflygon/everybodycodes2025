def gen_cache_string(positions, dragon, turn):
     return turn + str(dragon) + str(positions)

def count_sequences(positions, dragon, turn):
     if gen_cache_string(positions, dragon, turn) in CACHE:
          return CACHE[gen_cache_string(positions, dragon, turn)]
     
     if turn == 's':
          total = 0
          moves = 0
          for i in range(len(positions)):
               # no sheep in column
               if positions[i] is None:
                    continue
               # sheep is free
               if positions[i] + 1 == len(GRID):
                    moves += 1
                    continue
               if [positions[i] + 1, i] in HIDEOUTS or dragon[1] != i or dragon[0] != positions[i] + 1:
                    new_positions = positions.copy()
                    new_positions[i] += 1
                    moves += 1
                    total += count_sequences(new_positions, dragon, 'd')
          if moves == 0:
               total += count_sequences(positions, dragon, 'd')
          CACHE[gen_cache_string(positions, dragon, turn)] = total
          return total
     elif turn == 'd':
          total = 0
          for row_delta, col_delta in DRAGON_MOVES:
               new_dragon = [dragon[0] + row_delta, dragon[1] + col_delta]
               # check if new dragon is in bounds
               if 0 <= new_dragon[0] < len(GRID) and 0 <= new_dragon[1] < len(GRID[0]):
                    new_positions = positions.copy()
                    if new_dragon not in HIDEOUTS and positions[new_dragon[1]] == new_dragon[0]:
                         new_positions[new_dragon[1]] = None
                         if new_positions.count(None) == len(new_positions):
                              total += 1
                              continue
                    total += count_sequences(new_positions, new_dragon, 's')
          CACHE[gen_cache_string(positions, dragon, turn)] = total
          return total

DRAGON_MOVES = [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
with open("quest10-3.txt", "r") as file:
     GRID = file.read().split("\n")

start_sheep = [None for _ in range(len(GRID[0]))]
HIDEOUTS = []
for i in range(len(GRID)):
     for j in range(len(GRID[0])):
          if GRID[i][j] == 'D':
               start_dragon = [i, j]
          elif GRID[i][j] == 'S':
               start_sheep[j] = i
          elif GRID[i][j] == '#':
               HIDEOUTS.append([i, j])

CACHE = dict()
sequences = count_sequences(start_sheep, start_dragon, 's')
print(sequences)
