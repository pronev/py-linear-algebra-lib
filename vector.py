import math
from decimal import *
getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Zero vector cannot be normalized'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(tuple([x.to_eng_string() for x in self.coordinates]))


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def __add__(self, v):
        return Vector([x+y for x,y in zip(self.coordinates, v.coordinates)])


    def __sub__(self, v):
        return Vector([x-y for x,y in zip(self.coordinates, v.coordinates)])


    def mul_scalar(self, c):
        return Vector([Decimal(c)*x for x in self.coordinates])


    def mag(self):
        return sum([x**Decimal('2') for x in self.coordinates]).sqrt()


    def norm(self):
        try:
            return self.mul_scalar(Decimal('1')/self.mag())

        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)


    def __mul__(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])


    # Different precision
    # def __mul__(self, v):
    #     x = self.mag() * v.mag()
    #     return x * Decimal(str(math.cos(self.ang(v))))


    def ang(self, v, in_degrees = False):
        try:
            # Different precision
            # radian = math.acos(self * v / (self.mag() * v.mag()))
            radian = math.acos(self.norm() * v.norm())

            if in_degrees:
                return str(radian * 180 / math.pi)
            else:
                return str(radian)

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with zero vector')
            else:
                raise e