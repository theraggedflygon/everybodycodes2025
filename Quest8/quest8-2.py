with open("quest8-2.txt", "r") as file:
     nails = [int(num) for num in file.read().split(",")]

edges = []

knots = 0
for i in range(1, len(nails)):
     if nails[i] > nails[i - 1]:
          big = nails[i]
          small = nails[i - 1]
     else:
          big = nails[i - 1]
          small = nails[i]
     for edge in edges:
          if big in edge or small in edge:
               continue
          elif big > edge[0] > small and not (big > edge[1] > small):
               knots += 1
          elif big > edge[1] > small and not (big > edge[0] > small):
               knots += 1
     edges.append((nails[i - 1], nails[i]))
     
print(knots)