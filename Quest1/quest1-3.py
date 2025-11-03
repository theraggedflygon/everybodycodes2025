class Node:
     def __init__(self, name, head, tail):
          self.name = name
          self.head = head
          self.tail = tail

     def print_cycle(self):
          print(self.head.name + '->' + self.name + "->" + self.tail.name)
          node = self.tail
          while node != self:
               print(node.head.name + '->' + node.name + "->" + node.tail.name)
               node = node.tail


with open("quest1-3.txt", "r") as file:
     names, moves = file.read().split("\n\n")

names = names.split(",")

head = None
prev_node = None
for name in names:
     new_node = Node(name, prev_node, None)
     if prev_node is not None:
          prev_node.tail = new_node
     if head is None:
          head = new_node
     prev_node = new_node

head.head = prev_node
prev_node.tail = head


moves = moves.split(",")

current_node = head
for move in moves:
     print("-----")
     current_node.print_cycle()
     target_node = current_node
     if move[0] == 'L':
          for i in range(int(move[1:])):
               target_node = target_node.head
     else:
          for i in range(int(move[1:])):
               target_node = target_node.tail

     if target_node.tail == current_node:
          current_node.head = target_node.head
          target_node.tail = current_node.tail
          current_node.head.tail = current_node
          target_node.tail.head = target_node
          current_node.tail = target_node
          target_node.head = current_node
     elif target_node.head == current_node:
          current_node.tail = target_node.tail
          target_node.head = current_node.head
          current_node.tail.head = current_node
          target_node.head.tail = target_node
          current_node.head = target_node
          target_node.tail = current_node
     else:
          old_head = current_node.head
          old_tail = current_node.tail

          current_node.head = target_node.head
          current_node.tail = target_node.tail
          current_node.head.tail = current_node
          current_node.tail.head = current_node

          target_node.head = old_head
          target_node.tail = old_tail
          target_node.head.tail = target_node
          target_node.tail.head = target_node

     current_node = target_node
     
print(current_node.name)