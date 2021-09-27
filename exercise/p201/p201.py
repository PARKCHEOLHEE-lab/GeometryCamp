import math
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh

class Triangrid:
    def __init__(self, plane, size, x_count, y_count):
        self.plane = plane
        self.size = size
        self.x_count = x_count
        self.y_count = y_count
        self.curves = self.grid_gen()
        
#    def get_guid(self, curve):
#        guid = rs.MoveObject(curve, [0,0,0])
#        return guid
        
    def grid_gen(self):
        grid = gh.Triangular(self.plane, self.size, self.x_count, self.y_count)[0]
        return grid
        
    def grid_merge(self):
        union = gh.RegionUnion(self.curves)
        return union
        
    def grid_centroid(self, curve):
        centroid = rs.CurveAreaCentroid(curve)[0]
        return centroid
        
    def grid_scaled(self, curve, origin, factor):
        scaled = gh.Scale(curve, origin, factor)[0]
        return scaled
        
    def grid_segment(self, curve, scaled):
        segmented = rs.AddLoftSrf([curve, scaled])
        return segmented
        
    def grid_deconstruct(self, curve):
        curve_list = gh.DeconstructBrep(curve)[1]
        return curve_list  
        
    def surface_gen(self, curve):
        surface = gh.BoundarySurfaces(curve)
        return surface
        
    def surface_reparam(self):
        base_srf = self.surface_gen(self.grid_merge())
        base_srf = rs.coercesurface(base_srf)
        domain = rg.Interval(0.00, 1.00)
        base_srf.SetDomain(0, domain)
        base_srf.SetDomain(1, domain)
        return base_srf
        
    def surface_eval(self, u, v):
        point = rs.EvaluateSurface(self.surface_reparam(), u, v)
        return point

if __name__ == '__main__':
    SCALE = 0.0001
    PLANE = rg.Plane.WorldXY
    triangles = Triangrid(PLANE, 3, 13, 8)
    point = triangles.surface_eval(slider[0], slider[1])
    
    grid_scaled = []
    grid_segmented = []
    for t_curve in triangles.curves:
        centroid = triangles.grid_centroid(t_curve)
        scaled = triangles.grid_scaled(t_curve, centroid, SCALE)
        
        triangle_line_list = triangles.grid_deconstruct(t_curve)
        scaled_line_list = triangles.grid_deconstruct(scaled)
        for i in range(len(scaled_line_list)):
            segmented = triangles.grid_segment(triangle_line_list[i], scaled_line_list[i])[0]
            grid_segmented.append(segmented)
