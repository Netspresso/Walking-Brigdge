import apex
from apex.construct import Point3D, Point2D
from apex.geometry import createPointXYZ, createCurve3DNurb
import math

apex.setScriptUnitSystem(unitSystemName=r'''mm-kg-s-N''')
applicationSettingsGeometry = apex.setting.ApplicationSettingsGeometry()
applicationSettingsGeometry.createGeometryInNewPart = apex.setting.CreateGeometryInNewPart.CurrentPart
applicationSettingsGeometry.geometryTessellationIsWatertight = False
applicationSettingsGeometry.geometryEdgeTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
applicationSettingsGeometry.geometryFaceTesselationTolerance = apex.setting.GeometryTessellationTolerance.Medium
apex.setting.setApplicationSettingsGeometry(
    applicationSettingsGeometry=applicationSettingsGeometry)
model_1 = apex.currentModel()


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


def odsetep_slupa(t):
    if (t >= 0 and t < math.pi):
        return -2 / math.pi * t + 4
    elif (t >= 1 * math.pi and t < 2 * math.pi):
        return 2 / math.pi * t
    elif (t >= 2 * math.pi and t < 3 * math.pi):
        return -2 / math.pi * t + 8
    elif (t >= 3 * math.pi and t < 4 * math.pi):
        return 2 / math.pi * t - 4
    elif (t >= 4 * math.pi and t < 5 * math.pi):
        return -2 / math.pi * t + 12
    else:
        return 2 / math.pi * t - 8


def a_p(tmax, Step, component, beginning):
    """Inner radius(f) (from center to the beam)"""
    radius = []
    t = beginning
    while t <= tmax:
        radius.append((-5 / (4 * math.pi)) * beginning + 10.0 - component(t))
        t += Step
    return radius


def b_p(tmax, Step, component, beginning):
    """Inner radius(f) (from center to the beam)"""
    radius = []
    t = beginning
    while t <= tmax:
        radius.append((-5 / (4 * math.pi)) * beginning + 7.5 - component(t))
        t += Step
    return radius


ptList = []
n_of_curve = 2
slow_step = math.pi / 24.0
v = 2.0 / math.pi

for i in range(0, n_of_curve):
    ptList.append([])

Elipsa(a_p(2 * math.pi, slow_step, odsetep_slupa, 0), -1, ptList[0])
Elipsa_2(a_p(2 * math.pi, slow_step, odsetep_slupa, 0), v * 4 * math.pi + 1,
         ptList[1])

for elipsa in range(0, len(ptList)):
    Lista = ptList[elipsa]
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
