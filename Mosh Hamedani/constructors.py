# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("Move")
#
#     def draw(self):
#         print("Draw")
#
#
# point = Point(10, 20)
# point.x = 333
# print(point.x)
class Point:
    def __init__(self, x , y):
        self.firstitem = x
        self.lastitem = y


numbers = Point(14, 22)
numbers.firstitem = 28
print(numbers.firstitem)