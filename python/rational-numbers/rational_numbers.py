from __future__ import division
from functools import reduce

def prime_factors(number):
    if number == 0:
        return [0]
    factors, n = [1], 2 # return 1 as well
    absnumber = abs(number) # ignoring negative numbers
    while absnumber > 1:
        while absnumber % n == 0:
            factors.append(n)
            absnumber /= n
        n += 1
    return factors

class Rational(object):
    def __init__(self, numer, denom):
        numer_factored = prime_factors(numer)
        denom_factored = prime_factors(denom)
        for i in numer_factored[:]:
            if i in denom_factored and not i == 1:
                numer_factored.remove(i)
                denom_factored.remove(i)
        self.numer = reduce(lambda x, y: x*y, numer_factored)
        if numer * denom < 0:
            self.numer *= -1
        self.denom = reduce(lambda x, y: x*y, denom_factored)
        if numer == 0:
            self.denom = 1

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        power_abs = abs(power)
        if power <0:
            return Rational(self.denom ** power_abs, self.numer ** power_abs)
        else:
            return Rational(self.numer ** power_abs, self.denom ** power_abs)

    def __rpow__(self, base):
        return (base**self.numer)**(1/self.denom)
