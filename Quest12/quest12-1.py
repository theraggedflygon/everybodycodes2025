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


VISITED = []
with open("quest12-1.txt", "r") as file:
    GRID = file.read().split("\n")

set_fire(0, 0)

print(len(VISITED))
