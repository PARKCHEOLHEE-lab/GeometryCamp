##### ___GeometryCamp___
##### _[Reference Documents](https://github.com/tylerjereddy/pycon-2016)_
### ___Computational Geometry in Python___ 
#  
### ___1 ) Geometry___
#### ___1. 1 ) Polygons___<br>


>  ___🔶 Definition ▽___　
>  - _a polygon is the closed region of the plane bounded by a finite collection of line segments forming a closed curve that does `not intersect itself`_
>  - _In geometry, a polygon is a plane figure that is described by a finite number of straight line segments connected to form a closed `polygonal chain (or polygonal circuit)`_
> 　<br><br>
> 
>  ___💡 Polygon & Not Polygon ▽___
> 
> <p align="center"><img src="https://user-images.githubusercontent.com/83874157/129742828-076e8757-4100-4afc-895b-f987c13c53b0.png" width="750px"></p>
> 　<br>
> 
> ___✔️ Polygon Annotation ▽___
> - _Top Left Vertex : `[0,2]`_ 
> - _Top Right Vertex : `[2,2]`_ 
> - _Bot Left Vertex : `[2,0]`_ 
> - _Bot Right Vertex : `[0,0]`_ 
> - _Vertices Scatter : `*.scatter(polygon_vertices[..., 0], polygon_vertices[..., 1]`_ 
> - _Polygon : `Polygon(polygon_vertices)`_ 
>  <br>
>  
> ___❌ Not Polygon Annotation ▽___
> - _Top Left Vertex : `[0,2]`_ 
> - _Top Right Vertex : `[2,2]`_ 
> - _Bot Left Vertex : `[0,0]`_ 
> - _Bot Right Vertex : `[2,0]`_ 
> - _Vertices Scatter : `*.scatter(self_intersection_vertices[..., 0], self_intersection_vertices[..., 1])`_ 
> - _Polygon : `Polygon(self_intersection_vertices)`_ 


<br><br><br>

#### ___1. 2 ) Every Polygon has a `Triangulation`___<br>


>  ___🔺 Diagonal & Triangulation ▽___　
>  - _Diagonal : a line segment `connecting two vertices of P` and lying in the interior of P, not touching  ∂P except `at its endpoints`_
>  - _Triangulation : a decomposition of P into triangles by a maximal set of `noncrossing diagonals`_
> 　<br><br>
> 
>  ___💡 View Geometry ▽___
> <p align="center"><img src="https://user-images.githubusercontent.com/83874157/129746993-5c7ff2a4-162c-4089-9b9a-04598d45518b.png" width="377px"> <img src="https://user-images.githubusercontent.com/83874157/129747121-f545c560-a1d9-449d-80b5-ec66685d6253.png" width="370px"></p>


<br><br><br>

#### ___1. 3 ) Every triangulation of a polygon with `n vertices` has `n-2 triangles`___<br>


>  ___💡 View Geometry ▽___
> <p align="center"><img src="https://user-images.githubusercontent.com/83874157/129749379-61a10c7e-c0e6-4a72-b2d4-32c21a7e68ec.png" width="750px"></p>
> 　<br>
> 
> ___🔺 Triangulation Annotation ▽___
> - _Triangulation of a Polygon 1 : vertices_n = 7, triangles_n = 5_
> - _Triangulation of a Polygon 2 : vertices_n = 5, triangles_n = 3_
