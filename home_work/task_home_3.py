import random


class RectangleSideError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Сторона A == {self.a}, сторона B == {self.b}. Стороны не могут быть отрицательными."


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width
        if width is None:
            self.width = length
        if self.length < 0 or self.width < 0:
            raise RectangleSideError(self.length, self.width)

    def rectangle_perimeter(self):
        return 2 * self.length + 2 * self.width

    def area_of_a_rectangle(self):
        return self.width * self.length

    def __add__(self, other):
        p = (self.rectangle_perimeter() + other.rectangle_perimeter()) / 2
        side_one = random.randint(1, p)
        site_two = p - side_one
        return Rectangle(int(side_one), int(site_two))

    def __sub__(self, other):
        if self.rectangle_perimeter() - other.rectangle_perimeter() > 0:
            p = (self.rectangle_perimeter() - other.rectangle_perimeter()) / 2
        elif self.rectangle_perimeter() - other.rectangle_perimeter():
            return None
        else:
            p = (other.rectangle_perimeter() - self.rectangle_perimeter()) / 2
        side_one = random.randint(1, p)
        site_two = p - side_one
        return Rectangle(int(side_one), int(site_two))

    def __eq__(self, o) -> bool:
        return self.rectangle_perimeter() == o.rectangle_perimeter()

    def __ne__(self, o) -> bool:
        return self.rectangle_perimeter() != o.rectangle_perimeter()

    def __gt__(self, o) -> bool:
        return self.rectangle_perimeter() > o.rectangle_perimeter()

    def __ge__(self, o) -> bool:
        return self.rectangle_perimeter() <= o.rectangle_perimeter()

    def __lt__(self, o) -> bool:
        return self.rectangle_perimeter() < o.rectangle_perimeter()

    def __le__(self, o) -> bool:
        return self.rectangle_perimeter() >= o.rectangle_perimeter()


if __name__ == '__main__':
    p_1 = Rectangle(-1, 4)
    p_2 = Rectangle(4, 2)

    print(p_1 < p_2)
