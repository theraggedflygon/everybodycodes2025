class Node:
     def __init__(self, value):
          self.value = value
          self.left = None
          self.bottom = None
          self.right = None


with open("quest5-1.txt", "r") as file:
     data = file.read()
     quality, nodes = data.split(":")

nodes = [int(num) for num in nodes.split(",")]

head = Node(nodes[0])
for node in nodes[1:]:
     current = head
     while True:
          if node < current.value and current.left is None:
               current.left = Node(node)
               break
          elif node > current.value and current.right is None:
               current.right = Node(node)
               break
          elif current.bottom is not None:
               current = current.bottom
          else:
               current.bottom = Node(node)
               current = current.bottom
               break
     
current = head
spine = [current.value]     

while current.bottom is not None:
     current = current.bottom
     spine.append(current.value)

print("".join([str(num) for num in spine]))