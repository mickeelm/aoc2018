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

def most_frequent_guard(periods):
  guard_minute_counts = defaultdict(lambda:0)

  for period in periods:
    guard_id,slept,woke = period
    for minute in range(slept,woke):
      key = str(guard_id) + '_' + str(minute)
      guard_minute_counts[key] += 1

  largest_guard_minute = max(guard_minute_counts, key=guard_minute_counts.get)
  guard_id, minute = largest_guard_minute.split('_')
  return int(guard_id) * int(minute)

with open(inputfile) as f:
  log = sorted(f.readlines(), key=datetime_sorter)

periods = as_sleep_periods(log)
print(most_frequent_guard(periods))
