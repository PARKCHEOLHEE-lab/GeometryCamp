import Rhino.Geometry as rg
import rhinoscriptsyntax as rs

quarter = 0.25
for j in range(count):
    pts = []
    for i in range(len(points)-1):
        x1, y1, z1 = ((points[i+1] - points[i]) * quarter) + points[i]
        pt_1 = rg.Point3d(x1, y1, z1)
        pts.append(pt_1)
        
        x2, y2, z2 = ((points[i+1] - points[i]) * (1 - quarter)) + points[i]
        pt_2 = rg.Point3d(x2, y2, z2)
        pts.append(pt_2)
    points = pts

subdiv_points = pts
subdiv_curve = rs.AddPolyline(points)
