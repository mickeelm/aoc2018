import sys
import os
from itertools import product
from operator import itemgetter
from collections import Counter

inputfile=os.path.join(sys.path[0],sys.argv[1])
input_coordinates = []
places = []

with open(inputfile) as f:
  input_coordinates = f.readlines()

def get_closest(coordinate):
  distances = []
  for place in places:
    cx,cy = coordinate
    px,py = place
    distance = abs(cx-px)+abs(cy-py)
    distances.append((place, distance))
  
  distances.sort(key=lambda x: x[1])
  closest, closest_distance = distances[0]
  second, second_distance = distances[1]

  if closest_distance == second_distance:
    return None
  return closest


for coordinate in input_coordinates:
  x,y = coordinate.split(',')
  places.append((int(x),int(y)))

max_x = max(places,key=itemgetter(0))[0]
max_y = max(places,key=itemgetter(1))[1]

grid = list(product(range(max_x+1),range(max_y+1)))

plotted_grid = {}

for coordinate in grid:
  closest = get_closest(coordinate)
  if closest is not None:
    plotted_grid[coordinate] = closest

infinites = set()
for y in range(max_x+1):
  if (0,y) in plotted_grid:
    infinites.add(plotted_grid[0,y])
for x in range(max_y+1):
  if (x,0) in plotted_grid:
    infinites.add(plotted_grid[x,0])

valid_plots = []

for plot in plotted_grid.values():
  if not plot or plot in infinites:
    continue
  valid_plots.append(plot)


coord, count = Counter(valid_plots).most_common(1)[0]
print(count)
