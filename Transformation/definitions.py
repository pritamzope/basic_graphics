class Point():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y


class Line():
    def __init__(self, A, B):
        self.__A = A
        self.__B = B
    def getPointA(self):
        return self.__A
    def getPointB(self):
        return self.__B
    def setPointA(self, A):
        self.__A = A
    def setPointB(self, B):
        self.__B = B

class Triangle():
    def __init__(self, A, B, C):
        self.__A = A
        self.__B = B
        self.__C = C
    def getPointA(self):
        return self.__A
    def getPointB(self):
        return self.__B
    def getPointC(self):
        return self.__C
    def setPointA(self, A):
        self.__A = A
    def setPointB(self, B):
        self.__B = B
    def setPointC(self, C):
        self.__C = C


def get_point_coordinates_list(p):
    l = list()
    l.append(p.getX())
    l.append(p.getY())
    return l

def get_line_coordinates_list(line):
    l = list()
    l.append(get_point_coordinates_list(line.getPointA()))
    l.append(get_point_coordinates_list(line.getPointB()))
    return l

def get_triangle_coordinates_list(t):
    l = list()
    l.append(get_point_coordinates_list(t.getPointA()))
    l.append(get_point_coordinates_list(t.getPointB()))
    l.append(get_point_coordinates_list(t.getPointC()))
    return l

