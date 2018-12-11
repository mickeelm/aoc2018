import sys
import os
from collections import deque
from itertools import cycle

inputfile=os.path.join(sys.path[0],sys.argv[1])

def extract_prerequisites(raw):
  split = raw.split()
  return (int(split[0]), int(split[-2])+1)

def next_player():
  return next(player_iterator)

def update_score(player, score):
  player_scores[player] += score

def place_marble(player, marble):
 if marble % 23 == 0:
   circle.rotate(7)
   score = marble + circle.pop()
   update_score(player, score)
   circle.rotate(-1)
   return
 circle.rotate(-1)
 circle.append(marble)

with open(inputfile) as f:
  prerequisites = extract_prerequisites(f.readline())

nbr_of_players, last_marble = prerequisites

players = [player for player in range(nbr_of_players)]
player_iterator = cycle(players)
player_scores = {player : 0 for player in players}

marble = 0
turn = 0
circle = deque([0])

while(True):
  marble +=1
  if  marble > last_marble:
    break
  player = next_player()
  place_marble(player, marble)

print(max(player_scores.values()))
