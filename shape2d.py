from OpenGL.GL import *

class Vertex():

    def __init__(self, x, y ):

        self.x = x
        self.y = y

    def get_list(self):
        return [self.x,self.y]

class Line():
    def __init__(self,x1,y1,x2,y2):

        self.line = [Vertex(x1,y1), Vertex(x2,y2)]

    def draw(self):
        glBegin(GL_LINES)
        glColor3fv((1,1,1))
        for vertex in self.line:
            glVertex2fv(vertex.get_list())

        glEnd()


class Triangle():

    def __init__(self,x,y,width):

        self.vertices = self.__create_edges(x,y,width)



    def __create_edges(self,x,y,width):
        points_list = list()


        points_list.append(Vertex(x, y))
        points_list.append(Vertex(x+width, y))
        points_list.append(Vertex(x + (width/2), y + width))


        return points_list




    def draw(self):

        glBegin(GL_TRIANGLES)
        glColor3fv((0,1,0))
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

        points_list.append((self.x,self.y))
        points_list.append((self.x + self.width, self.y))
        points_list.append((self.x + self.width, self.y + self.width))
        points_list.append((self.x , self.y + self.width))


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
    pass

class Circle():
    pass
