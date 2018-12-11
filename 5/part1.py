import sys
import os
from collections import deque

inputfile=os.path.join(sys.path[0],sys.argv[1])

with open(inputfile) as f:
  chain = f.readline().strip()

stack = deque()

for char in chain:
  if len(stack) == 0:
    stack.append(char)
    continue
  if char.swapcase() == stack[-1]:
    stack.pop()
  else:
    stack.append(char)

print(len(stack))
