from dataclasses import dataclass


@dataclass
class Point3D:
    x: float
    y: float
    z: float
    ix: int
    iy: int

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y