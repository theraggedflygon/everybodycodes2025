def add_complex(c1, c2):
     return [c1[0] + c2[0], c1[1] + c2[1]]

def multiply_complex(c1, c2):
     return [c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c2[0] * c1[1]]

def divide_complex(c1, c2):
     return [int(c1[0] / c2[0]), int(c1[1] / c2[1])]

with open("quest2-3.txt", "r") as file:
     n1, n2 = file.read().split(",")

     A = [int(n1), int(n2)]

CYCLES = 100
trial_A = [A[0], A[1]]
score = 0
for i in range(1001):
     print(i)
     row_str = ""
     for j in range(1001):
          result = [0, 0]
          point = True
          for cycle in range(CYCLES):
               result = multiply_complex(result, result)
               result = divide_complex(result, [100000, 100000])
               result = add_complex(result, trial_A)

               if result[0] > 1000000 or result[1] > 1000000 or result[0] < -1000000 or result[1] < -1000000:
                    point = False
                    break
          if point:
               score += 1
               row_str += 'X'
          else:
               row_str += "."
          trial_A[1] += 1
     trial_A[1] = A[1]
     trial_A[0] += 1

print(score)
