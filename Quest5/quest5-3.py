class Node:
     def __init__(self, value, sword_id):
          self.value = value
          self.left = None
          self.bottom = None
          self.right = None
          self.id = sword_id

     def get_quality(self):
          vals = [self.value]
          current = self
          while current.bottom is not None:
               current = current.bottom
               vals.append(current.value)
          
          return int("".join([str(val) for val in vals]))
     
     def get_level(self):
          level_str = ""
          if self.left is not None:
               level_str += str(self.left.value)
          level_str += str(self.value)
          if self.right is not None:
               level_str += str(self.right.value)
          
          return int(level_str)


with open("quest5-3.txt", "r") as file:
     data = file.read().split("\n")


heads = []
for row in data:
     sword_id, nodes = row.split(":")
     sword_id = int(sword_id)
     nodes = [int(num) for num in nodes.split(",")]
     head = Node(nodes[0], sword_id)
     for node in nodes[1:]:
          current = head
          while True:
               if node < current.value and current.left is None:
                    current.left = Node(node, sword_id)
                    break
               elif node > current.value and current.right is None:
                    current.right = Node(node, sword_id)
                    break
               elif current.bottom is not None:
                    current = current.bottom
               else:
                    current.bottom = Node(node, sword_id)
                    current = current.bottom
                    break
          
     current = head
     spine = [current.value]     

     while current.bottom is not None:
          current = current.bottom
          spine.append(current.value)

     heads.append(head)


def compare_swords(s1, s2):
     if s1.get_quality() > s2.get_quality():
          return 1
     elif s1.get_quality() < s2.get_quality():
          return -1
     else:
          l1 = s1
          l2 = s2
          while True:
               if l1.get_level() > l2.get_level():
                    return 1
               elif l2.get_level() > l1.get_level():
                    return -1
               elif l1.bottom is None or l2.bottom is None:
                    break
               else:
                    l1 = l1.bottom
                    l2 = l2.bottom
     
     if l1.id > l2.id:
          return 1
     else:
          return -1


sorted_swords = []
for i in range(1, len(heads)):
     sword = heads[i]
     j = i - 1
     while j >= 0 and compare_swords(sword, heads[j]) > 0:
          heads[j + 1] = heads[j]
          j -= 1
     heads[j + 1] = sword

total = 0
for idx, head in enumerate(heads):
     total += (idx + 1) * head.id

print(total)
