import numpy
import random
import OpenGL
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import definitions
from definitions import *

def reflection_at_y(triangle):
    triangle_matrix = numpy.array(definitions.get_triangle_coordinates_list(triangle))
    reflect_matrix = numpy.array([[1, 0], [0, -1]])
    new_co_ords = numpy.mat(triangle_matrix) * numpy.mat(reflect_matrix)
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
    glColor3f(1.0, 1.0, 1.0)

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

    reflected_triangle = reflection_at_y(triangle)
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    A = reflected_triangle.getPointA()
    B = reflected_triangle.getPointB()
    C = reflected_triangle.getPointC()
    glVertex2f(A.getX(), A.getY())
    glVertex2f(B.getX(), B.getY())
    glVertex2f(C.getX(), C.getY())
    glEnd()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 0)
wind = glutCreateWindow("Reflection")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
gluOrtho2D(0.0,250.0,0.0,300.0)
glutMainLoop()
