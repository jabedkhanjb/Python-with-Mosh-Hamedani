class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.z = 1
print(point2.z)