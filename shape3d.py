from OpenGL.GL import *
from math import sin, cos, pi
import copy


class Vertex3d():

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_list(self):
        return [self.x, self.y,self.z]

class Line3d():
    def __init__(self, x1, y1,z1, x2, y2,z2):
        self.line = [Vertex3d(x1, y1,z1), Vertex3d(x2, y2,z2)]

    def draw(self):
        glBegin(GL_LINES)
        glColor3fv((1, 1, 1))
        for vertex in self.line:
            glVertex3fv(vertex.get_list())

        glEnd()




class Cube():
    def __init__(self,x,y,z,width):
        self.x = x
        self.y = y
        self.z = z
        self.width = width

        self.vertices = self.__create_edges(self.x,self.y,self.z,self.width)

    def __create_edges(self, x, y,z, width):
        points_list = list()

        points_list.append(Vertex3d(x, y, z))
        points_list.append(Vertex3d(x + width, y,z))
        points_list.append(Vertex3d(x + width, y + width,z))
        points_list.append(Vertex3d(x, y + width,z))

        points_list.append(Vertex3d(x, y, z+width))
        points_list.append(Vertex3d(x + width, y, z+width))
        points_list.append(Vertex3d(x + width, y + width, z+width))
        points_list.append(Vertex3d(x, y + width, z+width))

        return points_list

    def draw(self):
        glBegin(GL_TRIANGLES)
        #glColor3fv((0, 1, 0))
        #lado 1
        glVertex3fv(self.vertices[0].get_list())
        glVertex3fv(self.vertices[1].get_list())
        glVertex3fv(self.vertices[2].get_list())

        glVertex3fv(self.vertices[2].get_list())
        glVertex3fv(self.vertices[0].get_list())
        glVertex3fv(self.vertices[3].get_list())
        #lado 2
        glVertex3fv(self.vertices[0].get_list())
        glVertex3fv(self.vertices[4].get_list())
        glVertex3fv(self.vertices[7].get_list())

        glVertex3fv(self.vertices[7].get_list())
        glVertex3fv(self.vertices[0].get_list())
        glVertex3fv(self.vertices[3].get_list())

        #lado 3

        glVertex3fv(self.vertices[1].get_list())
        glVertex3fv(self.vertices[5].get_list())
        glVertex3fv(self.vertices[6].get_list())

        glVertex3fv(self.vertices[6].get_list())
        glVertex3fv(self.vertices[1].get_list())
        glVertex3fv(self.vertices[2].get_list())

        #lado 4
        glVertex3fv(self.vertices[2].get_list())
        glVertex3fv(self.vertices[6].get_list())
        glVertex3fv(self.vertices[7].get_list())

        glVertex3fv(self.vertices[7].get_list())
        glVertex3fv(self.vertices[2].get_list())
        glVertex3fv(self.vertices[3].get_list())

        # lado 5
        glVertex3fv(self.vertices[1].get_list())
        glVertex3fv(self.vertices[5].get_list())
        glVertex3fv(self.vertices[4].get_list())

        glVertex3fv(self.vertices[4].get_list())
        glVertex3fv(self.vertices[1].get_list())
        glVertex3fv(self.vertices[0].get_list())

        # lado 6
        glVertex3fv(self.vertices[4].get_list())
        glVertex3fv(self.vertices[5].get_list())
        glVertex3fv(self.vertices[6].get_list())

        glVertex3fv(self.vertices[6].get_list())
        glVertex3fv(self.vertices[4].get_list())
        glVertex3fv(self.vertices[7].get_list())

        glEnd()

class Cuboid():
    def __init__(self,x,y,z,width, height):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.heigth = height

    def __create_points(self,x,y,width,heigth):
        points_list = list()

        points_list.append(Vertex3d(x, y, z))
        points_list.append(Vertex3d(x + width, y, z))
        points_list.append(Vertex3d(x + width, y + width, z))
        points_list.append(Vertex3d(x, y + width, z))

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



class Sphere():
    pass

class Pyramid():
    pass
