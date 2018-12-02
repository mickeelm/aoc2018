import sys
import os

inputfile=os.path.join(sys.path[0],sys.argv[1])

with open(inputfile) as changes:
  frequency = 0
  for change in changes:
    frequency += int(change)

print(frequency)
