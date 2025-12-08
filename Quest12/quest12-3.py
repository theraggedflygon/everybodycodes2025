import sys

sys.setrecursionlimit(5000)


def set_fire(row, col):
    VISITED.append([row, col])
    options = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for row_delta, col_delta in options:
        if (
            0 <= row + row_delta < len(GRID)
            and 0 <= col + col_delta < len(GRID[0])
            and [row + row_delta, col + col_delta] not in VISITED
            and GRID[row][col] >= GRID[row + row_delta][col + col_delta]
        ):
            set_fire(row + row_delta, col + col_delta)


with open("quest12-3.txt", "r") as file:
    GRID = [[int(num) for num in list(row)] for row in file.read().split("\n")]

total_explode = 0
for barrel in range(3):
    max_explode = 0
    max_position = None
    max_visited = []
    ALL_VISITED = set()
    for num in range(9, 0, -1):
        for i in range(len(GRID)):
            for j in range(len(GRID[0])):
                if GRID[i][j] != num or GRID[i][j] > 9 or str([i, j]) in ALL_VISITED:
                    continue
                VISITED = []
                set_fire(i, j)
                if len(VISITED) > max_explode:
                    max_explode = len(VISITED)
                    max_position = [i, j]
                    max_visited = VISITED
                ALL_VISITED = ALL_VISITED.union(set([str(pair) for pair in VISITED]))
    for row, col in max_visited:
        GRID[row][col] = 10
    total_explode += max_explode

print(total_explode)
