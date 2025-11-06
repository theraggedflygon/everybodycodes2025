with open("quest3-3.txt", "r") as file:
     crates = [int(num) for num in file.read().split(",")]

crate_counts = [0 for _ in range(max(crates) + 1)]
for crate in crates:
     crate_counts[crate] += 1

max_count = 0
for count in crate_counts:
     if count > max_count:
          max_count = count

print(max_count)