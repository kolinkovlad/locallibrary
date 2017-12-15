import math


class Rational:
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __mul__(self, other):
        return Rational(self.num * other.num,
                        self.denom * other.denom)

    def __add__(self, other):
        """ Make the lass couch"""
        return Rational(self.num * other.denom + other.num * self.denom,
                        self.denom * other.denom)

    def __str__(self):
        return "Ration: " + str(self.num) + " / " + str(self.denom)

    def mul_rational(self, other):
        return Rational(self.num * other.num,
                        self.denom * other.denom)


rat1 = Rational(1, 2)
print(rat1)

rat2 = Rational(3, 8)

print(rat1 * rat2)

print(math.log(8, 2))
print(rat2.mul_rational(rat1))
