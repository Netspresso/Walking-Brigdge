import math
import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb


class Curves:
    '''Klasa tworząca punkty przepon'''
    def __init__(self, a, b, Velocity, Distance, ListPoint):
        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            self.x = a[i] * math.cos(t) - (5 * t) / (4 * math.pi) + 19
            self.y = b[i] * math.sin(t)
            self.z = Velocity * t + Distance
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += math.pi / 4.0


class Curves_up():
    '''Klasa tworząca punkty leżące na krzywej. Dla krzywych zawierających się w płycie pomostowej.'''
    def __init__(self, a, b, Velocity, Distance, ListPoint):

        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            self.x = a[i] * math.cos(t) - (5 * t) / (4 * math.pi) + 19
            self.y = b[i] * math.sin(t)
            self.z = Velocity * t + Distance
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += 0.1


class Curves_down():
    '''Klasa tworząca punkty leżące na krzywej. Dla krzywych zawierających się w pasie dolnym dźwigara. Uwzględnia wypuszczenie blach w dolnej części kładki na potrzeby dobrego zakotwienia w żelbetowym przyczółku'''
    def __init__(self, a, b, Distance, ListPoint):

        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            self.x = a[i] * math.cos(t) - (5 * t) / (4 * math.pi) + 19
            self.y = b[i] * math.sin(t)
            if t <= math.pi / 8.0:
                self.z = 9.6 / math.pi * t - 0.95 + Distance
            else:
                self.z = 2.0 / math.pi * t + Distance
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += 0.1


class Straight_line():
    '''Klasa tworząca punkty leżące w płaskim odcinku przęsła'''
    def __init__(self, component, Distance, ListPoint):
        x = 13
        while x >= 0:
            self.x = x
            self.y = 1.875 + component
            self.z = 9 + Distance
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            x -= 1


class Elipsa:
    '''Class defining elipses'''
    def __init__(self, a, z, ListPoint):
        t = 0
        count = len(a)
        r = range(0, count)
        for i in r:
            self.x = 6 * math.cos(t) + 5 + 3 + 6
            self.y = 3.5 * math.sin(t)
            ListPoint.append(createPointXYZ(x=self.x, y=self.y, z=z).asPoint())
            t += math.pi / 24.0


class Elipsa_2:
    '''Class defining elipses'''
    def __init__(self, a, z, ListPoint):
        t = 0
        count = len(a)
        r = range(0, count)
        for i in r:
            self.x = 2 * math.cos(t) + 5 + 3 + 2
            self.y = math.sin(t)
            ListPoint.append(createPointXYZ(x=self.x, y=self.y, z=z).asPoint())
            t += math.pi / 24.0


def linspace(low, up, leng):
    """function creating a linear space from [low] to [up] using [leng] number of elements"""
    list = []
    step = (up - low) / float(leng)
    for i in range(leng):
        list.append(low)
        low = low + step
    return list


def a(tmax, step, component):
    """Funkcja zwracająca tablicę zawierającą długości większej ogniskowej, wyznaczone w zależności od parametru t"""
    focal_length = []
    t = 0
    while t <= tmax:
        focal_length.append((-5 / (4 * math.pi)) * t + 10 + component)
        t += step
    return focal_length


def b(tmax, step, component):
    """Funkcja zwracająca tablicę zawierającą długości mniejszej ogniskowej, wyznaczone w zależności od parametru t"""
    focal_length = []
    t = 0
    while t <= tmax:
        focal_length.append((-5 / (4 * math.pi)) * t + 7.5 + component)
        t += step
    return focal_length


def odstep_slupa(t):
    if (t >= 0 and t < math.pi):
        return -2 / math.pi * t + 5
    elif (t >= 1 * math.pi and t < 2 * math.pi):
        return 1 / math.pi * t + 2
    elif (t >= 2 * math.pi and t < 3 * math.pi):
        return -1 / math.pi * t + 6
    elif (t >= 3 * math.pi and t < 4 * math.pi):
        return 3
    elif (t >= 4 * math.pi and t < 5 * math.pi):
        return -2 / math.pi * t + 12


def ap(tmax, Step, component):
    """Inner radius(f) (from center to the beam)"""
    radius = []

    t = 0
    while t <= tmax:
        radius.append((-5 / (4 * math.pi)) * t + 10 - component(t))
        t += Step
    return radius


def b_p(tmax, Step, component):
    """Inner radius(f) (from center to the beam)"""
    radius = []

    t = 0
    while t <= tmax:
        radius.append((-5 / (4 * math.pi)) * t + 7.5 - component(t))
        t += Step
    return radius
