class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "(" + str(self.x) + ', ' + str(self.y) + ")"

    def __mul__(self, scala):


vector1 = Vector2D(2, 4)
vector2 = Vector2D(3, 4)

print("Vector 1 is ", vector1)

print("Addition of ", vector1, "to  ", vector2, "is ", vector1 + vector2)

