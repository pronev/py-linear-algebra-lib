import math
from decimal import *
getcontext().prec = 32

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
        """Scalar multiplication"""
        return Vector([Decimal(c)*x for x in self.coordinates])


    def mag(self):
        """Magnitude"""
        return sum([x**Decimal('2') for x in self.coordinates]).sqrt()


    def norm(self):
        """Normalization"""
        try:
            return self.mul_scalar(Decimal('1')/self.mag())

        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)


    def dot(self, v):
        """Dot product (scalar product)"""
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])


    def ang(self, v, in_degrees = True):
        """Angle"""
        try:
            radian = math.acos(self.norm().dot(v.norm()))

            if in_degrees:
                return radian * 180 / math.pi
            else:
                return radian

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with zero vector')
            else:
                raise e


    def is_zero(self, tolerance = 1e-10):
        return self.mag() < tolerance


    def is_orthogonal_to(self, v, tolerance = 1e-10):
        return abs(self.dot(v)) < tolerance


    def is_parallel_to(self, v):
        return ( self.is_zero() or 
                v.is_zero() or 
                self.ang(v, False) == 0 or
                self.ang(v, False) == math.pi )
