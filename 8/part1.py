import sys
import os

inputfile=os.path.join(sys.path[0],sys.argv[1])
with open(inputfile) as f:
  spaced_input = f.readline()

raw = [int(number) for number in spaced_input.split()]
metasum = 0

def add_to_metasum(meta):
  global metasum
  metasum += meta

def traverse():
  no_nodes = next(iterator)
  no_metadatas = next(iterator)

  for node in range(no_nodes):
    traverse()
  for metadata in range(no_metadatas):
      add_to_metasum(next(iterator))

iterator = iter(raw)
traverse()
print(metasum)
