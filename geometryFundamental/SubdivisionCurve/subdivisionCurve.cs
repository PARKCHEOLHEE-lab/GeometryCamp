  private void RunScript(List<Point3d> points, int count, double quarter, ref object subdividePoints, ref object curve)
  {
    for (int j = 0; j < count; j++)
    {
      List<Point3d> pts = new List<Point3d>();

      for (int i = 0; i < points.Count - 1; i++)
      {
        Point3d quarterPoint1 = (1 - quarter) * points[i] + quarter * points[i + 1];
        pts.Add(quarterPoint1);

        Point3d quarterPoint2 = quarter * points[i] + (1 - quarter) * points[i + 1];
        pts.Add(quarterPoint2);
      }
      points = pts;
    }

    subdividePoints = points;
    curve = new PolylineCurve(points);
