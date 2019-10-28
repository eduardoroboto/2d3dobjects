import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from cube import *

from shape2d import *




if __name__ == "__main__":
    pygame.init()
    display = (700, 700)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    # Pode utilizar o Perspective
    gluPerspective(45, display[0]/display[1], 0.1, 50.0 )
    glTranslate(0.0, 0.0, -25)
    quad = Triangle(0,0,5)

    linex = Line(-10,0,10,0)
    liney = Line(0,-10,0,10)

    # liney

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        # glRotate(1,0,0,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # cube()
        quad.draw()
        linex.draw()
        liney.draw()

        pygame.display.flip()
        pygame.time.wait(10)
