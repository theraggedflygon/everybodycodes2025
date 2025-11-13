NAILS = 256

with open("quest8-3.txt", "r") as file:
     nails = [int(num) for num in file.read().split(",")]

edges = []
cuts = [[0 for _ in range(NAILS + 1)] for _ in range(NAILS + 1)]

knots = 0
for i in range(1, len(nails)):
     if nails[i] > nails[i - 1]:
          big = nails[i]
          small = nails[i - 1]
     else:
          big = nails[i - 1]
          small = nails[i]

     if big == NAILS:
          above = 1
     else:
          above = big + 1
     
     below = big - 1
     cuts[small][big] += 1

     while above != small:
          while below != small:
               if below < above:
                    cuts[below][above] += 1
               else:
                    cuts[above][below] += 1

               if below == 1:
                    below = NAILS
               else:
                    below -= 1
          below = big - 1
          if above == NAILS:
               above = 1
          else:
               above += 1
max_cuts = 0
for row in cuts:
     for val in row:
          if val > max_cuts:
               max_cuts = val

print(max_cuts)
