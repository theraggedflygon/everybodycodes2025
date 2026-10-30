import copy


def count_diag(row, col):
    count = 0
    if row != 0:
        if col != 0:
            if grid[row - 1][col - 1] == "#":
                count += 1
        if col != len(grid[0]) - 1:
            if grid[row - 1][col + 1] == "#":
                count += 1
    if row != len(grid) - 1:
        if col != 0:
            if grid[row + 1][col - 1] == "#":
                count += 1
        if col != len(grid[0]) - 1:
            if grid[row + 1][col + 1] == "#":
                count += 1

    return count


with open("quest14-1.txt", "r") as file:
    grid = [list(row) for row in file.read().split("\n")]

ROUNDS = 10
total = 0
for _ in range(ROUNDS):
    new_grid = copy.deepcopy(grid)
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            if grid[i][j] == "#" and count_diag(i, j) % 2 == 0:
                new_grid[i][j] = "."
            elif grid[i][j] == "." and count_diag(i, j) % 2 == 0:
                new_grid[i][j] = "#"
    grid = new_grid
    for row in grid:
        for col in row:
            if col == "#":
                total += 1

print(total)
