with open("quest3-2.txt", "r") as file:
     crates = [int(num) for num in file.read().split(",")]

single_crates = list(set(crates))
single_crates.sort()

print(sum(single_crates[:20]))