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
        
    def get_guid(self, curve):
        guid = rs.MoveObject(curve, [0,0,0])
        return guid
        
    def get_midpoint(self, curve):
        midpoint = rs.CurveMidPoint(curve)
        return midpoint
        
    def get_axis(self, curve):
        axis_line = rs.CurvePoints(curve)
        axis_line = axis_line[0] - axis_line[1]
        return axis_line
        
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
        
    def surface_centroid(self, surface):
        centroid = rs.SurfaceAreaCentroid(surface)[0]
        return centroid

if __name__ == '__main__':
    SCALE = 0.0001
    PLANE = rg.Plane.WorldXY
    TARGET_VALUE = 70
    triangles = Triangrid(PLANE, 3, 13, 8)
    datumn_point = triangles.surface_eval(slider[0], slider[1])
    
    grid_segmented = []
    distance_list = []
    axis_line = []
    for triangle in triangles.curves:
        triangle_centroid = triangles.grid_centroid(triangle)
        scaled = triangles.grid_scaled(triangle, triangle_centroid, SCALE)
        
        triangle_line_list = triangles.grid_deconstruct(triangle)
        scaled_line_list = triangles.grid_deconstruct(scaled)
        axis_line.extend([triangle_line_list[0],triangle_line_list[1],triangle_line_list[2]])
        
        for i in range(len(scaled_line_list)):
            segmented = triangles.grid_segment(triangle_line_list[i], scaled_line_list[i])[0]
            segmented_centroid = triangles.surface_centroid(segmented)
            distance = rs.Distance(rs.MoveObject(datumn_point, [0,0,0]), segmented_centroid)
            
            grid_segmented.append(segmented)
            distance_list.append(distance)
            
    source = rg.Interval(min(distance_list), max(distance_list))
    target = rg.Interval(TARGET_VALUE, 0)
    angle_list = gh.RemapNumbers(distance_list, source, target)[0]
    
    test = grid_segmented[5]
    sample_seg = triangles.grid_deconstruct(rs.coercebrep(test))
    sample_axs = triangles.get_axis(sample_seg[3])
    sample_mid = triangles.get_midpoint(triangles.get_guid(sample_seg[3]))
    a = rs.RotateObject(test, sample_mid, angle_list[1], sample_axs)