def in_range(number, range):
    return number > range[0] and number <= range[1]

def score(x, y):
    if x == 0 and y == 0:
        return 10
    c = (x**2 + y**2)**0.5
    points_range_map = {10: [0.0, 1.0], 5: [1.0, 5.0], 1: [5.0, 10.0], 0: [10.0, 100.0]}
    for points, dart_range in points_range_map.items():
        if in_range(c, dart_range):
            return points
