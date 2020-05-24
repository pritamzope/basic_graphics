import numpy
import random
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import definitions
from definitions import *


def transform(line, x, y):
    x1 = line.getPointA().getX()
    y1 = line.getPointA().getY()
    x2 = line.getPointB().getX()
    y2 = line.getPointB().getY()
    A = Point(x1 + x, y1 + y)
    B = Point(x2 + x, y2 + y)
    return Line(A, B)

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

    line_P = Line(Point(1, 1), Point(-1, -1))

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    A = line_P.getPointA()
    B = line_P.getPointB()
    glVertex2f(A.getX(), A.getY())
    glVertex2f(B.getX(), B.getY())
    glEnd()

    for i in range(0, 10):
        x = random.uniform(-4.0, 4.0)
        y = random.uniform(-4.0, 4.0)
        new_line = transform(line_P, x, y)
        glColor3f(0.0, 1.0, 1.0)
        glBegin(GL_LINES)
        A = new_line.getPointA()
        B = new_line.getPointB()
        glVertex2f(A.getX(), A.getY())
        glVertex2f(B.getX(), B.getY())
        glEnd()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 0)
wind = glutCreateWindow("Transformation Of Lines")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
