import Rhino.Geometry as rg
import rhinoscriptsyntax as rs

class TwoPointBox:
    def __init__(self, pt1, pt2):
        self.pt1 = pt1
        self.pt2 = pt2
        
    def domain(self):
        I = rg.Interval
        dom_x = I(self.pt1[0], self.pt2[0])
        dom_y = I(self.pt1[1], self.pt2[1])
        dom_z = I(self.pt1[2], self.pt2[2])
        
        return dom_x, dom_y, dom_z
        
    def generate(self):
        plane = rg.Plane.WorldXY
        box = rg.Box(plane, self.domain()[0], self.domain()[1], self.domain()[2])
        return box

b = TwoPointBox([-23.396866,-61.045327,0], [100,-26.161112,50])
b = b.generate()
