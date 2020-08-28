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
'''Here I began script'''
'''Classes'''


class curves:
    '''Class defining upper curves'''
    def __init__(self, a, b, Velocity, Distance, ListPoint):

        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            self.x = a[i] * math.cos(t) - (5 * t) / (4 * math.pi) + 15
            self.y = b[i] * math.sin(t)
            self.z = Velocity * t + Distance
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += 0.1


class curvesF:
    '''Class defining lower curves'''
    def __init__(self, a, b, Distance, ListPoint):

        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            self.x = a[i] * math.cos(t) - (5 * t) / (4 * math.pi) + 15
            self.y = b[i] * math.sin(t)
            if t <= math.pi / 8.0:
                self.z = 9.6 / math.pi * t - 0.95 + Distance
            else:
                self.z = 2.0 / math.pi * t + Distance
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += 0.1


class Elipsa:
    '''Class defining elipses'''
    def __init__(self, a, b, Height, distance, ListPoint):
        t = 0
        while t <= 2 * math.pi:
            self.x = a * math.cos(t) + distance
            self.y = b * math.sin(t)
            self.z = Height
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += 0.2


'''
class curvesE:
    #Class defining curves E

    def __init__(self, a, b, Distance, ListPoint):

        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            curvesE.x = -a[i] * math.cos(t) + (5 * t) / (4 * math.pi) - 15
            curvesE.y = -b[i] * math.sin(t)
            if t <= math.pi / 8.0:
                curvesE.z = 9.6 / math.pi * t - 1.0 + Distance
            else:
                curvesE.z = 2.0 / math.pi * t - 0.05 + Distance
            ListPoint.append(
                createPointXYZ(x=curvesE.x, y=curvesE.y,
                               z=curvesE.z).asPoint())
            t += 1
'''


class curvesB:
    '''Class defining flat and straight stretch'''
    def __init__(self, component, Distance, ListPoint):
        x = 9.375
        while x >= -8.0:
            curvesB.x = x
            curvesB.y = 1.875 + component
            curvesB.z = 9 + Distance
            ListPoint.append(
                createPointXYZ(x=curvesB.x, y=curvesB.y,
                               z=curvesB.z).asPoint())
            x -= 1


'''
class curvesD:
    def __init__(self, component, Distance, ListPoint):
        x = -9.375
        while x <= 8.0:
            curvesD.x = x
            curvesD.y = -1.875 - component
            curvesD.z = 9 + Distance
            ListPoint.append(
                createPointXYZ(x=curvesD.x, y=curvesD.y,
                               z=curvesD.z).asPoint())
'''
'''
class curvesC:
    def __init__(self, a, b, Velocity, Distance, ListPoint):
        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            curvesC.x = -a[i] * math.cos(t) + (5 * t) / (4 * math.pi) - 15
            curvesC.y = -b[i] * math.sin(t)
            curvesC.z = Velocity * t + Distance
            ListPoint.append(
                createPointXYZ(x=curvesC.x, y=curvesC.y,
                               z=curvesC.z).asPoint())
            t += 1
            '''
'''global functions:'''


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
    """function creating a linear space from [low] to [up] using [leng] number of elements"""
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
plate_height = 0
plate_bottom = 0.0
pipe_diameter = 0.4
range_a = 4.5 * math.pi
range_b = range_a
step = 0.1
beam_distance = 1.5
# thats all

# Lists of point for all curves
ptList = []
n_of_curve = 18
component = br_width + beam_width + pipe_diameter

for i in range(0, n_of_curve):
    ptList.append([])

curves(a(range_a, step, 0), b(range_b, step, 0), v, 0, ptList[0])
curvesB(0, 0, ptList[0])
curvesF(a(range_a, step, plinth), b(range_b, step, plinth), ibeam_height,
        ptList[1])
curvesB(plinth, ibeam_height, ptList[1])
curves(a(range_a, step, plinth + spacing), b(range_b, step, plinth + spacing),
       v, 0, ptList[2])
curvesB(plinth + spacing, 0, ptList[2])
curvesF(a(range_a, step, plinth + spacing), b(range_b, step, plinth + spacing),
        ibeam_height, ptList[3])
curvesB(plinth + spacing, ibeam_height, ptList[3])
curves(a(range_a, step, 2.0 * spacing + plinth),
       b(range_b, step, 2.0 * spacing + plinth), v, 0, ptList[4])
curvesB(2.0 * spacing + plinth, 0, ptList[4])
curvesF(a(range_a, step, 2.0 * spacing + plinth),
        b(range_b, step, 2.0 * spacing + plinth), ibeam_height, ptList[5])
