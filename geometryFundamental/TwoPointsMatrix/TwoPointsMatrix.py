import sys
import rhinoscriptsyntax as rs

# print(sys.version) 
# 2.7.8 (IronPython 2.7.8 (2.7.8.0) on .NET 4.0.30319.42000 (64-bit)) 

class Point:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        
    def coordinate(self):
        coord_dict = {'x':self._x, 'y':self._y, 'z':self._z}
        
        return coord_dict 
        
    def generate(self):
        x = self.coordinate()['x']
        y = self.coordinate()['y']
        z = self.coordinate()['z']
        pt = rs.AddPoint(x, y, z)
        
        return pt


class Matrix(Point):
    def __init__(self, p1, p2, cnt):
        self._p1 = p1
        self._p2 = p2
        self._cnt = cnt
        self._pts = []
        
    def points(self):
        p1_coord = self._p1.coordinate()
        p2_coord = self._p2.coordinate()
        points_dict = {'p1':p1_coord, 'p2':p2_coord}
        
        return points_dict
        
    def distance(self):
        p1_x = self.points()['p1']['x']; p1_y = self.points()['p1']['y']; p1_z = self.points()['p1']['z']
        p2_x = self.points()['p2']['x']; p2_y = self.points()['p2']['y']; p2_z = self.points()['p2']['z']
        x_distance = abs(p1_x - p2_x)
        y_distance = abs(p1_y - p2_y)
        z_distance = abs(p1_z - p2_z)
        distance_dict = {'x':x_distance, 'y':y_distance, 'z':z_distance}
        
        return distance_dict
        
    def interval(self):
        x_interval = self.distance()['x'] / self._cnt
        y_interval = self.distance()['y'] / self._cnt
        z_interval = self.distance()['z'] / self._cnt
        interval_dict = {'x':x_interval, 'y':y_interval, 'z':z_interval}
        
        return interval_dict
        
    def grid(self):
        def grid_gen(pos_1, pos_2, pos_3):
            for i in range(self._cnt+1):
                for j in range(self._cnt+1):
                    for k in range(self._cnt+1):
                        x = i*self.interval()['x']+pos_1
                        y = j*self.interval()['y']+pos_2
                        z = k*self.interval()['z']+pos_3
                        pt = Point(x,y,z).generate()
                        self._pts.append(pt)
                    
        p1_x = self.points()['p1']['x']; p1_y = self.points()['p1']['y']; p1_z = self.points()['p1']['z']
        p2_x = self.points()['p2']['x']; p2_y = self.points()['p2']['y']; p2_z = self.points()['p2']['z']
        
        if p1_x < p2_x:
            if p1_y < p2_y:
                if p1_z <= p2_z:
                    grid_gen(p1_x, p1_y, p1_z)
                
                elif p1_z > p2_z:
                    grid_gen(p1_x, p1_y, p2_z)
                
            elif p1_y > p2_y:
                if p1_z <= p2_z:
                    grid_gen(p1_x, p2_y, p1_z)
                
                elif p1_z > p2_z:
                    grid_gen(p1_x, p2_y, p2_z)
                    
        if p1_x > p2_x:
            if p1_y > p2_y:
                if p1_z > p2_z:
                    grid_gen(p2_x, p2_y, p2_z)
                
                elif p1_z <= p2_z:
                    grid_gen(p2_x, p2_y, p1_z)
                    
            elif p1_y < p2_y:
                if p1_z <= p2_z:
                    grid_gen(p2_x, p1_y, p1_z)
                
                elif p1_z > p2_z:
                    grid_gen(p2_x, p1_y, p2_z)
                
        return self._pts

#pt1 = Point(point1[0],point1[1],point1[2])
#pt2 = Point(point2[0],point2[1],point2[2])

pt1 = Point(-214.272358, -47.384897, 150.54862)
pt2 = Point(126.804278, 395.601923, 0)
matrix = Matrix(pt1,pt2,count)
matrix = matrix.grid()

