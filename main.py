from vpython import canvas, vector

from cube import Cube


scene = canvas(width=800, height=800)
scene.camera.pos = vector(0, 0, 7)
scene.camera.axis = vector(0, 0, -7)

cube = Cube()
# cube.scramble(1)
# cube.move("R F U2 B' R'")

# cubo no cubo
# cube.move("F L F U' R U F2 L2 U' L' B D' B' L2 U")
# cubo no cubo no cubo
cube.move("U' L' U' F' R2 B' R F U B2 U B' L U' F U R F'")
# c
# cube.move("U' B2 U L2 D L2 R2 D' B' R D' L R' B2 U2 F' L' U'")
 
input("Pressione qualquer tecla para sair")
