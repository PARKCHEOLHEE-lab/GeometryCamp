import Rhino.Geometry as rg
import rhinoscriptsyntax as rs

class BoundingBox:
    def __init__(self, polygon):
        vertices = rs.CurvePoints(polygon)
        self.vertices = vertices
        
    def base(self):
        x_list = []
        y_list = []
        for point in self.vertices:
            x_pt = point[0]
            y_pt = point[1]
            x_list.append(x_pt)
            y_list.append(y_pt)
        
        x_list = [min(x_list), max(x_list)]
        y_list = [min(y_list), max(y_list)]
        
        self.base_pt_1 = rs.AddPoint(min(x_list), min(y_list))
        self.base_pt_2 = rs.AddPoint(max(x_list), max(y_list))
        self.base_pt_1 = rs.PointCoordinates(self.base_pt_1)
        self.base_pt_2 = rs.PointCoordinates(self.base_pt_2)
        
        return self.base_pt_1, self.base_pt_2
        
    def box(self):
        plane = rg.Plane.WorldXY
        bounding_box = rg.Rectangle3d(plane, self.base()[0], self.base()[1])
        
        return bounding_box


POLYGON = BoundingBox(polygon)
bounding_box = POLYGON.box()