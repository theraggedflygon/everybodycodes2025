def add_complex(c1, c2):
     return [c1[0] + c2[0], c1[1] + c2[1]]

def multiply_complex(c1, c2):
     return [c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c2[0] * c1[1]]

def divide_complex(c1, c2):
     return [c1[0] // c2[0], c1[1] // c2[1]]

with open("quest2-1.txt", "r") as file:
     n1, n2 = file.read().split(",")

     A = [int(n1), int(n2)]

CYCLES = 3
result = [0, 0]
for _ in range(CYCLES):
     result = multiply_complex(result, result)
     result = divide_complex(result, [10, 10])
     result = add_complex(result, A)

print(result)
