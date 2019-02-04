from __future__ import division
from functools import reduce
from math import gcd

class Rational(object):
    def __init__(self, numer, denom):
        self.gcd = gcd(numer, denom)
        self.numer = abs(int(numer/self.gcd))
        self.denom = abs(int(denom/self.gcd))
        if numer == 0:
            self.denom = 1
        if numer * denom < 0:
            self.numer *= -1

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
