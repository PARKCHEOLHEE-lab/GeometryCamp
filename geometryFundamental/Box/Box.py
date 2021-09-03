import Rhino.Geometry as rg

class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        return "x:{}, y:{}, z:{}".format(self.x, self.y, self.z)
       
    def size(self):
        I = rg.Interval
        return I(0, self.x), I(0, self.y), I(0, self.z)
        
    def generate(self):
        plane = rg.Plane.WorldXY
        box = rg.Box(plane, self.size()[0], self.size()[1], self.size()[2])
        return box

b = Box(50,50,50)
b = b.generate()
