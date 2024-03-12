class rectangle :
    def __init__(self,width,height):
        self.width = width
        self.height = height

class square(rectangle):
    def __init__(self,width,height):
        super().__init__(width,height)

    def area(self):
        return self.width * self.height

class cube(rectangle):
    def __init__(self,width,height,length):
        super().__init__(width,height)
        self.length = length

    def volume(self):
        return self.width * self.height * self.length


square = square(2,5)
print("area is : " + str(square.area()))

cube=cube(5,6,7)
print("volume is : " + str(cube.volume()))