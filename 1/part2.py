frequency = 0
frequencies = {0}
changes = []
iteration = 1
with open('input') as changes_file:
    for change in changes_file:
        changes.append(int(change))

found = False
while not found:
    for change in changes:
        frequency += change
        if frequency in frequencies:
            print('hit {} twice! Took {} iterations.'.format(frequency,iteration))
            found = True
            break
        frequencies.add(frequency)
    iteration+=1
