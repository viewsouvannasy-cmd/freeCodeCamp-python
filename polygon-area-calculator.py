import math


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width: int) -> None:
        self.width = width

    def set_height(self, height: int) -> None:
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> int:
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self) -> str:
        result = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        for i in range(self.height):
            result += "*" * self.width + "\n"

        return result

    def get_amount_inside(self, shape) -> int:
        return math.floor((self.height / shape.height) * (self.width / shape.width))


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return f"Square(side={self.side})"

    def set_side(self, side: int) -> None:
        self.side = side

    def set_width(self, side):
        self.width = side
        self.height = side
        self.side = side

    def set_height(self, side):
        self.width = side
        self.height = side
        self.side = side

    def get_picture(self):
        result = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        for i in range(self.side):

            result += "*" * self.side + "\n"

        return result
