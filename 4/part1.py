from collections import defaultdict
from datetime import datetime
import sys
import os

inputfile=os.path.join(sys.path[0],sys.argv[1])

datetime_format = '[%Y-%m-%d %H:%M'
datetime_sorter = lambda entry : datetime.strptime(entry.split(']')[0], datetime_format)
guard_id = lambda entry : int(entry.split()[3][1:])
minutes_of_hour = lambda entry : int(entry.split()[1][:-1].split(':')[1])

def as_sleep_periods(log):
  periods = []
  for entry in log:
    if 'begins' in entry:
      current_id = guard_id(entry)
    elif 'falls' in entry:
      asleep = minutes_of_hour(entry)
    elif 'wakes' in entry:
      woke = minutes_of_hour(entry) 
      periods.append((current_id,asleep,woke))
  return periods

def most_asleep(periods):
  total_sleep = defaultdict(lambda:0)

  for period in periods:
    guard,slept,woke = period
    for minute in range(slept,woke):
      total_sleep[guard] += 1

  return int(max(total_sleep, key=total_sleep.get))

def most_common_minute(periods):
  most_common = defaultdict(lambda:0)

  for period in periods:
    guard,slept,woke = period
    if guard == most_asleep_id:
      for minute in range(slept,woke):
        most_common[minute] += 1

  return int(max(most_common, key=most_common.get))

with open(inputfile) as f:
  log = sorted(f.readlines(), key=datetime_sorter)

periods = as_sleep_periods(log)
most_asleep_id = most_asleep(periods)
most_common_minute = most_common_minute(periods)

print(most_asleep_id * most_common_minute)
