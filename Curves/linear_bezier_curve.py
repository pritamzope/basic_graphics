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


def linear_bezier_curve(c0, c1):
    # c(t) = a c0 + b c1  ...(equ 1)
    # where a = (1 - t) & b = t and 2 control points c0, c1
    # so that,
    # c(t) = (1 − t)c0 + tc1 for t ∈ [0...1]
    
    glBegin(GL_LINE_STRIP)
    for i in range(0, 100):
        # get t fraction in between 0 & 1 (t ∈ [0...1])
        t = 0.01 * i
        a = (1 - t)
        b = t
        # get x with equ 1 with x in control points
        x = a * c0.getX() + b * c1.getX()
        # get y with equ 1 with y in control points
        y = a * c0.getY() + b * c1.getY()
        glVertex2f(x, y)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glTranslatef(0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 1.0)

    for i in range(0, 10):
        x = random.uniform(-5.0, 5.0)
        y = random.uniform(-5.0, 5.0)
        c0 = Point(x ,y)
        x = random.uniform(-5.0, 5.0)
        y = random.uniform(-5.0, 5.0)
        c1 = Point(x ,y)
        linear_bezier_curve(c0, c1)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 0)
wind = glutCreateWindow("Linear Bezier Curves")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
gluOrtho2D(0.0,250.0,0.0,300.0)
glutMainLoop()
