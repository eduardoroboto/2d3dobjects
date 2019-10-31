from OpenGL.GL import *
from math import sin, cos, pi
import copy

from matrix import Matrix



class Vertex():

    def __init__(self, x, y,z=None):
        self.x = x
        self.y = y

        if z is not None:
            self.z = z
        else:
            self.z = 0


    def draw(self):
        glBegin(GL_vertices)
        glColor3fv((1, 1, 1))
        glVertex3fv(self.get_list())
        glEnd()

    def get_list(self):
        return [self.x, self.y,self.z]


    def __to_matrix(self):
        return  Matrix(4,1,[self.x,self.y,self.z,1])

    def __from_matrix(self, matriz):
        self.x = matriz[1, 1]
        self.y = matriz[2, 1]
        self.z = matriz[3, 1]

    def update(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


    def translation(self,dx,dy,dz=None):
        vertexMatrix = self.__to_matrix()

        if dz is not None:
            translationMatrix = Matrix(4, 4, [1, 0, 0, dx, 0, 1, 0, dy, 0, 0, 1, dz, 0, 0, 0, 1])
            result = translationMatrix.dot(vertexMatrix)
        else:
            translationMatrix = Matrix(4, 4, [1, 0, 0, dx, 0, 1, 0, dy, 0, 0, 1, 0, 0, 0, 0, 1])
            result = translationMatrix.dot(vertexMatrix)

        return self.__from_matrix(result)


    def rotation(self,angle):
        pass

    def scale(self, dx, dy, dz=None):

        if dz is not None:
            vertexMatrix = Matrix(1, 3,[self.x, self.y, self.z])

            scaleMatrix = Matrix(3,3 ,[dx,0,0,0,dy,0,0,0,dz])
            result = vertexMatrix.dot(scaleMatrix)
            ok = result.return_list_rows(1)
            self.update(ok[0], ok[1], ok[2])
        else:
            vertexMatrix = Matrix(1, 2,[self.x, self.y])
            scaleMatrix = Matrix(2,2, [dx,0,0,dy,])
            result =vertexMatrix.dot(scaleMatrix)
            ok = result.return_list_rows(1)
            self.update(ok[0],ok[1],0)

    def reflection(self):
        pass

    def projection(self):
        pass

    def shear(self,angle):
        pass

class Shape():

    def translation(self, dx, dy, dz=None):
        for vertex in self.vertices:
            vertex.translation(dx,dy,dz)

    def rotation(self, angle):
        pass

    def scale(self, dx, dy, dz=None):
        for vertex in self.vertices:
            vertex.scale(dx, dy, dz)

    def reflection(self):
        pass

    def projection(self):
        pass

    def shear(self, angle):
        pass

class Line(Shape):
    def __init__(self, x1, y1, z1, x2, y2,z2):
        self.line = [Vertex(x1, y1,z1), Vertex(x2, y2,z2)]

    def draw(self):
        glBegin(GL_LINES)
        glColor3fv((1, 1, 1))
        for vertex in self.line:
            glVertex3fv(vertex.get_list())

        glEnd()




class Triangle(Shape):

    def __init__(self, x, y, width):
        self.vertices = self.__create_edges(x, y, width)

    def __create_edges(self, x, y, width):
        vertices_list = list()

        vertices_list.append(Vertex(x, y))
        vertices_list.append(Vertex(x + width, y))
        vertices_list.append(Vertex(x + (width / 2), y + width))

        return vertices_list

    def draw(self):
        glBegin(GL_TRIANGLES)
        glColor3fv((0, 1, 0))
        for vertex in self.vertices:
            glVertex3fv(vertex.get_list())

        glEnd()


class Square(Shape):
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.vertices = self.__create_vertices()

    def __create_vertices(self):
        vertices_list = list()

        vertices_list.append(Vertex(self.x, self.y))
        vertices_list.append(Vertex(self.x + self.width, self.y))
        vertices_list.append(Vertex(self.x + self.width, self.y + self.width))
        vertices_list.append(Vertex(self.x, self.y + self.width))

        return vertices_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glVertex3fv(self.vertices[0].get_list())
        glVertex3fv(self.vertices[1].get_list())
        glVertex3fv(self.vertices[2].get_list())

        glVertex3fv(self.vertices[2].get_list())
        glVertex3fv(self.vertices[0].get_list())
        glVertex3fv(self.vertices[3].get_list())

        glEnd()


class Rectangle(Shape):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vertices = self.__create_vertices()

    def __create_vertices(self):
        vertices_list = list()

        vertices_list.append((self.x, self.y))
        vertices_list.append((self.x + self.width, self.y))
        vertices_list.append((self.x + self.width, self.y + self.height))
        vertices_list.append((self.x, self.y + self.height))

        return vertices_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glVertex3fv(self.vertices[0])
        glVertex3fv(self.vertices[1])
        glVertex3fv(self.vertices[2])

        glVertex3fv(self.vertices[2])
        glVertex3fv(self.vertices[0])
        glVertex3fv(self.vertices[3])

        glEnd()


class Circle(Shape):

    def __init__(self, x, y, radius, number,):
        self.x = x
        self.y = y
        self.radius = radius
        self.number = number

        self.vertices = self.__create_edges(self.x, self.y, self.radius,self.number)

    def __create_edges(self, x, y, radius,number):
        vertices_list = list()

        hx = copy.copy(x)
        hy = copy.copy(y)
        angle = 2*pi / number
        for i in range(0, number):
            vertices_list.append(Vertex(hx, hy))
            x = radius * cos(i*angle)
            y =  radius * sin(i*angle)
            vertices_list.append(Vertex(x, y))
            x2 = radius * cos((i+1)*angle)
            y2 = radius * sin((i+1)*angle)
            vertices_list.append(Vertex(x2 , y2))


        return vertices_list


    def draw(self):

        # glBegin(GL_LINES)
        glBegin(GL_TRIANGLES)
        glColor4fv((1, 1, 1,1))
        color = 0

        for vertex in self.vertices:
            glVertex3fv(vertex.get_list())
            print(vertex.get_list())
            glColor4fv((1,1,1,color))
            color = color + 0.1

        glEnd()



class Cube(Shape):
    def __init__(self,x,y,z,width):
        self.x = x
        self.y = y
        self.z = z
        self.width = width

        self.vertices = self.__create_edges(self.x,self.y,self.z,self.width)

    def __create_edges(self, x, y,z, width):
        vertices_list = list()

        vertices_list.append(Vertex(x, y, z))
        vertices_list.append(Vertex(x + width, y,z))
        vertices_list.append(Vertex(x + width, y + width,z))
        vertices_list.append(Vertex(x, y + width,z))

        vertices_list.append(Vertex(x, y, z+width))
        vertices_list.append(Vertex(x + width, y, z+width))
        vertices_list.append(Vertex(x + width, y + width, z+width))
        vertices_list.append(Vertex(x, y + width, z+width))

        return vertices_list

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

class Cuboid(Shape):
    def __init__(self,x,y,z,width, height):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.heigth = height

    def __create_vertices(self,x,y,width,heigth):
        vertices_list = list()

        vertices_list.append(Vertex(x, y, z))
        vertices_list.append(Vertex(x + width, y, z))
        vertices_list.append(Vertex(x + width, y + width, z))
        vertices_list.append(Vertex(x, y + width, z))

        vertices_list.append((self.x, self.y))
        vertices_list.append((self.x + self.width, self.y))
        vertices_list.append((self.x + self.width, self.y + self.height))
        vertices_list.append((self.x, self.y + self.height))

        return vertices_list

    def draw(self):
        glBegin(GL_TRIANGLES)

        glVertex3fv(self.vertices[0])
        glVertex3fv(self.vertices[1])
        glVertex3fv(self.vertices[2])

        glVertex3fv(self.vertices[2])
        glVertex3fv(self.vertices[0])
        glVertex3fv(self.vertices[3])

        glEnd()

# matematica de mapepamento
# Result := ((Input - InputLow) / (InputHigh - InputLow)) \
#          * (OutputHigh - OutputLow) + OutputLow;
def MAP(input, inputLow,inputHigh, outputLow ,outputHigh):
    result = ((input - inputLow) / (inputHigh - inputLow)) * (outputHigh - outputLow) + outputLow

    return result





class Sphere(Shape):
    def __init__(self,x,y,z,radius,total):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.total = total
        self.halfPI = pi / 2

        self.vertices = self.__creat_vertices()


    def __creat_vertices(self):
        globe = Matrix(self.total+1,self.total+1)

        for i in range(self.total+1):
            lon = MAP(i, 0, self.total,-pi,pi)
            for j in range(self.total+1):
                lat = MAP(j, 0, self.total, -self.halfPI, self.halfPI)
                xC = self.radius * sin(lon) * cos(lat)
                yC = self.radius * sin(lon) * sin(lat)
                zC = self.radius * cos(lon)
                globe[i,j] = Vertex(xC+self.x, yC+self.y, zC+self.z)

        return globe

    def __draw(self):
        #for point in self.vertices:
        for i in range(self.total):
            for j in range(self.total + 1):
                self.vertices[i,j].draw()


    def __draw(self):
        glBegin(GL_TRIANGLES)
        for i in range(self.total):
            for j in range(self.total + 1):
                glVertex3fv(self.vertices[i, j].get_list())
                glVertex3fv(self.vertices[i + 1, j].get_list())

    #GL_TRIANGLE_STRIP
    def draw(self):
        glBegin(GL_TRIANGLE_STRIP)
        glColor4fv((0, 0, 1,0.3))
        for i in range(self.total):
            for j in range(self.total+1):
                glVertex3fv(self.vertices[i,j].get_list())
                glVertex3fv(self.vertices[i+1,j].get_list())

        glEnd()


    def translation(self, dx, dy, dz=None):
        if dz is not None:
            for i in range(self.total):
                for j in range(self.total + 1):
                    self.vertices[i,j].translation(dx,dy,dz)
                    self.vertices[i+1, j].translation(dx, dy, dz)
        else:
            for i in range(self.total):
                for j in range(self.total + 1):
                    self.vertices[i,j].translation(dx,dy,0)
                    self.vertices[i + 1, j].translation(dx, dy, 0)


class Pyramid(Shape):
    pass


class Matris():
    def __init__(self, rows, cols, data=[]):
        self.rows = rows
        self.cols = cols
        self._init_data(data)

        if data:
            data = (self.rows + self.cols) * [0]

    def __getitem__(self, key):
            i, j = key
            self.__valor_invalido(i, j)
            return self.data[(j - 1) + (i - 1) * self.cols]


    def __setitem__(self, key, value):
            i, j = key
            self.__valor_invalido(i, j)
            self.data[(j - 1) + (i - 1) * self.cols] = value

