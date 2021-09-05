import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh

vertices = rs.CurvePoints(boundary)
centroid = rs.CurveAreaCentroid(boundary)[0]

pt1 = rs.AddPoint(vertices[0][0],vertices[1][1], 0)
pt2 = rs.AddPoint(vertices[4][0], vertices[7][1], 0)

bounding = rg.Rectangle3d(rg.Plane.WorldXY, rs.PointCoordinates(pt1), rs.PointCoordinates(pt2))