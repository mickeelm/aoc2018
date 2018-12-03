import sys
import os

inputfile=os.path.join(sys.path[0],sys.argv[1])
claimed = set()
conflicting = set()
entries = {}

def non_conflicting_claim():
  mark_claimed_and_conflicts()
  for claim_id, grid in entries.items():
    if grid.isdisjoint(conflicting):
      return claim_id

def mark_claimed_and_conflicts():
  for grid in entries.values():
    for coordinate in grid:
      if coordinate in claimed:
        conflicting.add(coordinate)
      else:
        claimed.add(coordinate)

def coordinates(entry):
  coordinates = set()
  cols, rows = cols_rows(entry)
  for col in cols:
    for row in rows:
      coordinates.add((col,row))
  return coordinates

def claim_id(entry):
  return int(entry.split()[0][1:])

def cols_rows(entry):
  id_, at, start, size = entry.split()
  col, row = map(int, start[:-1].split(','))
  width, height = map(int, size.split('x'))

  return range(col, col+width), range(row, row+height)

with open(inputfile) as f:
  lines = f.readlines()
  for line in lines:
    entries[claim_id(line)] = coordinates(line)

print(non_conflicting_claim())
