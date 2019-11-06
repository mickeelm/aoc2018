def init_grid(serial, size=300):
    return [[power_level(x, y, serial) for y in range(1, size + 1)] for x in range(1, size + 1)]


def grid_power(x, y, sat, side_length):
    x -= 1
    y -= 1
    offset = side_length - 1
    upper_left_outside = 0 if x == 0 else sat[x - 1][y - 1]
    lower_left_outside = 0 if x == 0 else sat[x - 1][y + offset]
    upper_right_outside = 0 if y == 0 else sat[x + offset][y - 1]
    lower_right = sat[x + offset][y + offset]
    return lower_right - upper_right_outside - lower_left_outside + upper_left_outside


def summed_area_table(table):
    height = len(table)
    width = len(table[0])
    sat = [[None for x in range(width)] for y in range(height)]
    for row in range(height):
        row_sum = 0
        for col in range(width):
            row_sum += table[row][col]
            sat[row][col] = row_sum
            if row > 0:
                sat[row][col] += sat[row - 1][col]
    return sat


def power_level(x, y, serial):
    rack_id = x + 10
    pwr_level = rack_id * y
    pwr_level += serial
    pwr_level *= rack_id
    pwr_level = (pwr_level // 100) % 10
    pwr_level -= 5
    return pwr_level


def highest_power_grid_coordinates(serial):
    table = init_grid(serial)
    sat = summed_area_table(table)
    greatest_power = -10
    greatest_power_info = ()
    for side_length in range(1, 301):
        x, y, power = highest_power_grid_coordinates_fixed_side(sat, side_length)
        if power > greatest_power:
            greatest_power = power
            greatest_power_info = (x, y, side_length, power)
    return greatest_power_info


def highest_power_grid_coordinates_fixed_side(sat, side_length):
    greatest_power = None
    coordinates = ()
    for y in range(1, 302 - side_length):
        for x in range(1, 302 - side_length):
            total_pwr = grid_power(x, y, sat, side_length)
            if not greatest_power or total_pwr > greatest_power:
                greatest_power = total_pwr
                coordinates = (x, y, total_pwr)
    return coordinates


def test_summed_area_table():
    table = [[31, 2, 4, 33, 5, 36], [12, 26, 9, 10, 29, 25], [13, 17, 21, 22, 20, 18], [24, 23, 15, 16, 14, 19],
             [30, 8, 28, 27, 11, 7], [1, 35, 34, 3, 32, 6]]
    assert summed_area_table(table) == sat_for_test()


def test_init_grid():
    expected_grid = [[power_level(1, 1, 72), power_level(2, 1, 72), power_level(3, 1, 72)],
                     [power_level(1, 2, 72), power_level(2, 2, 72), power_level(3, 2, 72)],
                     [power_level(1, 3, 72), power_level(2, 3, 72), power_level(3, 3, 72)]]

    assert init_grid(72, 3) == expected_grid


def test_power_level():
    assert power_level(3, 5, 8) == 4
    assert power_level(122, 79, 57) == -5
    assert power_level(217, 196, 39) == 0
    assert power_level(101, 153, 71) == 4


def test_total_power():
    assert grid_power(2, 2, sat_for_test(), 3) == 159
    assert grid_power(33, 45, summed_area_table(init_grid(18)), 3) == 29
    assert grid_power(21, 61, summed_area_table(init_grid(42)), 3) == 30


def test_highest_power_grid_coordinates_fixed_side():
    # Assignment 1 examples
    assert highest_power_grid_coordinates_fixed_side(summed_area_table(init_grid(18)), 3) == (33, 45, 29)
    assert highest_power_grid_coordinates_fixed_side(summed_area_table(init_grid(42)), 3) == (21, 61, 30)
    # Answer to assignment 1
    assert highest_power_grid_coordinates_fixed_side(summed_area_table(init_grid(5153)), 3) == (235, 18, 31)


def test_highest_power_grid_coordinates():
    # Assignment 2 examples
    #    assert highest_power_grid_coordinates(18) == (90, 269, 16, 113)
    #    assert highest_power_grid_coordinates(42) == (232, 251, 12, 119)
    # Assignment 2 answer
    assert highest_power_grid_coordinates(5153) == (236, 227, 12, 110)


def sat_for_test():
    return [[31, 33, 37, 70, 75, 111], [43, 71, 84, 127, 161, 222], [56, 101, 135, 200, 254, 333],
            [80, 148, 197, 278, 346, 444], [110, 186, 263, 371, 450, 555], [111, 222, 333, 444, 555, 666]]
