
class Point:
    from math import sqrt, pow
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def origin_distance(self):
        return self.sqrt(self.x * self.x + self.y * self.y)

    def distance(self, other):
        return self.sqrt(self.pow(self.x - other.x, 2) + self.pow(self.y - other.y, 2))


pset1 = Point(1, - 2)

pset2 = Point(2, 4)

print(pset1.origin_distance())

distance2 = pset2.origin_distance()
print(pset2.origin_distance())

print(pset1.distance(pset2))

