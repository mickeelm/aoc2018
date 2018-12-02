import sys
import os

inputfile=os.path.join(sys.path[0],sys.argv[1])

frequency = 0
frequencies = {0}
changes = []

with open(inputfile) as changes_file:
  for change in changes_file:
    changes.append(int(change))

while True:
  for change in changes:
    frequency += change
    if frequency in frequencies:
      print(frequency)
      sys.exit(0)
    frequencies.add(frequency)
