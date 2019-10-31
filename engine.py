import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#from cube import *

from shapes import *


if __name__ == "__main__":
    pygame.init()
    display = (700, 700)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    # Pode utilizar o Perspective
    gluPerspective(45, display[0]/display[1], 0.1, 500.0 )
    glTranslate(0.0, 0.0, -25)

    #glEnable(GL_BLEND)
    #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


    # quad2 = Square(0, 0, 7)
    # quad = Rectangle(0, 0, 5,5)


    linex = Line(-10,0,0,10,0,0)
    liney = Line(0,-10,0,0,10,0)
    linez = Line(0,0,-10,0,0,10)
    triangulo = Triangle(0, 0, 5)
    quadrado = Square(0,0,2)
    circulo = Circle(0,0,2,20)
    cubo = Cube(0,0,0,5)
    ponto = Vertex(2,2)
    esfera = Sphere(0,0,0,5,20)

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

        triangulo.draw()
        triangulo.scale(2,2,2)
        #quadrado.draw()
        #quadrado.translation(1,0)
        #circulo.draw()
        #circulo.translation(1,0)
        #cubo.draw()
        #cubo.translation(0,0,0)
        #esfera.draw()
        #esfera.translation(0,0,0)


        linex.draw()
        liney.draw()
        linez.draw()



        pygame.display.flip()
        pygame.time.wait(100)
