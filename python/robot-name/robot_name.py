import random
from string import ascii_uppercase, digits

class Robot:

    names = []
    
    def __init__(self):
        self.reset()

    def gen_rand_name(self):
        return ''.join(random.sample(ascii_uppercase,2)) + ''.join(random.sample(digits, 3))

    def reset(self):
        new = False
        while not new:
            name = self.gen_rand_name()
            if name not in self.names:
                self.name = name
                Robot.names.append(name)
                new = True

