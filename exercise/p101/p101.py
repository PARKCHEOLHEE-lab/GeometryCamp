import sys
import math
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh

# 2.7.8 (IronPython 2.7.8 (2.7.8.0) on .NET 4.0.30319.42000 (64-bit))

class Point:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def position(self):
        pos = {'x':self.x, 'y':self.y, 'z':self.z}
        return pos

    def point_gen(self):
         coord = self.position()
         point = rs.AddPoint(coord['x'], coord['y'], coord['z'])
         return point


class Matrix:
    def __init__(self, count, interval):
        self.interval = interval
        self.count = count
        self.points = []

    def matrix_gen(self):
        for i in range(self.count):
            for j in range(self.count):
                itvl = self.interval
                x = i*itvl
                y = j*itvl
                z = math.sin(x)*itvl/4 + math.sin(y)*itvl/4
                point = Point(x, y, z).point_gen()
                self.points.append(point)
        return self.points


class Surface(Matrix):
    def __init__(self, count, interval, u_count, interpolate=False):
        Matrix.__init__(self, count, interval)
        self.u_count = u_count
        self.interpolate = interpolate

    def points_coerce(self):
        return rs.coerce3dpointlist(self.matrix_gen())

    def surface_gen(self):
        points = self.points_coerce()
        surface = gh.SurfaceFromPoints(points, self.u_count, self.interpolate)
        return surface


class Box(Surface):
    def __init__(self, count, interval, size):
        Matrix.__init__(self, count, interval)
        self.size = size

    def box_gen(self):
        base = self.points_coerce()
        size = self.size / 2
        return gh.CenterBox(base, size, size, size)

if __name__ == "__main__":
    grid_count = 15
    grid_interval = 32
    box = Box(grid_count, grid_interval, grid_interval)
    box = box.box_gen()