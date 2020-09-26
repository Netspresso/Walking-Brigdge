import math
import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb


def a(tmax, step, component):
    """Inner radius(f) (from center to the beam)"""
    radius = []

    t = 0
    while t <= tmax:
        radius.append((-5 / (4 * math.pi)) * t + 10 + component)
        t += step
    return radius


def b(tmax, step, component):
    """distance between borders of beams """
    radius = []

    t = 0
    while t <= tmax:
        radius.append((-5 / (4 * math.pi)) * t + 7.5 + component)
        t += step

    return radius


def linspace(low, up, leng):
    """function creating a linear space from [low] to [up] using [leng] number of elements"""
    list = []
    step = (up - low) / float(leng)
    for i in range(leng):
        list.append(low)
        low = low + step
    return list


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
