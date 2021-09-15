import rhinoscriptsyntax as rs

# 선분1 ; (x11,y11) to (x12, y12)
# 선분2 ; (x21,y21) to (x22, y22)
x11 = p1[0]; y11 = p1[1]
x12 = p2[0]; y12 = p2[1]
x21 = p3[0]; y21 = p3[1]
x22 = p4[0]; y22 = p4[1]

# 선분1의 기울기 => m1; 선분2의 기울기 => m2
m1 = (y11-y12) / (x11-x12)
m2 = (y21-y22) / (x21-x22)

cx = (x11*m1 - x21*m2 - y11+y21) / (m1 - m2)
cy = m1*(cx-x11) + y11

# 선분1과 선분2의 교차 여부 판단
f1 = y21- (m1*x21 - m1*x11 + y11 )
f2 = y22 - (m1*x22 - m1*x11 + y11 )

if f1*f2 < 0:
    a = rs.AddPoint(cx, cy, 0)
