import sys
import os
import string
from collections import deque

inputfile=os.path.join(sys.path[0],sys.argv[1])

with open(inputfile) as f:
  chain = f.readline().strip()

def remaining_count(lower,upper):
  stack = deque()
  for char in chain:
    if char == lower or char == upper:
      continue
    if len(stack) == 0:
      stack.append(char)
      continue
    if char.swapcase() == stack[-1]:
      stack.pop()
    else:
      stack.append(char)
  return len(stack)

remaining_counts = []

for lower,upper in zip(string.ascii_lowercase, string.ascii_uppercase):
  remaining_counts.append(remaining_count(lower,upper))

print(min(remaining_counts))
