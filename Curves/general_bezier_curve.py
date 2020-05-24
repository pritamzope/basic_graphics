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


# n = no of control points coordinates x/y
def get_c_of_t(n, t, control_points_coord_list):
    # b(t) = summation(i=0 to n) (n i) t^i (1 - t)^(n-i) bi
    # where factor (n i) = n! / i! (n - i)!
    result = 0
    for i in range(0, n):
        factor = math.factorial(n) / (math.factorial(i) * math.factorial(n - i))
        result += factor * (t ** i) * (1 - t)**(n - i) * control_points_coord_list[i]
    return result


def general_bezier_curve(control_points_list):

    control_points_list_x = list()
    control_points_list_y = list()

    for p in control_points_list:
        control_points_list_x.append(p.getX())
        control_points_list_y.append(p.getY())


    glBegin(GL_LINE_STRIP)
    for i in range(0, 100):
        # get t fraction in between 0 & 1 (t ∈ [0...1])
        t = 0.01 * i
        # get x from equation get_c_of_t()
        x = get_c_of_t(len(control_points_list_x), t, control_points_list_x)
        # get y from equation get_c_of_t()
        y = get_c_of_t(len(control_points_list_y), t, control_points_list_y)
        glVertex2f(x, y)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glTranslatef(0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 1.0)

    control_points_list = list()

    # add 10 random control points to list
    for i in range(0, 10):
        x = random.uniform(-5.0, 5.0)
        y = random.uniform(-5.0, 5.0)
        control_points_list.append(Point(x, y))

    general_bezier_curve(control_points_list)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 0)
wind = glutCreateWindow("General Bezier Curves")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
gluOrtho2D(0.0,250.0,0.0,300.0)
glutMainLoop()
