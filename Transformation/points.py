import numpy
import random
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from definitions import *

def transform(point, x, y):
    points_matrix = numpy.array([[point.getX(), point.getY()]])
    identity_matrix = numpy.array([[x, 0], [0, y]])
    new_co_ords = numpy.mat(points_matrix) * numpy.mat(identity_matrix)
    return Point(new_co_ords[0, 0], new_co_ords[0, 1])

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

    P = Point(1, 2)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_POINTS)
    glVertex2f(P.getX(), P.getY())
    glEnd()

    for i in range(0, 1000):
        x = random.uniform(-3.0, 3.0)
        y = random.uniform(-2.0, 2.0)
        new_point = transform(P, x, y)
        glColor3f(0.0, 1.0, 1.0)
        glBegin(GL_POINTS)
        glVertex2f(new_point.getX(), new_point.getY())
        glEnd()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 0)
wind = glutCreateWindow("Transformation Of Points")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
