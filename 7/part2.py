import sys
import os
from string import ascii_uppercase

inputfile=os.path.join(sys.path[0],sys.argv[1])
with open(inputfile) as f:
  lines = f.readlines()

nbr_of_workers = int(sys.argv[2])
time_base = int(sys.argv[3])

instructions = []
nodes = {}
remaining_work = {node : duration for duration, node in enumerate(ascii_uppercase, start=time_base+1)}
workers = {worker : None for worker in range(1, nbr_of_workers+1)}
rounds = 0

for line in lines:
  before = line[5]
  after = line[36]
  instructions.append((before,after))
  nodes[before] = []
  nodes[after] = []

for instruction in instructions:
  before, after = instruction
  nodes[after].append(before)

def no_parents_not_started():
  keys = []
  for node, parent_list in nodes.items():
    if not parent_list and not node in workers.values():
      keys.append(node)
  return keys


def remove_node(node):
  del nodes[node]
  for parent_list in nodes.values():
    if node in parent_list:
      parent_list.remove(node)

def work():
  for node in workers.values():
    if node:  
      remaining_work[node] -=1
  global rounds
  rounds +=1

def remove_finished_nodes():
  for worker, node in workers.items():
    if node and remaining_work[node] == 0:
      remove_node(node)
      workers[worker] = None

def get_worker():
  for worker, node in workers.items():
    if not node:
      return worker

def assign_work(assignable_nodes_list):
  assignable_nodes_list.sort(reverse=True)
  while(assignable_nodes_list):
    worker = get_worker()
    if not worker:
      return
    node = assignable_nodes_list.pop()
    workers[worker] = node
  
def busy_workers():
  for node in workers.values():
    if node:
      return True
  return False

while(True):
  assignable_nodes_list = no_parents_not_started()
  if not assignable_nodes_list and not busy_workers():
    break
  assign_work(assignable_nodes_list)
  work()
  remove_finished_nodes()

print(rounds)
