import sys
import os
from collections import deque

inputfile = os.path.join(sys.path[0], sys.argv[1])

extract_value_parts = lambda line: line[10:-2].split('> velocity=<')
extract_values = lambda value_part: [int(value.strip()) for value in value_part.split(',')]
calc_offsets = lambda second: deque([(x * second, y * second) for x, y in velocities])
lesser = lambda new, current: new if new < current else current
greater = lambda new, current: new if new > current else current


def add_coordinates_and_velocity(line):
    coords, vels = extract_value_parts(line)
    coord_x, coord_y = extract_values(coords)
    vel_x, vel_y = extract_values(vels)

    start_coordinates.append((coord_x, coord_y))
    velocities.append((vel_x, vel_y))


def calc_current_coordinates(offsets):
    current_coordinates = deque()
    for coordinates in start_coordinates:
        coord_x, coord_y = coordinates
        transfer_x, transfer_y = offsets.popleft()

        current_coordinates.append((coord_x + transfer_x, coord_y + transfer_y))
    return current_coordinates


def get_edges(second):
    offsets = calc_offsets(second)
    current_coordinates = calc_current_coordinates(offsets)

    min_x, min_y = current_coordinates.pop()
    max_x, max_y = min_x, min_y

    while (True):
        try:
            x, y = current_coordinates.pop()
            min_x = lesser(x, min_x)
            min_y = lesser(y, min_y)
            max_x = greater(x, max_x)
            max_y = greater(y, max_y)
        except IndexError:
            break
    x_distance = max_x - min_x
    y_distance = max_y - min_y
    return max_x, min_x, max_y, min_y


def calc_surface_size(edges):
    max_x, min_x, max_y, min_y = edges
    x_distance = max_x - min_x
    y_distance = max_y - min_y
    return x_distance * y_distance


def print_grid(second, edges):
    offsets = calc_offsets(second)
    as_list = list(calc_current_coordinates(offsets))

    max_x, min_x, max_y, min_y = edges
    for y in range(min_y, max_y + 1):
        print()
        for x in range(min_x, max_x + 1):
            if (x, y) in as_list:
                print('#', end='')
            else:
                print('.', end='')
    print()


start_coordinates = []
velocities = []

with open(inputfile) as f:
    for line in f.readlines():
        add_coordinates_and_velocity(line)

current_second = 0
current_edges = get_edges(current_second)
current_size = calc_surface_size(current_edges)

while (True):
    previous_second = current_second
    previous_edges = current_edges
    previous_size = current_size

    current_second += 1
    current_edges = get_edges(current_second)
    current_size = calc_surface_size(current_edges)
    if current_size > previous_size:
        break

print_grid(previous_second, previous_edges)
print(previous_second)
