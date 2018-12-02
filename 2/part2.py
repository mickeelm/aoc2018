import sys
import os

inputfile=os.path.join(sys.path[0],sys.argv[1])
with open(inputfile) as f:
 codes = f.readlines()

def compare(code1, code2):
  common = ''
  for a,b in zip(code1, code2):
    if a is b:
      common += a
  if len(code1) - len(common) is 1:
    print(common)
    return True
  return False

def check_code(code1):
  for code2 in codes:
    if compare(code1, code2):
      return True

while codes:
  if check_code(codes[0]):
    break
  del codes[0]
