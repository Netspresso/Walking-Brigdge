import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb
import math
# import numpy as np

apex.setScriptUnitSystem(unitSystemName=r'''mm-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(
    applicationSettingsGeometry=applicationSettingsGeometry)
model_1 = apex.currentModel()

#
# Start of recorded operations
#


# Class defining curves
class Curves:
    def __init__(self, a, b, Velocity, Distance, ListPoint):
        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            Curves.x = a[i] * math.cos(t) - (5 * t) / (4 * math.pi) + 16.2
            Curves.y = b[i] * math.sin(t)
            Curves.z = Velocity * t + Distance
            ListPoint.append(
                createPointXYZ(x=Curves.x, y=Curves.y, z=Curves.z).asPoint())
            t += 0.1


def a(tmax, Step, component):
    """Inner radius(f) (from center to the beam)"""
    radius = []
    t = 0
    while t <= tmax:
        radius.append((-5 / (4 * math.pi)) * t + 10 + component)
        t += Step

    return radius


def b(tmax, Step, component):
    """distance between borders of beams """
    radius = []
    t = 0
    while t <= tmax:
        radius.append((-5 / (4 * math.pi)) * t + 7.5 + component)
        t += Step
    return radius


def linspace(low, up, leng):
    list = []
    step = (up - low) / float(leng)
    for i in range(leng):
        list.append(low)
        low = low + step
    return list


# Velocity of growing curves
v = 2.0 / math.pi

# other lenght in meters:
br_width = 0.5
spacing = 0.2
plinth = 0.15
beam_width = 2.0 * plinth + 3.0 * spacing
ibeam_height = -0.4
obeam_height = -0.5
plate_height = 0.25
pipe_diameter = 0.4
range_a = 4.0 * math.pi
range_b = 6.0 * math.pi
step = 0.1
beam_distance = 1.5
# thats all

# Lists of point for all curves
ptList = []
n_of_curve = 2
ncurve = []
curveSegment = []
designCurve = []
component = br_width + beam_width + pipe_diameter

for i in range(0, n_of_curve):
    ptList.append([])

CurvesList = [
    Curves(a(range_a, step, 0), b(range_b, step, 0), v, 0, ptList[0]),
    Curves(a(range_a, step, plinth), b(range_b, step, plinth), v, ibeam_height,
           ptList[1]),
    # Curves(a(range_a, step, plinth + spacing),
    #        b(range_b, step, plinth + spacing), v, 0, ptList[2]),
    # Curves(a(range_a, step, plinth + spacing),
    #        b(range_b, step, plinth + spacing), v, ibeam_height, ptList[3]),
    # Curves(a(range_a, step, 2.0 * spacing + plinth),
    #        b(range_b, step, 2.0 * spacing + plinth), v, 0, ptList[4]),
    # Curves(a(range_a, step, 2.0 * spacing + plinth),
    #        b(range_b, step, 2.0 * spacing + plinth), v, ibeam_height,
    #        ptList[5]),
    # Curves(a(range_a, step, 3.0 * spacing + 2.0 * plinth),
    #        b(range_b, step, 3.0 * spacing + 2.0 * plinth), v, 0, ptList[6]),
    # Curves(a(range_a, step, 3.0 * spacing + plinth),
    #        b(range_b, step, 3.0 * spacing + plinth), v, ibeam_height,
    #        ptList[7]),
    # Curves(a(range_a, step, beam_distance), b(range_b, step, beam_distance), v,
    #        0, ptList[8]),
    # Curves(a(range_a, step, beam_distance + plinth),
    #        b(range_b, step, beam_distance + plinth), v, obeam_height,
    #        ptList[9]),
    # Curves(a(range_a, step, beam_distance + plinth + spacing),
    #        b(range_b, step, beam_distance + plinth + spacing), v, 0,
    #        ptList[10]),
    # Curves(a(range_a, step, beam_distance + plinth + spacing),
    #        b(range_b, step, beam_distance + plinth + spacing), v, obeam_height,
    #        ptList[11]),
    # Curves(a(range_a, step, beam_distance + plinth + 2.0 * spacing),
    #        b(range_b, step, beam_distance + plinth + 2.0 * spacing), v, 0,
    #        ptList[12]),
    # Curves(a(range_a, step, beam_distance + plinth + 2.0 * spacing),
    #        b(range_b, step, beam_distance + plinth + 2.0 * spacing), v,
    #        obeam_height, ptList[13]),
    # Curves(a(range_a, step, beam_distance + 2.0 * plinth + 3.0 * spacing),
    #        b(range_b, step, beam_distance + 2.0 * plinth + 3.0 * spacing), v,
    #        0, ptList[14]),
    # Curves(a(range_a, step, beam_distance + plinth + 3.0 * spacing),
    #        b(range_b, step, beam_distance + plinth + 3.0 * spacing), v,
    #        obeam_height, ptList[15]),
    # Curves(a(range_a, step, beam_distance + beam_width + br_width),
    #        b(range_b, step, beam_distance + beam_width + br_width), v,
    #        plate_height, ptList[16]),
    # Curves(a(range_a, step, -br_width), b(range_b, step, -br_width), v,
    #        plate_height, ptList[17])
]


for Curve in range(0, len(ptList)):
    Lista = ptList[Curve]
    n = len(Lista)
    deg = 3
    m = n + deg + 1
    controlPoints = Lista
    knotPoints = linspace(0, 1, m)
    createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()