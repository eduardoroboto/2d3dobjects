from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    ( 1,   1,  1),  #A
    (-1,   1,  1),  #B
    ( 1,   1, -1),  #C
    (-1,   1, -1),  #D
    ( 1,  -1,  1),  #E
    (-1,  -1,  1),  #F
    ( 1,  -1, -1),  #G
    (-1,  -1, -1),  #H

)

edges = (
    (0, 1),
    (0, 2),
    (0, 4),
    (1, 3),
    (1, 5),
    (2, 3),
    (2, 6),
    (3, 7),
    (4, 5),
    (4, 6),
    (5, 7),
    (6, 7),
)


def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

