import sys
import os

inputfile=os.path.join(sys.path[0],sys.argv[1])

def has_multiple_chars_of_count(id_string, count):
  for char in id_string:
    if id_string.count(char) is count:
      return True
  return False

with open(inputfile) as f:
  twoCount = 0
  threeCount = 0

  for line in f:
    if has_multiple_chars_of_count(line, 2):
      twoCount +=1
    if has_multiple_chars_of_count(line, 3):
      threeCount +=1

print(twoCount*threeCount)
