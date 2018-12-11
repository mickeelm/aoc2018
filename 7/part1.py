import sys
import os

inputfile=os.path.join(sys.path[0],sys.argv[1])
with open(inputfile) as f:
  lines = f.readlines()

instructions = []
nodes = {}

for line in lines:
  before = line[5]
  after = line[36]
  instructions.append((before,after))
  nodes[before] = []
  nodes[after] = []

for instruction in instructions:
  before, after = instruction
  nodes[after].append(before)

def no_parents():
  keys = []
  for node, parent_list in nodes.items():
    if not parent_list:
      keys.append(node)
  return keys

def remove_node(node):
  del nodes[node]
  for parent_list in nodes.values():
    if node in parent_list:
      parent_list.remove(node)


traversion = ''
while(True):
  no_parents_list = no_parents()
  if not no_parents_list:
    break
  node = min(no_parents_list)
  remove_node(node)
  traversion += node

print(traversion)
