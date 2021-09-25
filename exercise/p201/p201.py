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

    def surface_reparam(self):
        base_srf = self.surface_gen(self.grid_merge())
        base_srf = rs.coercesurface(base_srf)
        domain = rg.Interval(0.00, 1.00)
        base_srf.SetDomain(0, domain)
        base_srf.SetDomain(1, domain)
        return base_srf

    def grid_gen(self):
        grid = gh.Triangular(self.plane, self.size, self.x_count, self.y_count)[0]
        return grid

    def grid_merge(self):
        union = gh.RegionUnion(self.curves)
        return union

    def grid_centroid(self, curve):
        centroid = rs.CurveAreaCentroid(curve)
        return centroid

    def surface_gen(self, curve):
        surface = gh.BoundarySurfaces(curve)
        return surface

    def surface_eval(self, u, v):
        point = rs.EvaluateSurface(self.surface_reparam(), u, v)
        return point


if __name__ == '__main__':
    plane = rg.Plane.WorldXY
    triangles = Triangrid(plane, 3, 13, 8)
    point = triangles.surface_eval(slider[0], slider[1])
    grid_srfs = []
    grid_pts = []
    for i in triangles.curves:
        tri = triangles.surface_gen(i)
        cen = triangles.grid_centroid(i)[0]
        grid_srfs.append(tri)
        grid_pts.append(cen)