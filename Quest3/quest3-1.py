with open("quest3-1.txt", "r") as file:
     crates = [int(num) for num in file.read().split(",")]

max_crate = sum(set(crates))
print(max_crate)