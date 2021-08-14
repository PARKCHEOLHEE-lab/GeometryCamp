##### ___GeometryCamp___
### ___Rhino Python Geometry Study : `<type 'Vector3d'>`___ </div>
#  
#### ___Geometry Fundamentals___<br>


>  ___📖 Study Content ▽___　_[Reference Documents](https://developer.rhino3d.com/guides/rhinopython/python-rhinoscriptsyntax-vectors/)_
>  - _Similar to 3D points, 3D vectors are stored as Vector3d structures. They can be thought as a zero-based, `one-dimensional list` that contain three numbers._
> - _To find the vector between two points, use `vector subtraction`_
> - _Vectors can also be added to points to `create new point` locations._
> - _`rs.CreateVector(1,2,3)` The method allows you to create vectors._ 
> 　<br><br>
> 
>  ___💬 View Geometry ▽___
> 
> <p align="center"><img src="https://user-images.githubusercontent.com/83874157/129447476-56c3cb58-41a4-46bf-8142-88520c3966b3.PNG" width="378px"> <img src="https://user-images.githubusercontent.com/83874157/129447577-29e3182a-6ffa-49ce-8d20-c593ce12f322.PNG" width="378px"> <img src="https://user-images.githubusercontent.com/83874157/129447580-e267bdf2-39f5-459d-8e49-33e9e5f7b4be.PNG" width="378px"> <img src="https://user-images.githubusercontent.com/83874157/129447581-ed01a351-d4c7-4109-bc9e-695fd8240424.PNG" width="378px"></p>
> 
> ___⬜ Image Annotation ▽___
> - _Top Left : `p1, p2, p3 = rs.PointCoordinates(rs.AddPoint(0,0,0)), (2,4,0), (5,2,0)`_ 
> - _Top Right : `v3 = p1 - p3`_ 
> - _Bottom Left : `v2 = p3 - p2`_ 
> - _Bottom Right : `v3 = p1 - p3`_ 
> 　
<br>

