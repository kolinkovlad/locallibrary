from oop2 import Point


class Circle(Point):
    def __init__(self, x=0, y=0, R=0):
        super(Circle, self).__init__(x, y)
        self.R = R

    def in_circle(self, x, y):
        return self.distance(Point(x, y)) < self.R

    def foo(self):
        print(self.x, self.y, self.R)


def main():
    circle = Circle(R=10)
    print(circle.in_circle(2.25, 7.25))


if __name__ == "__main__":
    main()