curvesB(2.0 * spacing + plinth, ibeam_height, ptList[5])
curves(a(range_a, step, 3.0 * spacing + 2.0 * plinth),
       b(range_b, step, 3.0 * spacing + 2.0 * plinth), v, 0, ptList[6])
curvesB(3.0 * spacing + 2.0 * plinth, 0, ptList[6])
curvesF(a(range_a, step, 3.0 * spacing + plinth),
        b(range_b, step, 3.0 * spacing + plinth), ibeam_height, ptList[7])
curvesB(3.0 * spacing + plinth, ibeam_height, ptList[7])
curves(a(range_a, step, beam_distance), b(range_b, step, beam_distance), v, 0,
       ptList[8])
curvesB(beam_distance, 0, ptList[8])
curvesF(a(range_a, step, beam_distance + plinth),
        b(range_b, step, beam_distance + plinth), obeam_height, ptList[9])
curvesB(beam_distance + plinth, obeam_height, ptList[9])
curves(a(range_a, step, beam_distance + plinth + spacing),
       b(range_b, step, beam_distance + plinth + spacing), v, 0, ptList[10])
curvesB(beam_distance + plinth + spacing, 0, ptList[10])
curvesF(a(range_a, step, beam_distance + plinth + spacing),
        b(range_b, step, beam_distance + plinth + spacing), obeam_height,
        ptList[11])
curvesB(beam_distance + plinth + spacing, obeam_height, ptList[11])
curves(a(range_a, step, beam_distance + plinth + 2.0 * spacing),
       b(range_b, step, beam_distance + plinth + 2.0 * spacing), v, 0,
       ptList[12])
curvesB(beam_distance + plinth + 2.0 * spacing, 0, ptList[12])
curvesF(a(range_a, step, beam_distance + plinth + 2.0 * spacing),
        b(range_b, step, beam_distance + plinth + 2.0 * spacing), obeam_height,
        ptList[13])
curvesB(beam_distance + plinth + 2.0 * spacing, obeam_height, ptList[13])
curves(a(range_a, step, beam_distance + 2.0 * plinth + 3.0 * spacing),
       b(range_b, step, beam_distance + 2.0 * plinth + 3.0 * spacing), v, 0,
       ptList[14])
curvesB(beam_distance + 2.0 * plinth + 3.0 * spacing, 0, ptList[14])
curvesF(a(range_a, step, beam_distance + plinth + 3.0 * spacing),
        b(range_b, step, beam_distance + plinth + 3.0 * spacing), obeam_height,
        ptList[15])
curvesB(beam_distance + plinth + 3.0 * spacing, obeam_height, ptList[15])
curves(a(range_a, step, beam_distance + beam_width + br_width),
       b(range_b, step, beam_distance + beam_width + br_width), v,
       plate_height, ptList[16])
curvesB(beam_distance + beam_width + br_width, plate_height, ptList[16])
curves(a(range_a, step, -br_width), b(range_b, step, -br_width), v,
       plate_height, ptList[17])
