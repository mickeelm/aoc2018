frequency = 0
with open('input') as changes:
    for change in changes:
        frequency += int(change)
print(frequency)
