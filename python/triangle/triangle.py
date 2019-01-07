def is_triangle(sides):
    return all([sum(sides)-i >= i for i in sides]) and all([i > 0 for i in sides])

def is_equilateral(sides):
    if not is_triangle(sides):
        return False
        #raise ValueError('Not a triangle')
    return sides[0] == sides[1] == sides[2]


def is_isosceles(sides):
    if not is_triangle(sides):
        return False
        #raise ValueError('Not a triangle')
    return len(set(sides)) in [1,2]


def is_scalene(sides):
    if not is_triangle(sides):
        return False
        #raise ValueError('Not a triangle')
    return len(set(sides)) == 3
