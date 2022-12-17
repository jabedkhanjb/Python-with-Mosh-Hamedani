class Point:
    def move(self):
        print("Let's move")

    def back(self):
        print("Go back")

point1 = Point()
point1.plus = "This is string and int number", 10
print(point1.plus)
point1.move()

point2 = Point()
point2.subtract = "This is String"
print(point2.subtract)
point2.back()
