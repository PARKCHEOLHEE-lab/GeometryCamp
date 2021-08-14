import rhinoscriptsyntax as rs

p1 = rs.PointCoordinates(rs.AddPoint(0,0,0))
p2 = rs.PointCoordinates(rs.AddPoint(2,4,0))
p3 = rs.PointCoordinates(rs.AddPoint(5,2,0))

v1 = p2 - p1
v2 = p3 - p2
v3 = p1 - p3