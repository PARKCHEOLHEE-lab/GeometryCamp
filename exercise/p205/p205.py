﻿import math
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh

class Box:
    def __init__(self, x, y, z):
        self.plane = rg.Plane.WorldXY
        self.x = x
        self.y = y
        self.z = z
        self.size = self.get_size()
        self.box = self.box_gen()
        
    def get_size(self):
        size_dict = {'x':self.x, 'y':self.y, 'z':self.z}
        return size_dict
        
    def box_gen(self):
        box = gh.CenterBox(self.plane, self.size['x'], self.size['y'], self.size['z'])
        return box
        
    def box_array(self):
        boxes = gh.BoxArray(self.box, self.box, self.size['x'], self.size['y'], self.size['z'])[0]
        return boxes
        
    def box_union(self, boxes):
        return gh.SolidUnion(boxes)


class Sphere:
    def __init__(self, radius):
        self.radius = radius
        
    def sphere_gen(self, base):
        sphere = gh.Sphere(base, self.radius)
        return sphere


if __name__ == "__main__":
    box = Box(x,y,z)
    boxes = box.box_array()
    boxes_union = box.box_union(boxes)
    
    RAD = 43
    COUNT = 6
    SEED = 35
    sphere_base = gh.PopulateGeometry(boxes_union, COUNT, SEED)
    sphere = Sphere(RAD).sphere_gen(sphere_base)
