import sys
import os
from itertools import product
from operator import itemgetter
from collections import Counter

inputfile=os.path.join(sys.path[0],sys.argv[1])
distance_limit = int(sys.argv[2])
input_coordinates = []
places = []

with open(inputfile) as f:
  input_coordinates = f.readlines()

def get_distances_sum(coordinate):
  distancesum = 0
  for place in places:
    cx,cy = coordinate
    px,py = place
    distance = abs(cx-px)+abs(cy-py)
    distancesum += distance

  return distancesum

for coordinate in input_coordinates:
  x,y = coordinate.split(',')
  places.append((int(x),int(y)))

max_x = max(places,key=itemgetter(0))[0]
max_y = max(places,key=itemgetter(1))[1]

grid = list(product(range(max_x+1),range(max_y+1)))

safe_spots = 0

for coordinate in grid:
  if get_distances_sum(coordinate) < distance_limit:
    safe_spots +=1

print(safe_spots)
