from OpenGL.GL import *
from math import sin, cos, pi
import copy


class Vertex():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_list(self):
        return [self.x, self.y]


class Line():
    def __init__(self, x1, y1, x2, y2):
        self.line = [Vertex(x1, y1), Vertex(x2, y2)]

    def draw(self):
        glBegin(GL_LINES)
        glColor3fv((1, 1, 1))
        for vertex in self.line:
            glVertex2fv(vertex.get_list())

        glEnd()


class Triangle():

    def __init__(self, x, y, width):
        self.vertices = self.__create_edges(x, y, width)

    def __create_edges(self, x, y, width):
        points_list = list()

        points_list.append(Vertex(x, y))
        points_list.append(Vertex(x + width, y))
        points_list.append(Vertex(x + (width / 2), y + width))

        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)
        glColor3fv((0, 1, 0))
        for vertex in self.vertices:
            glVertex2fv(vertex.get_list())

        glEnd()


class Square():
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.points = self.__create_points()

    def __create_points(self):
        points_list = list()

        points_list.append((self.x, self.y))
        points_list.append((self.x + self.width, self.y))
        points_list.append((self.x + self.width, self.y + self.width))
        points_list.append((self.x, self.y + self.width))

        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glVertex2fv(self.points[0])
        glVertex2fv(self.points[1])
        glVertex2fv(self.points[2])

        glVertex2fv(self.points[2])
        glVertex2fv(self.points[0])
        glVertex2fv(self.points[3])

        glEnd()


class Rectangle():

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.points = self.__create_points()

    def __create_points(self):
        points_list = list()

        points_list.append((self.x, self.y))
        points_list.append((self.x + self.width, self.y))
        points_list.append((self.x + self.width, self.y + self.height))
        points_list.append((self.x, self.y + self.height))

        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glVertex2fv(self.points[0])
        glVertex2fv(self.points[1])
        glVertex2fv(self.points[2])

        glVertex2fv(self.points[2])
        glVertex2fv(self.points[0])
        glVertex2fv(self.points[3])

        glEnd()


class Circle():

    def __init__(self, x, y, radius, number,):
        self.x = x
        self.y = y
        self.radius = radius
        self.number = number

        self.vertices = self.__create_edges(self.x, self.y, self.radius,self.number)

    def __create_edges(self, x, y, radius,number):
        points_list = list()
        # points_list.append(Vertex(x, y))
        # points_list.append(Vertex(x + width, y))
        # points_list.append(Vertex(x + width , y + width))
        # point_one.x = point_one.x + radius * cos(i)
        # point_one.y = point_one.y + radius * sin(i)

        hx = copy.copy(x)
        hy = copy.copy(y)
        angle = 2*pi / number
        for i in range(0, number):
            points_list.append(Vertex(hx, hy))
            x = radius * cos(i*angle)
            y =  radius * sin(i*angle)
            points_list.append(Vertex(x, y))
            x2 = radius * cos((i+1)*angle)
            y2 = radius * sin((i+1)*angle)
            points_list.append(Vertex(x2 , y2))


        return points_list


    def draw(self):

        # glBegin(GL_LINES)
        glBegin(GL_TRIANGLES)
        glColor4fv((1, 1, 1,1))
        color = 0

        for vertex in self.vertices:
            glVertex2fv(vertex.get_list())
            print(vertex.get_list())
            glColor4fv((1,1,1,color))
            color = color + 0.1

        glEnd()
