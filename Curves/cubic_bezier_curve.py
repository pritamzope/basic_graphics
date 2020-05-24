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


def cubic_bezier_curve(c0, c1, c2, c3):
    # c(t) = a^3 c0 + 3a^2b c1 + 3ab^2 c2 + b^3 c3  ...(equ 1)
    # where a = (1 - t) & b = t and 4 control points c0, c1, c2, c3
    # so that,
    # c(t) = (1 − t)^3 c0 + 3t(1 − t)^2 c1 + 3t^2(1 − t)c2 + t^3 c3 for t ∈ [0...1]
    
    glBegin(GL_LINE_STRIP)
    for i in range(0, 100):
        # get t fraction in between 0 & 1 (t ∈ [0...1])
        t = 0.01 * i
        a = (1 - t)
        b = t
        # get x with equ 1 with x in control points
        x = (a**3)*c0.getX() + (3*(a**2)*b)*c1.getX() + (3*a*(b**2))*c2.getX() + (b**2)*c3.getX()
        # get y with equ 1 with y in control points
        y = (a**3)*c0.getY() + (3*(a**2)*b)*c1.getY() + (3*a*(b**2))*c2.getY() + (b**2)*c3.getY()
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
        x = random.uniform(-5.0, 5.0)
        y = random.uniform(-5.0, 5.0)
        c2 = Point(x ,y)
        x = random.uniform(-5.0, 5.0)
        y = random.uniform(-5.0, 5.0)
        c3 = Point(x ,y)
        cubic_bezier_curve(c0, c1, c2, c3)

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 0)
wind = glutCreateWindow("Cubic Bezier Curves")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
gluOrtho2D(0.0,250.0,0.0,300.0)
glutMainLoop()
