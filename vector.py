import math
from decimal import *
getcontext().prec = 16

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(str(x)) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(tuple([float(x.to_eng_string()) for x in self.coordinates]))


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def __add__(self, v):
        return Vector([x+y for x,y in zip(self.coordinates, v.coordinates)])


    def __sub__(self, v):
        return Vector([x-y for x,y in zip(self.coordinates, v.coordinates)])


    def mul_scalar(self, c):
        return Vector([Decimal(str(c))*x for x in self.coordinates])


    def mag(self):
        return sum([x**Decimal(str(2)) for x in self.coordinates]).sqrt()


    def norm(self):
        try:
            return self.mul_scalar(Decimal(str(1))/self.mag())

        except ZeroDivisionError:
            raise Exception('Zero vector cannot be normalized')


    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])


    def ang_rad(self, v):
        x = float((self.dot(v) / (self.mag() * v.mag())).to_eng_string())
        return math.acos(x)


    def ang(self, v):
        x = float((self.dot(v) / (self.mag() * v.mag())).to_eng_string())
        return math.acos(x) * 180 / math.pi


    def __mul__(self, v):
        x = self.mag() * v.mag()
        return x * Decimal(str(math.cos(self.ang_rad(v))))