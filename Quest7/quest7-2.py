with open("quest7-2.txt", "r") as file:
     names, rules = file.read().split("\n\n")

names = names.split(",")
next_char = {}
for rule in rules.split("\n"):
     current, nexts = rule.split(" > ")
     next_char[current] = nexts.split(",")

total = 0
for idx, name in enumerate(names):
     trigger = False
     for i in range(len(name) - 1):
          if name[i + 1] not in next_char[name[i]]:
               trigger = True
               break
     if not trigger:
          total += (idx + 1)

print(total)