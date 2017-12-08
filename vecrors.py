class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return 2

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        return "(" + str(self.x) + ', ' + str(self.y) + ")"

    def __mul__(self, scala):
        return Vector2D(self.x * scala, self.y * scala)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __getitem__(self, item):
        if item == 'x':
            return self.x
        if item == 'y':
            return self.y

    def __setitem__(self, key, value):
        if key == 'x':
            self.x = value
        if key == 'y':
            self.y = value

    def __call__(self, *args, **kwargs):
        print('Arguments: ')
        for item in args:
            print(item)
        print("Keywords: ")
        for item in kwargs.keys():
            print(item, " : ", kwargs[item])


vector1 = Vector2D(2, 4)
vector2 = Vector2D(3, 4)

print("Vector 1 is ", vector1)

print("Addition of ", vector1, "to  ", vector2, "is ", vector1 + vector2)
print("Multiplication of ", vector1, "with 3  is ", vector1 * 3)
print(Vector2D(6, 8) == vector2 * 2)

print("Vector2 is ", vector2)
print("X coord of Vector2 is ", vector2['x'])
print("Y coord of Vector2 is ", vector2['y'])

print(len(vector2))

vector2(2, 4, 'Some string', g=3, rez = "asd")