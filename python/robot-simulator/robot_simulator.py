NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)

    def turn_right(self):
        self.bearing = (self.bearing + 1 )%4

    def turn_left(self):
        self.bearing = (self.bearing - 1 )%4

    def simulate(self, sequence):
        for action in sequence:
            if action == 'R':
                self.turn_right()
            elif action == 'L':
                self.turn_left()
            elif action == 'A':
                self.advance()
            else:
                raise ValueError('Unallowed action')

    def advance(self):
        if self.bearing == 0:
            self.y += 1
        elif self.bearing == 1:
            self.x += 1
        elif self.bearing == 2:
            self.y += -1
        elif self.bearing == 3:
            self.x += -1
        self.coordinates = (self.x, self.y)
