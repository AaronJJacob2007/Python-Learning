class Point:
    #self is reference to the current object
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def move(self):
        print("Move")

    def draw(self):
        print("draw")

point=Point(10,20)
point.x=11
print(point.x)
