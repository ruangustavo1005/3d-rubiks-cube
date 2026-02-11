from math import pi
from typing import List
from vpython import vector, box

import cores


class Piece:
    def __init__(self, x: int, y: int, z: int) -> None:
        size = 0.9
        self.l_face = box(pos=vector(-size/2 + x, y, z), size=vector(0.97 - size, size, size), color=cores.VERMELHO if x == -1 else cores.PRETO) # Face esquerda
        self.r_face = box(pos=vector(+size/2 + x, y, z), size=vector(0.97 - size, size, size), color=cores.LARANJA  if x == +1 else cores.PRETO) # Face direita
        self.d_face = box(pos=vector(x, -size/2 + y, z), size=vector(size, 0.97 - size, size), color=cores.BRANCO   if y == -1 else cores.PRETO) # Face inferior
        self.u_face = box(pos=vector(x, +size/2 + y, z), size=vector(size, 0.97 - size, size), color=cores.AMARELO  if y == +1 else cores.PRETO) # Face superior
        self.b_face = box(pos=vector(x, y, -size/2 + z), size=vector(size, size, 0.97 - size), color=cores.AZUL     if z == -1 else cores.PRETO) # Face traseira
        self.f_face = box(pos=vector(x, y, +size/2 + z), size=vector(size, size, 0.97 - size), color=cores.VERDE    if z == +1 else cores.PRETO) # Face frontal

    def get_faces(self) -> List[box]:
        return [self.l_face, self.r_face, self.d_face, self.u_face, self.b_face, self.f_face]

    def rotate(self, axis: str, direction: int = 1) -> None:
        assert axis in ["x", "y", "z"], "Invalid axis"
        assert direction in [1, -1], "Invalid direction"
        axis_vector = vector(
            1 if axis == "x" else 0,
            1 if axis == "y" else 0,
            1 if axis == "z" else 0
        )
        angle = pi/2 * direction
        for face in self.get_faces():
            face.rotate(angle=angle, axis=axis_vector, origin=vector(0, 0, 0))
