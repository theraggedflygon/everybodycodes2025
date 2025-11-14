DUCKS = 100

def parent_check(parent1, parent2, child):
     for i in range(len(parent1)):
          if parent1[i] != child[i] and parent2[i] != child[i]:
               return False
     
     return True

def calc_similarity(parent, child):
     hit = 0
     for i in range(len(parent)):
          if parent[i] == child[i]:
               hit += 1
     return hit


total = 0
sequences = ["" for _ in range(DUCKS + 1)]
found = [False for _ in range(DUCKS + 1)]
with open("quest9-2.txt", "r") as file:
     sequence_data = file.read().split("\n")
     for sequence in sequence_data:
          key, seq = sequence.split(":")
          sequences[int(key)] = seq

for i in range(1, len(sequences)):
     for j in range(1, len(sequences)):
          if i == j:
               continue
          for k in range(1, len(sequences)):
               if i == k or j == k or found[k]:
                    continue
               if parent_check(sequences[i], sequences[j], sequences[k]):
                    total += calc_similarity(sequences[i], sequences[k]) * calc_similarity(sequences[j], sequences[k])
                    found[k] = True

print(total)
