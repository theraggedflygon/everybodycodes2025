DUCKS = 500

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


current_family = 1
sequences = ["" for _ in range(DUCKS + 1)]
family = [0 for _ in range(DUCKS + 1)]
found = [False for _ in range(DUCKS + 1)]
with open("quest9-3.txt", "r") as file:
     sequence_data = file.read().split("\n")
     for sequence in sequence_data:
          key, seq = sequence.split(":")
          sequences[int(key)] = seq

for i in range(1, len(sequences)):
     print(f"{i} out of {len(sequences)}")
     for j in range(1, len(sequences)):
          if i == j:
               continue
          for k in range(1, len(sequences)):
               if i == k or j == k or found[k]:
                    continue
               if parent_check(sequences[i], sequences[j], sequences[k]):
                    trees = [tree for tree in [family[i], family[j], family[k]] if tree != 0]
                    if len(trees) == 0:
                         family[i] = current_family
                         family[j] = current_family
                         family[k] = current_family
                         current_family += 1
                    else:
                         trees.sort()
                         for idx in [i, j, k]:
                              target_family = family[idx]
                              if target_family == trees[0]:
                                   continue
                              elif target_family == 0:
                                   family[idx] = trees[0]
                              else:
                                   for l in range(len(family)):
                                        if family[l] == target_family:
                                             family[l] = trees[0]
                    found[k] = True

family_count = [0 for _ in range(current_family + 1)]
family_score = [0 for _ in range(current_family + 1)]
for i in range(1, len(family)):
     if family[i] != 0:
          target_family = family[i]
          family_count[target_family] += 1
          family_score[target_family] += i

max_count = 0
score = 0
for i in range(1, len(family_count)):
     if family_count[i] > max_count:
          max_count = family_count[i]
          score = family_score[i]

print(score)
