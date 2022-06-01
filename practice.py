# class Point:
#     default_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(self.x, self.y)

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def __cmp__(self, pointer):
#         return self.x != pointer.x and self.y != pointer.y


# point = Point(1, 2)
# pointer = Point(5, 6)
# print(point != pointer)
