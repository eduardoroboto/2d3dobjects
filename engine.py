import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from cube import *

from shape2d import *
from shape2d import Rectangle

if __name__ == "__main__":
    pygame.init()
    display = (700, 700)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    # Pode utilizar o Perspective
    gluPerspective(45, display[0]/display[1], 0.1, 500.0 )
    glTranslate(0.0, 0.0, -25)


    # quad2 = Square(0, 0, 7)
    # quad = Rectangle(0, 0, 5,5)


    linex = Line(-10,0,10,0)
    liney = Line(0,-10,0,10)
    # linez = Line(0,-10,0,10)
    #quad = Triangle(0, 0, 5)
    cc = Circle(0,0,2,20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("clicado")
                    #quad2.draw()


        mouseMove = pygame.mouse.get_rel()

        glRotate(mouseMove[0] * 0.2, 0.0, 1.0, 0.0)
        glRotate(mouseMove[1] * 0.2, 1.0, 0.0, 0.0)

        # glRotate(1,0,0,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # cube()
        # quad.draw()
        #quad2.draw()
        cc.draw()

        linex.draw()
        liney.draw()


        pygame.display.flip()
        pygame.time.wait(10)