curvesB(-br_width, plate_height, ptList[17])
'''
curvesC(a(range_a, step, 0), b(range_b, step, 0), v, 0, ptList[18])
curvesE(a(range_a, step, plinth), b(range_b, step, plinth), ibeam_height,
        ptList[19])
curvesC(a(range_a, step, plinth + spacing), b(range_b, step, plinth + spacing),
        v, 0, ptList[20])
curvesE(a(range_a, step, plinth + spacing), b(range_b, step, plinth + spacing),
        ibeam_height, ptList[21])
curvesC(a(range_a, step, 2.0 * spacing + plinth),
        b(range_b, step, 2.0 * spacing + plinth), v, 0, ptList[22])
curvesE(a(range_a, step, 2.0 * spacing + plinth),
        b(range_b, step, 2.0 * spacing + plinth), ibeam_height, ptList[23])
curvesC(a(range_a, step, 3.0 * spacing + 2.0 * plinth),
        b(range_b, step, 3.0 * spacing + 2.0 * plinth), v, 0, ptList[24])
curvesE(a(range_a, step, 3.0 * spacing + plinth),
        b(range_b, step, 3.0 * spacing + plinth), ibeam_height, ptList[25])
curvesC(a(range_a, step, beam_distance), b(range_b, step, beam_distance), v, 0,
        ptList[26])
curvesE(a(range_a, step, beam_distance + plinth),
        b(range_b, step, beam_distance + plinth), obeam_height, ptList[27])
curvesC(a(range_a, step, beam_distance + plinth + spacing),
        b(range_b, step, beam_distance + plinth + spacing), v, 0, ptList[28])
curvesE(a(range_a, step, beam_distance + plinth + spacing),
        b(range_b, step, beam_distance + plinth + spacing), obeam_height,
        ptList[29])
curvesC(a(range_a, step, beam_distance + plinth + 2.0 * spacing),
        b(range_b, step, beam_distance + plinth + 2.0 * spacing), v, 0,
        ptList[30])
curvesE(a(range_a, step, beam_distance + plinth + 2.0 * spacing),
        b(range_b, step, beam_distance + plinth + 2.0 * spacing), obeam_height,
        ptList[31])
curvesC(a(range_a, step, beam_distance + 2.0 * plinth + 3.0 * spacing),
        b(range_b, step, beam_distance + 2.0 * plinth + 3.0 * spacing), v, 0,
        ptList[32])
curvesE(a(range_a, step, beam_distance + plinth + 3.0 * spacing),
        b(range_b, step, beam_distance + plinth + 3.0 * spacing), obeam_height,
        ptList[33])
curvesC(a(range_a, step, beam_distance + beam_width + br_width),
        b(range_b, step, beam_distance + beam_width + br_width), v,
        plate_height, ptList[34])
curvesC(a(range_a, step, -br_width), b(range_b, step, -br_width), v,
        plate_height, ptList[35])

curvesD(0, 0, ptList[18])
curvesD(plinth, ibeam_height, ptList[19])
curvesD(plinth + spacing, 0, ptList[20])
curvesD(plinth + spacing, ibeam_height, ptList[21])
curvesD(2.0 * spacing + plinth, 0, ptList[22])
curvesD(2.0 * spacing + plinth, ibeam_height, ptList[23])
curvesD(3.0 * spacing + 2.0 * plinth, 0, ptList[24])
curvesD(3.0 * spacing + plinth, ibeam_height, ptList[25])
curvesD(beam_distance, 0, ptList[26])
curvesD(beam_distance + plinth, obeam_height, ptList[27])
curvesD(beam_distance + plinth + spacing, 0, ptList[28])
curvesD(beam_distance + plinth + spacing, obeam_height, ptList[29])
curvesD(beam_distance + plinth + 2.0 * spacing, 0, ptList[30])
curvesD(beam_distance + plinth + 2.0 * spacing, obeam_height, ptList[31])
curvesD(beam_distance + 2.0 * plinth + 3.0 * spacing, 0, ptList[32])
curvesD(beam_distance + plinth + 3.0 * spacing, obeam_height, ptList[33])
curvesD(beam_distance + beam_width + br_width, plate_height, ptList[34])
curvesD(-br_width, plate_height, ptList[35])
'''
for Curve in range(0, len(ptList)):
    Lista = ptList[Curve]
    n = len(Lista)
    deg = 1
    m = n + deg + 1
    controlPoints = Lista
    knotPoints = linspace(0, 1, m)
    createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()

