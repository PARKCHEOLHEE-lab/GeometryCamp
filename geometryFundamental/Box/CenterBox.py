import Rhino.Geometry as rg

class CenterBox:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def domain(self):
        I = rg.Interval
        dom_x = I(int(-self.x/2), int(self.x/2))
        dom_y = I(int(-self.y/2), int(self.y/2))
        dom_z = I(int(-self.z/2), int(self.z/2))
        
        return dom_x, dom_y, dom_z
        
    def generate(self):
        plane = rg.Plane.WorldXY
        box = rg.Box(plane, self.domain()[0], self.domain()[1], self.domain()[2])
        return box

b = CenterBox(50,50,50)
b = b.generate()
