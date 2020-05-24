import random
import OpenGL
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import definitions
from definitions import *

def reshape(_w, _h):
    glViewport(0, 0, _w, _h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, _w/_h, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


def circle(x, y, radius):
    glBegin(GL_POINTS)
    for i in range(0, 360):
        _x = x + radius * math.cos(i)
        _y = y + radius * math.sin(i)
        glVertex2f(_x, _y)
    glEnd()


def ellipse(x, y, radius, x_width, y_width):
    glBegin(GL_POINTS)
    for i in range(0, 360):
        _x = x + (x_width/2) * radius * math.cos(i)
        _y = y + (y_width/2) * radius * math.sin(i)
        glVertex2f(_x, _y)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glTranslatef(0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 1.0)

    for i in range(0, 5):
        x = random.uniform(-5.0, 5.0)
        y = random.uniform(-5.0, 5.0)
        radius = random.uniform(0, 4.0)
        circle(x, y, radius)

    for i in range(0, 5):
        x = random.uniform(-5.0, 5.0)
        y = random.uniform(-5.0, 5.0)
        radius = random.uniform(0, 4.0)
        x_width = random.uniform(0, 5.0)
        y_width = random.uniform(0, 5.0)
        ellipse(x, y, radius, x_width, y_width)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 0)
wind = glutCreateWindow("Transformation Of Points")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
gluOrtho2D(0.0,250.0,0.0,300.0)
glutMainLoop()
