import math
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh

class Box:
    def __init__(self, x, y, z):
        self.plane = rg.Plane.WorldXY
        self.x = x
        self.y = y
        self.z = z
        self.box = self.box_gen()
        
    def get_size(self):
        size_dict = {'x':self.x, 'y':self.y, 'z':self.z}
        return size_dict
        
    def box_gen(self):
        size_x = self.get_size()['x']
        size_y = self.get_size()['y']
        size_z = self.get_size()['z']
        box = gh.CenterBox(self.plane, size_x, size_y, size_z)
        return box
        
    def box_array(self):
        size_x = self.get_size()['x']
        size_y = self.get_size()['y']
        size_z = self.get_size()['z']
        array = gh.BoxArray(self.box, self.box, size_x, size_y, size_z)[0]
        return array


if __name__ == "__main__":
    box = Box(x,y,z)
    box = box.box_array()