# Pierwsza płaszczyzna
_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_1 = part_1.getCurve(name="Curve 18")
_target.extend(curve_1.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_2 = part_1.getCurve(name="Curve 1")
_target.extend(curve_2.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)
# druga płaszczyzna
_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_2 = part_1.getCurve(name="Curve 1")
_target.extend(curve_2.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_3 = part_1.getCurve(name="Curve 3")
_target.extend(curve_3.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

# trzecia płaszczyzna
_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_3 = part_1.getCurve(name="Curve 3")
_target.extend(curve_3.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_4 = part_1.getCurve(name="Curve 5")
_target.extend(curve_4.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_5 = part_1.getCurve(name="Curve 7")
_target.extend(curve_5.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_4 = part_1.getCurve(name="Curve 5")
_target.extend(curve_4.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_6 = part_1.getCurve(name="Curve 9")
_target.extend(curve_6.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_5 = part_1.getCurve(name="Curve 7")
_target.extend(curve_5.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_7 = part_1.getCurve(name="Curve 11")
_target.extend(curve_7.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_6 = part_1.getCurve(name="Curve 9")
_target.extend(curve_6.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_8 = part_1.getCurve(name="Curve 13")
_target.extend(curve_8.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_7 = part_1.getCurve(name="Curve 11")
_target.extend(curve_7.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_9 = part_1.getCurve(name="Curve 15")
_target.extend(curve_9.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_8 = part_1.getCurve(name="Curve 13")
_target.extend(curve_8.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_9 = part_1.getCurve(name="Curve 15")
_target.extend(curve_9.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_10 = part_1.getCurve(name="Curve 17")
_target.extend(curve_10.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_2 = part_1.getCurve(name="Curve 1")
_target.extend(curve_2.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_11 = part_1.getCurve(name="Curve 2")
_target.extend(curve_11.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_3 = part_1.getCurve(name="Curve 3")
_target.extend(curve_3.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_12 = part_1.getCurve(name="Curve 4")
_target.extend(curve_12.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_4 = part_1.getCurve(name="Curve 5")
_target.extend(curve_4.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_13 = part_1.getCurve(name="Curve 6")
_target.extend(curve_13.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_5 = part_1.getCurve(name="Curve 7")
_target.extend(curve_5.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_14 = part_1.getCurve(name="Curve 8")
_target.extend(curve_14.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_6 = part_1.getCurve(name="Curve 9")
_target.extend(curve_6.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_15 = part_1.getCurve(name="Curve 10")
_target.extend(curve_15.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_7 = part_1.getCurve(name="Curve 11")
_target.extend(curve_7.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_16 = part_1.getCurve(name="Curve 12")
_target.extend(curve_16.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_8 = part_1.getCurve(name="Curve 13")
_target.extend(curve_8.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_17 = part_1.getCurve(name="Curve 14")
_target.extend(curve_17.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_9 = part_1.getCurve(name="Curve 15")
_target.extend(curve_9.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_18 = part_1.getCurve(name="Curve 16")
_target.extend(curve_18.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_11 = part_1.getCurve(name="Curve 2")
_target.extend(curve_11.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_12 = part_1.getCurve(name="Curve 4")
_target.extend(curve_12.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_12 = part_1.getCurve(name="Curve 4")
_target.extend(curve_12.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_13 = part_1.getCurve(name="Curve 6")
_target.extend(curve_13.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_13 = part_1.getCurve(name="Curve 6")
_target.extend(curve_13.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_14 = part_1.getCurve(name="Curve 8")
_target.extend(curve_14.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_15 = part_1.getCurve(name="Curve 10")
_target.extend(curve_15.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_16 = part_1.getCurve(name="Curve 12")
_target.extend(curve_16.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_16 = part_1.getCurve(name="Curve 12")
_target.extend(curve_16.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_17 = part_1.getCurve(name="Curve 14")
_target.extend(curve_17.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_17 = part_1.getCurve(name="Curve 14")
_target.extend(curve_17.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_18 = part_1.getCurve(name="Curve 16")
_target.extend(curve_18.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=False)

ptList_e = []
n_of_curve_e = 2

for i in range(0, n_of_curve_e):
    ptList_e.append([])

Elipsa(3.5, 0.75, 0, 12.5, ptList_e[0])
Elipsa(1.75 / 2, 0.75, 10, 9.875, ptList_e[1])

for elipsa in range(0, len(ptList_e)):
    Lista = ptList_e[elipsa]
    n = len(Lista)
    deg = 1
    m = n + deg + 1
    controlPoints = Lista
    knotPoints = linspace(0, 1, m)
    createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()

_list = []
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_1 = part_1.getCurve(name="Curve 20")
_target.extend(curve_1.getEdges())
_list.append(_target)
_target = apex.EntityCollection()
part_1 = apex.getPart(pathName="Model/Part 1")
curve_2 = part_1.getCurve(name="Curve 19")
_target.extend(curve_2.getEdges())
_list.append(_target)
result = apex.geometry.createSurfaceLofted(
    name='',
    target=_list,
    loftClampingMethod=apex.geometry.LoftClampingMethod.No,
    clampStartProfile=True,
    clampEndProfile=True,
    stitch=True)


class Knots:
    # Class defining curves A

    def __init__(self, a, b, Velocity, Distance, ListPoint):
        t = 0
        count = len(a)
        z = range(0, count)
        for i in z:
            self.x = a[i] * math.cos(t) + 15
            self.y = b[i] * math.sin(t)
            self.z = Velocity * t + Distance
            ListPoint.append(
                createPointXYZ(x=self.x, y=self.y, z=self.z).asPoint())
            t += math.pi / 4.0


def a0(tmax, Step):
    """center"""
    radius = []
    t = 0
    while t <= tmax:
        radius.append(0)
        t += Step
    return radius


slow_step = math.pi / 4.0

# Lists of point for all curves
ptList_p = []

n_of_curve = 21

for i in range(0, n_of_curve):
    ptList_p.append([])
# Do przeróbki:

# Do przeróbki:
Curves(a0(range_a, slow_step), a0(range_b, slow_step), v, pr_height - 0.4,
       ptList_p[0])
# //
Curves(a(range_a, slow_step, plinth), b(range_b, slow_step, plinth), v,
       ibeam_height, ptList_p[1])
Curves(a(range_a, slow_step, spacing + plinth),
       b(range_b, slow_step, spacing + plinth), v, ibeam_height, ptList_p[2])
Curves(a(range_a, slow_step, 2.0 * spacing + plinth),
       b(range_b, slow_step, 2.0 * spacing + plinth), v, ibeam_height,
       ptList_p[3])
Curves(a(range_a, slow_step, 3.0 * spacing + plinth),
       b(range_b, slow_step, 3.0 * spacing + plinth), v, ibeam_height,
       ptList_p[4])
Curves(a(range_a, slow_step, beam_distance + plinth),
       b(range_b, slow_step, beam_distance + plinth), v, obeam_height,
       ptList_p[5])
Curves(a(range_a, slow_step, beam_distance + plinth + spacing),
       b(range_b, slow_step, beam_distance + plinth + spacing), v,
       obeam_height, ptList_p[6])
Curves(a(range_a, slow_step, beam_distance + plinth + 2.0 * spacing),
       b(range_b, slow_step, beam_distance + plinth + 2.0 * spacing), v,
       obeam_height, ptList_p[7])
Curves(a(range_a, slow_step, beam_distance + plinth + 3.0 * spacing),
       b(range_b, slow_step, beam_distance + plinth + 3.0 * spacing), v,
       obeam_height, ptList_p[8])
Curves(
    a(range_a, slow_step,
      beam_distance + 2.0 * plinth + 3.0 * spacing + br_width),
    b(range_b, slow_step,
      beam_distance + 2.0 * plinth + 3.0 * spacing + br_width), v, pr_height,
    ptList_p[9])
Curves(
    a(range_a, slow_step,
      beam_distance + 2.0 * plinth + 3.0 * spacing + br_width),
    b(range_b, slow_step,
      beam_distance + 2.0 * plinth + 3.0 * spacing + br_width), v, 0,
    ptList_p[10])
Curves(a(range_a, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing),
       b(range_b, slow_step, beam_distance + 2.0 * plinth + 3.0 * spacing), v,
       0, ptList_p[11])
Curves(a(range_a, slow_step, beam_distance + plinth + 2.0 * spacing),
       b(range_b, slow_step, beam_distance + plinth + 2.0 * spacing), v, 0,
       ptList_p[12])
Curves(a(range_a, slow_step, beam_distance + plinth + spacing),
       b(range_b, slow_step, beam_distance + plinth + spacing), v, 0,
       ptList_p[13])
Curves(a(range_a, slow_step, beam_distance),
       b(range_b, slow_step, beam_distance), v, 0, ptList_p[14])
Curves(a(range_a, slow_step, 3.0 * spacing + 2.0 * plinth),
       b(range_b, slow_step, 3.0 * spacing + 2.0 * plinth), v, 0, ptList_p[15])
Curves(a(range_a, slow_step, 2.0 * spacing + plinth),
       b(range_b, slow_step, 2.0 * spacing + plinth), v, 0, ptList_p[16])
Curves(a(range_a, slow_step, spacing + plinth),
       b(range_b, slow_step, spacing + plinth), v, 0, ptList_p[17])
Curves(a(range_a, slow_step, 0), b(range_b, slow_step, 0), v, 0, ptList_p[18])
Curves(a(range_a, slow_step, -br_width), b(range_b, slow_step, -br_width), v,
       0, ptList_p[19])
Curves(a0(range_a, slow_step), a0(range_b, slow_step), v, 0, ptList_p[20])

size = len(ptList_p[10])
new_ptList = []

for nr_przepony in range(0, size):
    new_ptList.append([])
    for list in ptList_p:
        new_ptList[nr_przepony].append(list[nr_przepony])

for Curve in range(0, len(new_ptList)):
    Lista = new_ptList[Curve]
    n = len(Lista)
    deg = 1
    m = n + deg + 1
    controlPoints = Lista
    knotPoints = linspace(0, 1, m)
    createCurve3DNurb(controlPoints, knotPoints, deg).asCurve()

for i in range(21, 38):
    _target = apex.EntityCollection()
    part_1 = apex.getPart(pathName="Model/Part 1")
    curve_1 = part_1.getCurve(name="Curve {}".format(i))
    _target.extend(curve_1.getEdges())
    result = apex.geometry.fillerSurface(target=_target)