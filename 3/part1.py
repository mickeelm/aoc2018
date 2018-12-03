import sys
import os

inputfile=os.path.join(sys.path[0],sys.argv[1])
with open(inputfile) as f:
  entries = f.readlines()

claimed = set() 
conflicting = set()

def coordinates(entry):
  coordinates = []
  cols, rows = cols_rows(entry)
  for col in cols:
    for row in rows:
      coordinates.append((col,row))
  return coordinates

def cols_rows(entry):
  id_, at, start, size = entry.split()
  col, row = map(int, start[:-1].split(','))
  width, height = map(int, size.split('x'))

  return range(col, col+width), range(row, row+height)

def register_coordinates(entry):
  grid = coordinates(entry)
  for coordinate in grid:
    if coordinate in claimed:
      conflicting.add(coordinate)
    else:
      claimed.add(coordinate)

for entry in entries:
  register_coordinates(entry)

print(len(conflicting))
