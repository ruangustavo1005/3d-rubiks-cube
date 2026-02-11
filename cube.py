from random import randint, random
from typing import Dict

from piece import Piece


class Cube:
    def __init__(self) -> None:
        self.__init_pieces()

    def __init_pieces(self):
        self.pieces: Dict[int, Dict[int, Dict[int, Piece]]] = {}
        for x in range(-1, 2):
            self.pieces[x] = {}
            for y in range(-1, 2):
                self.pieces[x][y] = {}
                for z in range(-1, 2):
                    self.pieces[x][y][z] = Piece(x, y, z)

    def scramble(self, total_moves: int = 10) -> None:
        moves_mapper = self.moves_mapper()
        moves_names = list(self.moves_mapper().keys())
        last_move_axis = ""
        for _ in range(total_moves):
            move_name = moves_names[randint(0, len(moves_names) - 1)]
            while move_name[0] == last_move_axis:
                move_name = moves_names[randint(0, len(moves_names) - 1)]
            last_move_axis = move_name[0]
            moves_mapper.get(move_name)()

    def move(self, moves: str) -> None:
        moves = moves.split(" ")
        moves_mapper = self.moves_mapper()
        for move in moves:
            if not moves_mapper.get(move):
                raise ValueError(f"Invalid move: {move}")
        for move in moves:
            moves_mapper.get(move)()

    def moves_mapper(self):
        return {
            "L": self.L,
            "R": self.R,
            "D": self.D,
            "U": self.U,
            "B": self.B,
            "F": self.F,
            "L'": self.L_,
            "R'": self.R_,
            "D'": self.D_,
            "U'": self.U_,
            "B'": self.B_,
            "F'": self.F_,
            "L2": self.L2,
            "R2": self.R2,
            "D2": self.D2,
            "U2": self.U2,
            "B2": self.B2,
            "F2": self.F2,
        }

    def __L(self, direction: int = 1) -> None:
        if direction == 1:
            aux = self.pieces[-1][0][1]
            self.pieces[-1][0][1] = self.pieces[-1][1][0]
            self.pieces[-1][1][0] = self.pieces[-1][0][-1]
            self.pieces[-1][0][-1] = self.pieces[-1][-1][0]
            self.pieces[-1][-1][0] = aux

            aux = self.pieces[-1][-1][1]
            self.pieces[-1][-1][1] = self.pieces[-1][1][1]
            self.pieces[-1][1][1] = self.pieces[-1][1][-1]
            self.pieces[-1][1][-1] = self.pieces[-1][-1][-1]
            self.pieces[-1][-1][-1] = aux
        else:
            aux = self.pieces[-1][-1][0]
            self.pieces[-1][-1][0] = self.pieces[-1][0][-1]
            self.pieces[-1][0][-1] = self.pieces[-1][1][0]
            self.pieces[-1][1][0] = self.pieces[-1][0][1]
            self.pieces[-1][0][1] = aux

            aux = self.pieces[-1][-1][1]
            self.pieces[-1][-1][1] = self.pieces[-1][-1][-1]
            self.pieces[-1][-1][-1] = self.pieces[-1][1][-1]
            self.pieces[-1][1][-1] = self.pieces[-1][1][1]
            self.pieces[-1][1][1] = aux

        for y in range(-1, 2):
            for z in range(-1, 2):
                self.pieces[-1][y][z].rotate("x", direction)

    def __R(self, direction: int = 1) -> None:
        if direction == 1:
            aux = self.pieces[1][-1][0]
            self.pieces[1][-1][0] = self.pieces[1][0][-1]
            self.pieces[1][0][-1] = self.pieces[1][1][0]
            self.pieces[1][1][0] = self.pieces[1][0][1]
            self.pieces[1][0][1] = aux

            aux = self.pieces[1][-1][1]
            self.pieces[1][-1][1] = self.pieces[1][-1][-1]
            self.pieces[1][-1][-1] = self.pieces[1][1][-1]
            self.pieces[1][1][-1] = self.pieces[1][1][1]
            self.pieces[1][1][1] = aux
        else:
            aux = self.pieces[1][0][1]
            self.pieces[1][0][1] = self.pieces[1][1][0]
            self.pieces[1][1][0] = self.pieces[1][0][-1]
            self.pieces[1][0][-1] = self.pieces[1][-1][0]
            self.pieces[1][-1][0] = aux

            aux = self.pieces[1][-1][1]
            self.pieces[1][-1][1] = self.pieces[1][1][1]
            self.pieces[1][1][1] = self.pieces[1][1][-1]
            self.pieces[1][1][-1] = self.pieces[1][-1][-1]
            self.pieces[1][-1][-1] = aux

        for y in range(-1, 2):
            for z in range(-1, 2):
                self.pieces[1][y][z].rotate("x", -direction)

    def __D(self, direction: int = 1) -> None:
        if direction == 1:
            aux = self.pieces[-1][-1][0]
            self.pieces[-1][-1][0] = self.pieces[0][-1][-1]
            self.pieces[0][-1][-1] = self.pieces[1][-1][0]
            self.pieces[1][-1][0] = self.pieces[0][-1][1]
            self.pieces[0][-1][1] = aux

            aux = self.pieces[-1][-1][1]
            self.pieces[-1][-1][1] = self.pieces[-1][-1][-1]
            self.pieces[-1][-1][-1] = self.pieces[1][-1][-1]
            self.pieces[1][-1][-1] = self.pieces[1][-1][1]
            self.pieces[1][-1][1] = aux
        else:
            aux = self.pieces[0][-1][1]
            self.pieces[0][-1][1] = self.pieces[1][-1][0]
            self.pieces[1][-1][0] = self.pieces[0][-1][-1]
            self.pieces[0][-1][-1] = self.pieces[-1][-1][0]
            self.pieces[-1][-1][0] = aux

            aux = self.pieces[-1][-1][1]
            self.pieces[-1][-1][1] = self.pieces[1][-1][1]
            self.pieces[1][-1][1] = self.pieces[1][-1][-1]
            self.pieces[1][-1][-1] = self.pieces[-1][-1][-1]
            self.pieces[-1][-1][-1] = aux

        for x in range(-1, 2):
            for z in range(-1, 2):
                self.pieces[x][-1][z].rotate("y", direction)

    def __U(self, direction: int = 1) -> None:
        if direction == 1:
            aux = self.pieces[0][1][1]
            self.pieces[0][1][1] = self.pieces[1][1][0]
            self.pieces[1][1][0] = self.pieces[0][1][-1]
            self.pieces[0][1][-1] = self.pieces[-1][1][0]
            self.pieces[-1][1][0] = aux

            aux = self.pieces[-1][1][1]
            self.pieces[-1][1][1] = self.pieces[1][1][1]
            self.pieces[1][1][1] = self.pieces[1][1][-1]
            self.pieces[1][1][-1] = self.pieces[-1][1][-1]
            self.pieces[-1][1][-1] = aux
        else:
            aux = self.pieces[-1][1][0]
            self.pieces[-1][1][0] = self.pieces[0][1][-1]
            self.pieces[0][1][-1] = self.pieces[1][1][0]
            self.pieces[1][1][0] = self.pieces[0][1][1]
            self.pieces[0][1][1] = aux
            
            aux = self.pieces[-1][1][1]
            self.pieces[-1][1][1] = self.pieces[-1][1][-1]
            self.pieces[-1][1][-1] = self.pieces[1][1][-1]
            self.pieces[1][1][-1] = self.pieces[1][1][1]
            self.pieces[1][1][1] = aux

        for x in range(-1, 2):
            for z in range(-1, 2):
                self.pieces[x][1][z].rotate("y", -direction)

    def __B(self, direction: int = 1) -> None:
        if direction == 1:
            aux = self.pieces[-1][0][-1]
            self.pieces[-1][0][-1] = self.pieces[0][1][-1]
            self.pieces[0][1][-1] = self.pieces[1][0][-1]
            self.pieces[1][0][-1] = self.pieces[0][-1][-1]
            self.pieces[0][-1][-1] = aux
            
            aux = self.pieces[-1][-1][-1]
            self.pieces[-1][-1][-1] = self.pieces[-1][1][-1]
            self.pieces[-1][1][-1] = self.pieces[1][1][-1]
            self.pieces[1][1][-1] = self.pieces[1][-1][-1]
            self.pieces[1][-1][-1] = aux
        else:
            aux = self.pieces[0][-1][-1]
            self.pieces[0][-1][-1] = self.pieces[1][0][-1]
            self.pieces[1][0][-1] = self.pieces[0][1][-1]
            self.pieces[0][1][-1] = self.pieces[-1][0][-1]
            self.pieces[-1][0][-1] = aux

            aux = self.pieces[-1][-1][-1]
            self.pieces[-1][-1][-1] = self.pieces[1][-1][-1]
            self.pieces[1][-1][-1] = self.pieces[1][1][-1]
            self.pieces[1][1][-1] = self.pieces[-1][1][-1]
            self.pieces[-1][1][-1] = aux

        for x in range(-1, 2):
            for y in range(-1, 2):
                self.pieces[x][y][-1].rotate("z", direction)

    def __F(self, direction: int = 1) -> None:
        if direction == 1:
            aux = self.pieces[0][-1][1]
            self.pieces[0][-1][1] = self.pieces[1][0][1]
            self.pieces[1][0][1] = self.pieces[0][1][1]
            self.pieces[0][1][1] = self.pieces[-1][0][1]
            self.pieces[-1][0][1] = aux

            aux = self.pieces[-1][-1][1]
            self.pieces[-1][-1][1] = self.pieces[1][-1][1]
            self.pieces[1][-1][1] = self.pieces[1][1][1]
            self.pieces[1][1][1] = self.pieces[-1][1][1]
            self.pieces[-1][1][1] = aux
        else:
            aux = self.pieces[-1][0][1]
            self.pieces[-1][0][1] = self.pieces[0][1][1]
            self.pieces[0][1][1] = self.pieces[1][0][1]
            self.pieces[1][0][1] = self.pieces[0][-1][1]
            self.pieces[0][-1][1] = aux
            
            aux = self.pieces[-1][-1][1]
            self.pieces[-1][-1][1] = self.pieces[-1][1][1]
            self.pieces[-1][1][1] = self.pieces[1][1][1]
            self.pieces[1][1][1] = self.pieces[1][-1][1]
            self.pieces[1][-1][1] = aux

        for x in range(-1, 2):
            for y in range(-1, 2):
                self.pieces[x][y][1].rotate("z", -direction)

    def L(self) -> None:
        print("L")
        self.__L()

    def R(self) -> None:
        print("R")
        self.__R()

    def D(self) -> None:
        print("D")
        self.__D()

    def U(self) -> None:
        print("U")
        self.__U()

    def B(self) -> None:
        print("B")
        self.__B()

    def F(self) -> None:
        print("F")
        self.__F()

    def L_(self) -> None:
        print("L'")
        self.__L(-1)

    def R_(self) -> None:
        print("R'")
        self.__R(-1)

    def D_(self) -> None:
        print("D'")
        self.__D(-1)

    def U_(self) -> None:
        print("U'")
        self.__U(-1)

    def B_(self) -> None:
        print("B'")
        self.__B(-1)

    def F_(self) -> None:
        print("F'")
        self.__F(-1)

    def L2(self) -> None:
        print("L2")
        self.__L()
        self.__L()

    def R2(self) -> None:
        print("R2")
        self.__R()
        self.__R()

    def D2(self) -> None:
        print("D2")
        self.__D()
        self.__D()

    def U2(self) -> None:
        print("U2")
        self.__U()
        self.__U()

    def B2(self) -> None:
        print("B2")
        self.__B()
        self.__B()

    def F2(self) -> None:
        print("F2")
        self.__F()
        self.__F()
