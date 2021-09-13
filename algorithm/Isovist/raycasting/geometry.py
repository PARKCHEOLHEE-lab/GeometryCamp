import math
from typing import List, Tuple, Set, Sequence, Dict, Optional, Iterator

from main import SCREEN_H, SCREEN_W

hypotenuse = math.hypot # Hypotenuse : Longest Side of Right Triangle

def distance(coord_a: Tuple, coord_b: Tuple) -> float:
    """
    Calculate distance between two points in 2D space

    - param coord_a: Tuple -- (x, y) coords of first point
    - param coord_b: Tuple -- (x, y) coords of second point
    - return: float -- 2Dimensional distance between segment
    """
    return hypotenuse(coord_b[0]-coord_a[0], coord_b[1]-coord_a[1])


def calculate_vector_2d(angle: float, scalar: float) -> Tuple[float, float]:
    """
    Calculate x and y parts of the current vector

    - param angle: float -- angle of the vector
    - param scalar: float -- scalar value of the vector
    - return: Tuple -- x and y parts of the vector in format: (float, float)
    """
    
    radians = math.radians(angle)
    change_x = math.cos(radians)
    change_y = math.sin(radians)

    return change_x*scalar, change_y*scalar


def calculate_angle(start: Tuple, end: Tuple) -> float:
    
    radians = -math.atan2(end[0]-start[0], end[1]-start[1])

    return math.degrees(radians) % 360


if __name__ == "__main__":
    print(calculate_vector_2d(10, 5))