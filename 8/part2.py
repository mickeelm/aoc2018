import sys
import os

inputfile=os.path.join(sys.path[0],sys.argv[1])
with open(inputfile) as f:
  spaced_input = f.readline()

raw = [int(number) for number in spaced_input.split()]

def get_metadata_entries(nbr_of_metadatas):
  metadata_entries = []
  for metadata in range(nbr_of_metadatas):
    metadata_entries.append(next(iterator))
  return metadata_entries

def traverse():
  nbr_of_nodes = next(iterator)
  nbr_of_metadatas = next(iterator)
  node_values = {}
  for node in range(1, nbr_of_nodes+1):
    node_values[node] = traverse()

  value = 0
  metadatas = get_metadata_entries(nbr_of_metadatas)

  if node_values:
    for metadata in metadatas:
      if metadata in node_values:
        value += node_values[metadata]
  else:
    value = sum(metadatas)
  return value

iterator = iter(raw)
print(traverse())
