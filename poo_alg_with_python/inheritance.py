from cmath import rect


class Rectangle:

    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):

        return f'The area is {self.b * self.h} m2'


class Square(Rectangle):
    
    def __init__(self, l):
        super().__init__(l, l)


def run():

    rect_1 = Rectangle(10, 4)
    print(rect_1.area())

    sqr_1 = Square(5)
    print(sqr_1.area())


if __name__ == '__main__':
    
    run()