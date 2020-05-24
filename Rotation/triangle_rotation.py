import numpy
import random
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import definitions
from definitions import *

DEGREE_90 = 1
DEGREE_180 = 2
DEGREE_270 = 3

def rotate(triangle, angle):
    triangle_matrix = numpy.array(definitions.get_triangle_coordinates_list(triangle))
    rotate_matrix = numpy.array([[0, 0], [0, 0]])
    if angle == DEGREE_90:
        rotate_matrix[0, 1] = 1
        rotate_matrix[1, 0] = -1
    elif angle == DEGREE_180:
        rotate_matrix[0, 0] = -1
        rotate_matrix[1, 1] = -1
    elif angle == DEGREE_270:
        rotate_matrix[0, 1] = -1
        rotate_matrix[1, 0] = 1
    
    new_co_ords = numpy.mat(triangle_matrix) * numpy.mat(rotate_matrix)
    A = Point(new_co_ords[0, 0], new_co_ords[0, 1])
    B = Point(new_co_ords[1, 0], new_co_ords[1, 1])
    C = Point(new_co_ords[2, 0], new_co_ords[2, 1])
    return Triangle(A, B, C)

def reshape(_w, _h):
    glViewport(0, 0, _w, _h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, _w/_h, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glTranslatef(0.0, 0.0, 0.0)

    triangle = Triangle(Point(0, 3), Point(3, 0), Point(-3, 0))

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    A = triangle.getPointA()
    B = triangle.getPointB()
    C = triangle.getPointC()
    glVertex2f(A.getX(), A.getY())
    glVertex2f(B.getX(), B.getY())
    glVertex2f(C.getX(), C.getY())
    glEnd()

    x = random.uniform(-2.0, 2.0)
    y = random.uniform(-2.0, 2.0)
    new_triangle = rotate(triangle, DEGREE_270)
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    A = new_triangle.getPointA()
    B = new_triangle.getPointB()
    C = new_triangle.getPointC()
    glVertex2f(A.getX(), A.getY())
    glVertex2f(B.getX(), B.getY())
    glVertex2f(C.getX(), C.getY())
    glEnd()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 0)
wind = glutCreateWindow("Rotations at angles 90/180/270")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
