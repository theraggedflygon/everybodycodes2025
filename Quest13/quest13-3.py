SPINS = 202520252025


class DialRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = abs(end - start) + 1


with open("quest13-3.txt", "r") as file:
    nums = [
        [int(num) for num in num_range.split("-")]
        for num_range in file.read().split("\n")
    ]

forwards = [DialRange(1, 1)]
backwards = []

for idx, num_range in enumerate(nums):
    num1, num2 = num_range
    if idx % 2 == 0:
        forwards.append(DialRange(num1, num2))
    else:
        backwards.append(DialRange(num2, num1))

circle = forwards + backwards[::-1]

total_length = sum([dial_range.length for dial_range in circle])
leftover_spins = SPINS % total_length
range_idx = 0
while leftover_spins >= circle[range_idx].length:
    leftover_spins -= circle[range_idx].length
    range_idx += 1

if circle[range_idx].start < circle[range_idx].end:
    print(circle[range_idx].start + leftover_spins)
else:
    print(circle[range_idx].start - leftover_spins)
