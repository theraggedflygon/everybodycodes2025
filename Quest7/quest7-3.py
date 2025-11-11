MIN_LEN = 7
MAX_LEN = 11

def generate_names(prefix):
     if len(prefix) > MAX_LEN:
          return set()
     elif len(prefix) == MAX_LEN:
          return set([prefix])

     all_words = set()
     last_letter = prefix[-1]
     options = []
     if last_letter in next_char:
          options = next_char[last_letter]

     if len(prefix) >= MIN_LEN:
          all_words.add(prefix)
     for letter in options:
          all_words = all_words.union(generate_names(prefix + letter))
          
     return all_words


with open("quest7-3.txt", "r") as file:
     prefix_data, rules = file.read().split("\n\n")

prefixes = prefix_data.split(",")
next_char = {}
for rule in rules.split("\n"):
     current, nexts = rule.split(" > ")
     next_char[current] = nexts.split(",")

valid_prefixes = []
for idx, prefix in enumerate(prefixes):
     trigger = False
     for i in range(len(prefix) - 1):
          if prefix[i + 1] not in next_char[prefix[i]]:
               trigger = True
               break
     if not trigger:
          valid_prefixes.append(prefix)

all_words = set()
for prefix in valid_prefixes:
     all_words = all_words.union(generate_names(prefix))


print(len(all_words))